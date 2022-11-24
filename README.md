# @newsbot@mstdn.social

Based on this [Platypus blog post](https://blog.platypush.tech/article/Create-a-Mastodon-bot-to-forward-Twitter-and-RSS-feeds-to-your-timeline).

Create a Mastodon bot to forward Twitter and RSS feeds to your timeline.

Install Redis
```Shell
brew install redis

redis-server # start Redis 

# or run Redis in the background
brew services start redis # brew services stop redis
brew services info redis 
```

Install and run your bot.
```Shell
git clone git@github.com:santisbon/newsbot.git && cd newsbot
mkdir -p ~/.config/platypush/scripts
ln -sf <newsbot dir>/.config/platypush/config.yaml ~/.config/platypush/config.yaml
ln -sf <newsbot dir>/.config/platypush/scripts/mastodon_queue_bot.py ~/.config/platypush/scripts/mastodon_bot.py
pip3 install 'platypush[rss]'

platypush
```