# Mastodon bot

Create a Mastodon bot to forward Twitter and RSS feeds to your timeline.
Inspired by this [Platypush blog post](https://blog.platypush.tech/article/Create-a-Mastodon-bot-to-forward-Twitter-and-RSS-feeds-to-your-timeline).  
Recommended deployment: on [Docker](https://github.com/santisbon/guides/blob/main/setup/docker.md) containers running on a [Raspberry Pi](https://github.com/santisbon/guides/blob/main/setup/raspberry-pi.md).

```Shell
git clone https://github.com/santisbon/mastodonbot.git && cd mastodonbot
```

Edit `config.yaml` to set your Mastodon `base_url`, `access_token`, and `subscriptions`.  
Edit `compose.yaml` to set the correct `platform` for your [hardware](https://github.com/santisbon/guides/blob/main/setup/docker.md#architecture).  

```Shell
docker compose -p mastodon-bot-project up --detach
```
```Shell
docker compose -p mastodon-bot-project down
```