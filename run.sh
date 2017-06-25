#!/bin/bash

script=smartbee_actor.py
if [[ $# -eq 1 ]]; then
    script=$1
fi

rm -f geckodriver.log
source browser-sign-in/bin/activate
python $script
deactivate