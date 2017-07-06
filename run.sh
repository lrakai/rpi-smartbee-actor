#!/bin/bash

fullscreen_delay=10
script=smartbee_actor.py
if [[ $# -eq 1 ]]; then
    script=$1
fi

rm -f geckodriver.log
ps | grep geckodriver | awk '{print $1}' | xargs kill &> /dev/null
ps | grep firefox | awk '{print $1}' | xargs kill &> /dev/null
ps | grep unclutter | awk '{print $1}' | xargs kill &> /dev/null

unclutter -idle 0.1 -root &
source smartbee-actor/bin/activate
(sleep $fullscreen_delay; xvkbd -window Firefox -text "\[0xffc8]")&
python $script
deactivate