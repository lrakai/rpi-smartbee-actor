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
You need create a configuration file in the project directory to configure how the actor behaves.
The format of the file is as follows
```text
[DEFAULT]
url=<http://hive_address:hive_port>
password=<hive_password>
room_id=<target_room_id>
target_id=<target_id_to_focus_on>
logged_out_message=<log_out_error_message>
```
The following settings will sign in when automatically signed out, return to room `1`, and focus on the graph:
```text
...
room_id=1
target_id=OuterContainer
logged_out_message=There was a problem with the connection, you have been logged out
```
