# Mastodon bot

Create a Mastodon bot to forward Twitter and RSS feeds to your timeline.
Inspired by this [Platypush blog post](https://blog.platypush.tech/article/Create-a-Mastodon-bot-to-forward-Twitter-and-RSS-feeds-to-your-timeline).  

Recommended deployment: on Docker containers running on a Raspberry Pi.  
[How to set up a Raspberry Pi](https://github.com/santisbon/guides/blob/main/setup/raspberry-pi.md)  
[How to set up Docker](https://github.com/santisbon/guides/blob/main/setup/docker.md)  

---  
## Instructions

1. Grab the code.
```Shell
git clone https://github.com/santisbon/mastodonbot.git && cd mastodonbot
```

2. Edit `config.yaml` to set your Mastodon `base_url`, `access_token`, and `subscriptions`.  
Edit `compose.yaml` to set the correct `platform` for your [hardware](https://github.com/santisbon/guides/blob/main/setup/docker.md#architecture).  

3. To start or stop the bot:
```Shell
docker compose -p mastodon-bot-project up --detach
```
```Shell
docker compose -p mastodon-bot-project down
```