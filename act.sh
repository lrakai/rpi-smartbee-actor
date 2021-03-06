#!/bin/bash

fullscreen_delay=30
script=smartbee_actor.py
if [[ $# -eq 1 ]]; then
    script=$1
fi

unclutter -idle 0.1 -root &
source smartbee-actor/bin/activate
(sleep $fullscreen_delay; xvkbd -window Firefox -text "\[0xffc8]")&
python $script
deactivate