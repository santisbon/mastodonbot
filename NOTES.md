# Notes

## Configuration 

Goes here:
```Shell
# global
/etc/platypush/config.yaml
/etc/platypush/scripts/
# user
~/.config/platypush/config.yaml
~/.config/platypush/scripts/
```

You can override the config.yaml location via the command line:
```
platypush -c "/path/to/config.yaml"
```

## Kubernetes

This project is meant to run on a single, small machine like a Raspberry Pi. However, Kubernetes can be used to make sure the app recovers from a crash as long as the bot docker image is pulled from a private registry.  

The reason for a private registry is that Platypush doesn't support specifying an access token programatically. It's always loaded from the config file. This means the container image that k8s pulls from the registry contains that secret instead of gettting it from the orchestrator's secrets store.  




