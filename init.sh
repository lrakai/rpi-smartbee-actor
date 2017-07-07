#!/bin/bash

# Upgrade and install firefox and pip
sudo apt-get update
sudo apt-get -y dist-upgrade
sudo apt-get install -y firefox python-pip xvkbd unclutter git
sudo apt-get clean
# geckodriver=geckodriver-v0.17.0-linux64 # For x86_64 architectures
geckodriver=geckodriver-v0.17.0-arm7hf # For ARM architectures
curl -LO https://github.com/mozilla/geckodriver/releases/download/v0.17.0/${geckodriver}.tar.gz
sudo tar -zxf ${geckodriver}.tar.gz -C /usr/local/bin
rm ${geckodriver}.tar.gz

pip install virtualenv

# Create a virtual environment for the script
mkdir smartbee-actor
virtualenv smartbee-actor
source smartbee-actor/bin/activate
pip install -U selenium configparser
deactivate

# Ensure permission to execute the run script
chmod u+x run.sh

# Clone reference source
git clone https://github.com/lrakai/rpi-smartbee-actor.git
cd rpi-smartbee-actor
git log -1 --date=iso-strict | grep Date\: | awk '{print $2}' > found_commit
cd ..
cp rpi-smartbee-actor/found_commit installed_commit