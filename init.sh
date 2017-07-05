#!/bin/bash

# Upgrade and install firefox and pip
sudo apt-get update
sudo apt-get -y dist-upgrade
sudo apt-get install -y firefox python-pip xvkbd
sudo apt-get clean
curl -LO https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz
sudo tar -zxf geckodriver-v0.17.0-linux64.tar.gz -C /usr/local/bin
rm geckodriver-v0.17.0-linux64.tar.gz

pip install virtualenv

# Create a virtual environment for the script
mkdir smartbee-actor
virtualenv smartbee-actor
source smartbee-actor/bin/activate
pip install -U selenium configparser
deactivate

# Ensure permission to execute the run script
chmod u+x run.sh