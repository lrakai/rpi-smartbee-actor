#!/bin/bash

script=browser_sign_in.py
if [[ $# -eq 1 ]]; then
    script=$1
fi

source browser-sign-in/bin/activate
python $script
deactivate