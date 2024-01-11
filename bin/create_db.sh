#! /usr/bin/env zsh

##########################################################
#   Shell procedure to create DB and populate tables
#       Parameter $1 - DB filename
#
#   04.12.2023  Rada Telyukova, HSE Lyceum 
##########################################################

if [ -f $1 ]; 
then
    rm $1           # Remove DB if exists
    echo "Old version of DB '$1' removed"
fi

echo "Createing new DB '$1' ..."

sqlite3 $1 <<'END_SQL'
.read app/sql/create_schools.sql
.read app/sql/create_scales.sql
.read app/sql/create_questionnaire.sql
.read app/sql/create_points.sql
.read app/sql/create_respondents.sql
.read app/sql/create_responses.sql
.read app/sql/create_scores.sql
END_SQL
