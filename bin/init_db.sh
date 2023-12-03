#! /usr/bin/env zsh

###############################################
#   Initiates DB (production or test)
#       Parameter $1 - {production | test}}
#
#   02.12.2023  Rada
###############################################
set +xv

if [ -z "$1" ]; # if no parameter
then 
    echo "command format: bin/init_db.sh {production | test}"
else
    if [ "$1" = "test" ]; 
    then
        bin/create_test_db.sh 'db/lazarus_test.sqlite3'

    elif  [ "$1" = "production" ]; then
        bin/create_production_db.sh 'db/lazarus.sqlite3'

    else
        echo "Parameter must be either 'test' or 'production'"
        exit()
    fi
fi
