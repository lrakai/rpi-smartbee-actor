# rpi-smartbee-actor
Automate staying signed into and navigating to target pages of a SmartBee hive using a raspberry pi

## Running
Prepare your working directory with:
```shell
bash init.sh
```
Then run the actor with:
```shell
bash run.sh
```

## Configuration
You need create a configuration file named `smartbee_actor.conf` in the project directory to configure how the actor behaves.
An example is provided in `smartbee_actor.example.conf`. 
You only need to configure the `SERVER` section to have the actor sign in when automatically signed out, return to room `1`, and focus on the metrics graph.
