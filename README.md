# Mastodon bot

Based on this [Platypus blog post](https://blog.platypush.tech/article/Create-a-Mastodon-bot-to-forward-Twitter-and-RSS-feeds-to-your-timeline).

Create a Mastodon bot to forward Twitter and RSS feeds to your timeline.

# Docker

```Shell
# Create containers for services and start services
docker compose -p mastodon-bot-project create
docker compose -p mastodon-bot-project start
# or
docker compose -p mastodon-bot-project up --detach

# Connect to the running container:
docker exec -it bot-app bash # or bot-redis

# Stop services
docker compose -p mastodon-bot-project stop
# Or stop and remove containers, networks
docker compose -p mastodon-bot-project down
```

# Without containers

## Install Redis

Mac
```Shell
brew install redis

redis-server # start Redis 

# or run Redis in the background
brew services start redis # brew services stop redis
brew services info redis 
```

## Install and run your bot.

```Shell
git clone git@github.com:santisbon/newsbot.git && cd newsbot
mkdir -p ~/.config/platypush/scripts
ln -sf <repo dir>/config.yaml ~/.config/platypush/config.yaml
ln -sf <repo dir>/scripts/mastodon_queue_bot.py ~/.config/platypush/scripts/mastodon_bot.py
pip3 install 'platypush[rss]'

platypush
```
