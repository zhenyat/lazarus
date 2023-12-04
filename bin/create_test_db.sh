#! /usr/bin/env zsh

########################################
#   Creates and populates test DB
#       Parameter $1 - DB filename
#########################################

if [ -f "$1" ]; 
then
    rm "$1"         # Remove DB if exists
fi

# app/python/tests/generate_fakes.py
