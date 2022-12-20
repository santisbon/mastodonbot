# Mastodon bot

Create a Mastodon bot to forward Twitter and RSS feeds to your timeline.
Inspired by this [Platypush blog post](https://blog.platypush.tech/article/Create-a-Mastodon-bot-to-forward-Twitter-and-RSS-feeds-to-your-timeline).  

Recommended deployment: on containers (use Docker Compose or Kubernetes) running on a Raspberry Pi.  
See [NOTES.md](NOTES.md) for an important disclaimer when using Kubernetes.  

[How to set up a Raspberry Pi](https://github.com/santisbon/guides/blob/main/setup/raspberry-pi.md)  
[How to set up Docker](https://github.com/santisbon/guides/blob/main/setup/docker.md)  
[How to set up Kubernetes](https://github.com/santisbon/guides/blob/main/setup/k8s.md)

---  
## Instructions

1. Grab the code.
   ```Shell
   git clone https://github.com/santisbon/mastodonbot.git && cd mastodonbot
   ```

2. Configure the app.  
   - Edit `config.yaml` to set your Mastodon `base_url`, `access_token`, and `subscriptions`.  
   - For **Docker Compose**:  
   Edit `compose.yaml` to set the correct `platform` for your [hardware](https://github.com/santisbon/guides/blob/main/setup/docker.md#architecture).  
   In `config.yaml` make sure the Redis `host` matches the cache service `hostname` from the `compose.yaml` file.
   - For **Kubernetes**:  
   In `config.yaml` make sure the Redis `host` is `localhost` as both containers (app and cache) are in the same pod.  
   Build the app image for your target architecture and push it to a **private** registry. Example:
   ```Shell
   docker build -f Dockerfile-app -t localhost:32000/mastodonbot --platform linux/arm64 .
   docker push localhost:32000/mastodonbot
   ```

3. To start or stop the bot:
   - With **Docker Compose**
   ```Shell
   docker compose -p mastodon-bot-project up --detach
   docker compose -p mastodon-bot-project down
   ```
   - With **Kubernetes** (if using microk8s type `microk8s kubectl`)
   ```Shell
   kubectl create namespace botspace
   kubectl apply -f kubernetes-sc.yaml 
   kubectl apply -f kubernetes-pv.yaml
   kubectl apply -f kubernetes-namespace.yaml -n botspace # apply or delete
   ```
