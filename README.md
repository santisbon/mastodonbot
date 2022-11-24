# Mastodon bot

Create a Mastodon bot to forward Twitter and RSS feeds to your timeline.
Based on this [Platypus blog post](https://blog.platypush.tech/article/Create-a-Mastodon-bot-to-forward-Twitter-and-RSS-feeds-to-your-timeline).

# Installation

```Shell
# Create containers for services and start them
docker compose -p mastodon-bot-project up --detach
# or
# docker compose -p mastodon-bot-project create
# docker compose -p mastodon-bot-project start

# If you want to connect to a running container (bot-app or bot-redis)
# docker exec -it bot-app bash

# Stop and remove containers, networks
docker compose -p mastodon-bot-project down
# or just stop services
# docker compose -p mastodon-bot-project stop
```

## Notes
Configuration goes in:
```Shell
# global
/etc/platypush/config.yaml
/etc/platypush/scripts/
# user
~/.config/platypush/config.yaml
~/.config/platypush/scripts/
```
