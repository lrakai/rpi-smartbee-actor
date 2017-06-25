#!/bin/bash

script=smartbee_actor.py
if [[ $# -eq 1 ]]; then
    script=$1
fi

rm -f geckodriver.log
ps | grep geckodriver | awk '{print $1}' | xargs kill &> /dev/null
ps | grep firefox | awk '{print $1}' | xargs kill &> /dev/null
source smartbee-actor/bin/activate
python $script
deactivate