#! /usr/bin/env zsh

##########################################################
#   Shell procedure to create and populate production DB
#       Parameter $1 - DB filename
##########################################################

if [ -f "$1" ]; 
then
    rm "$1"         # Remove DB if exists
fi

sqlite3 "$1" <<'END_SQL'
.read app/sql/create_schools.sql
.read app/sql/create_scales.sql
.read app/sql/create_questionnaire.sql
.read app/sql/create_respondents.sql
.read app/sql/create_responses.sql
.read app/sql/create_points.sql
.read app/sql/create_scores.sql
END_SQL
