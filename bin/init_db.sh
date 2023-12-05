#! /usr/bin/env zsh

###############################################
#   Initiates DB (production or ground)
#       Parameter $1 - {production | ground}}
#
#   02.12.2023  Rada Telyukova, HSE Lyceum 
###############################################
set +xv

if [[ -z "$1" ]]    # if no parameter
then 
    echo "command format: bin/init_db.sh {production | ground}"
else
    if [[ "$1" = "production" ]] 
    then
        file="db/lazarus.sqlite3"
    elif [[ "$1" = "ground" ]]
    then
        file="db/lazarus_ground.sqlite3"
    else
        echo "Parameter must be either 'production' or 'ground'"
    fi
    bin/create_db.sh $file
fi
