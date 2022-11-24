import logging
import re
import requests

from queue import Queue, Empty
from threading import Thread
from time import time

from platypush.event.hook import hook
from platypush.message.event.application import ApplicationStartedEvent
from platypush.message.event.rss import NewFeedEntryEvent
from platypush.utils import run

logger = logging.getLogger('rss2mastodon')
url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# How often the events should be flushed, in seconds
flush_interval = 30

# Maximum number of items to be flushed per iteration
batch_size = 10

# Shared events queue
events_queue = Queue()

# Utility function to parse bit.ly links content
def parse_bitly_link(link):
    rs = requests.get(link, allow_redirects=False)
    return rs.headers.get('Location', link)


def feed_entries_publisher():
    events_cache = []

    while True:
        # Read an event from the queue
        try:
            events_cache.append(
                events_queue.get(timeout=0.5)
            )
        except Empty:
            continue

        # Only pick the most recent events
        events = sorted(
            filter(lambda e: e.published, events_cache),
            key=lambda e: e.published,
            reverse=True
        )[:batch_size]

        for event in events:
          try:
            # Your event conversion and `mastodon.publish_status`
            # logic goes here
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
              content = f'{content}\n\n{source_name}: {item_url}'
              #if referenced_urls:
                #content = f'Referenced link: {referenced_urls[-1]}\n{content}'

              # Publish the status to Mastodon
              run(
                'mastodon.publish_status',
                status=content,
                visibility='public',
              )

              logger.info(f'The URL has been successfully cross-posted: {item_url}')
          except Exception as exc:
              raise RuntimeError('Failed to process event') from exc

        # Reset the events cache
        events_cache.clear()


@hook(ApplicationStartedEvent)
def on_application_started(*_, **__):
    # Start the feed processing thread
    Thread(target=feed_entries_publisher).start()


@hook(NewFeedEntryEvent)
def push_feed_item_to_queue(event, **context):
    # Just push the event to the processor
    events_queue.put(event)