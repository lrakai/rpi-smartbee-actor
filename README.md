# rpi-smartbee-actor
Automate staying signed into and navigating to target pages of a SmartBee hive using a raspberry pi 3 running ubuntu 16. The original applicaiton was to display the metric chart for a room on a display at the entrance of the room. The features include:
- Automatic sign in and re-sign in when timed out
- Automatic navigation to the metrics chart of the configured room
- Automatic entering full screen mode of the browser
- Automatic hiding of the cursor
- Extending the graph across the full width of the page
- Automatic updates from the configured Git repository 
- Removal of the honeycomb background styling

The default view of a room metric chart looks as follows:
<img src="https://user-images.githubusercontent.com/3911650/27997102-57acccec-64ae-11e7-9b30-e07fc13e893e.png" alt="Without actor">

When using the actor the view is as follows:
<img src="https://user-images.githubusercontent.com/3911650/27997042-9abeb8c6-64ac-11e7-8db1-ed94f545e2f5.png" alt="With actor">

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

## Automatic Updates
When an agent is configured using init.sh it pulls reference source from a Git repository (this repository by default). When the actor is started using run.sh, it also periodically checks for more recent commits in the Git repository. If detected, the actor is terminated and restarted with the new version of the code.