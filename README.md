# Mastodon bot

Create a Mastodon bot to forward Twitter and RSS feeds to your timeline.
Inspired by this [Platypus blog post](https://blog.platypush.tech/article/Create-a-Mastodon-bot-to-forward-Twitter-and-RSS-feeds-to-your-timeline).

## Get the code.
```Shell
git clone git@github.com:santisbon/mastodonbot.git && cd mastodonbot
```

## Deploy

Edit ```config.yaml``` to set your Mastodon ```base_url``` and ```access_token```.
```Shell
# Create containers for services and start them
docker compose -p mastodon-bot-project up --detach
# Stop and remove containers, networks
docker compose -p mastodon-bot-project down
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
as seen on ```https://github.com/BlackLight/platypush/blob/73f6712f7a550f8ee449e5da756ee5ce06f71d03/platypush/config/__init__.py#L28```  
or rather ```https://git.platypush.tech/platypush/platypush/src/branch/master/platypush/config/__init__.py#L41```  

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

### Kubernetes

This project is not a good fit for k8s. It's meant to run on a single, small machine like a Raspberry Pi.  
In addition, Platypush doesn't support specifying an access token programatically. It's always loaded from the config file.  
This means the container image that k8s pulls from a repository would expose that secret instead of gettting it from the orchestrator's secrets store.  

**For other projects that can benefit from k8s, here are some tips:**

You can convert the Docker Compose file to k8s files with:
```Shell
kompose --file compose.yaml convert
```

Make sure the container image is available in a repository.  
You can build it with ```docker build``` or ```docker compose create``` and push it to a public repository like Docker Hub.
```Shell
docker image push user/repo
# multiple -f filenames or a folder 
kubectl apply -f ./k8s
kubectl get pods
kubectl delete -f ./k8s
```
