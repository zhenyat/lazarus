#! /usr/bin/env zsh

###############################################
#   Initiates DB (production or test)
#       Parameter $1 - {production | test}}
#
#   02.12.2023  Rada Telyukova, HSE Lyceum 
###############################################
set +xv

if [[ -z "$1" ]]    # if no parameter
then 
    echo "command format: bin/init_db.sh {production | test}"
else
    if [[ "$1" = "production" ]] 
    then
        file="db/lazarus.sqlite3"
    elif [[ "$1" = "test" ]]
    then
        file="db/lazarus_test.sqlite3"
    else
        echo "Parameter must be either 'test' or 'production'"
    fi
    bin/create_db.sh $file
fi
