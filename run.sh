#!/bin/bash

actor_pid_file=actor.pid
update_check_period=3600

clean_up ()
{   echo ">> cleaning up old logs and processes"
    rm -f geckodriver.log
    ps | grep geckodriver | awk '{print $1}' | xargs kill &> /dev/null
    ps | grep firefox | awk '{print $1}' | xargs kill &> /dev/null
    ps | grep unclutter | awk '{print $1}' | xargs kill &> /dev/null
    ps | grep python | awk '{print $1}' | xargs kill &> /dev/null
}

pull_code ()
{   echo ">> checking for code updates and updating last found commit timestamp"
    caller_directory=`pwd`
    cd rpi-smartbee-actor
    git pull origin master
    git log -1 --date=iso-strict | grep Date\: | awk '{print $2}' > found_commit
    cd $caller_directory
}

need_update ()
{   echo ">> comparing installed commit and last pulled commit"
    found_commit=`cat rpi-smartbee-actor/found_commit`
    installed_commit=`cat installed_commit`
    found=`date -d $found_commit +%s`
    installed=`date -d $installed_commit +%s`

    if [ $found -gt $installed ]; then
        echo ">> update required"
        return 0
    else
        echo ">> no update required"
        return 1
    fi  
}

update ()
{   echo ">> updating the code and restarting the actor"
    stop_actor
    rsync -a --exclude found_commit rpi-smartbee-actor/ .
    start_actor
}

start_actor ()
{   echo ">> starting actor"
    clean_up
    bash act.sh&
    echo $! > $actor_pid_file
}

stop_actor ()
{   echo ">> stopping actor"
    if [ -e $actor_pid_file ]; then
        kill `cat $actor_pid_file`
        rm $actor_pid_file
    fi
}

start_actor

while true; do
    echo ">> sleeping for $update_check_period seconds"
    sleep $update_check_period
    pull_code
    if need_update; then
        update
    fi
done
