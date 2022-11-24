import logging
import re
import requests

from platypush.event.hook import hook
from platypush.message.event.rss import NewFeedEntryEvent
from platypush.utils import run

logger = logging.getLogger('rss2mastodon')
url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')


# Utility function to parse bit.ly links content
def parse_bitly_link(link):
    rs = requests.get(link, allow_redirects=False)
    return rs.headers.get('Location', link)


# Run this hook when the application receives a `NewFeedEntryEvent`
@hook(NewFeedEntryEvent)
def sync_feeds_to_mastodon(event, **context):
    item_url = event.url or ''
    content = event.title or ''
    source_name = event.feed_title or item_url

    # Find and expand the shortened links
    bitly_links = set(re.findall(r'https?://bit.ly/[a-zA-Z0-9]+', content))
    for link in bitly_links:
        expanded_link = parse_bitly_link(link)
        content = content.replace(link, expanded_link)

    # Find all the referenced URLs
    referenced_urls = url_regex.findall(content)

    # Replace nitter.net prefixes with twitter.com
    if '/nitter.net/' in item_url:
        item_url = item_url.replace('/nitter.net/', '/twitter.com/')
        source_name += '@twitter.com'

    if item_url and content:
        content = f'Originally posted by {source_name}: {item_url}\n\n{content}'
        if referenced_urls:
            content = f'Referenced link: {referenced_urls[-1]}\n{content}'

        # Publish the status to Mastodon
        run(
            'mastodon.publish_status',
            status=content,
            visibility='public',
        )

        logger.info(f'The URL has been successfully cross-posted: {item_url}')