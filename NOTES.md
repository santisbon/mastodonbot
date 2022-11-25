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

## Kubernetes

This project is not a good fit for k8s. It's meant to run on a single, small machine like a Raspberry Pi.  
In addition, Platypush doesn't support specifying an access token programatically. It's always loaded from the config file.  
This means the container image that k8s pulls from a repository would expose that secret instead of gettting it from the orchestrator's secrets store.  




