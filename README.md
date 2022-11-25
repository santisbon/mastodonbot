# Mastodon bot

Create a Mastodon bot to forward Twitter and RSS feeds to your timeline.
Inspired by this [Platypus blog post](https://blog.platypush.tech/article/Create-a-Mastodon-bot-to-forward-Twitter-and-RSS-feeds-to-your-timeline).

```Shell
git clone git@github.com:santisbon/mastodonbot.git && cd mastodonbot
```

## Deploy with Docker Compose

```Shell
# Create containers for services and start them
docker compose -p mastodon-bot-project up --detach

# Stop and remove containers, networks
docker compose -p mastodon-bot-project down
```

## Deploy with Kubernetes

To deploy to one or more machines on-premises or in the cloud.
```Shell
kubectl apply -f ./k8s
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

You can convert the Docker Compose file to k8s files with:
```Shell
kompose --file compose.yaml convert
```

Instead of ```docker compose up``` you can:
```Shell
docker compose -p mastodon-bot-project create
docker compose -p mastodon-bot-project start
```

If you want to connect to a running container (bot-app or bot-redis)
```Shell
docker exec -it bot-app bash
```

Instead of ```docker compose down``` you can just stop services:
```Shell
docker compose -p mastodon-bot-project stop
```