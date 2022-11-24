# newsbot

```python
mkdir -p ~/.config/platypush/scripts
ln -sf <newsbot dir>/.config/platypush/config.yaml ~/.config/platypush/config.yaml
ln -sf <newsbot dir>/.config/platypush/scripts/mastodon_queue_bot.py ~/.config/platypush/scripts/mastodon_bot.py
pip3 install 'platypush[rss]'

platypush
```