#   Lazarus Ways of Coping Checklist (WCCL)

## Author: Rada Telyukova. HSE Lyceum, Moscow, Russia

### IDE
* OS:       macOS
* RDBMS:    SQLite3
* Editor:   VS Code
* Programming languages: Python, SQL

### DB GUI:
  - DB Browser for SQLite
  - Valentina Studio

### Commands to create and populate Production DB:
```sh
  % rm db/lazarus.sqlite3
  % sqlite3 db/lazarus.sqlite3
    > .read app/sql/create_schools.sql
    > .read app/sql/create_scales.sql
    > .read app/sql/create_questionnaire.sql
    > .read app/sql/create_points.sql
    > .read app/sql/create_respondents.sql
    > .read app/sql/create_responses.sql
    > .read app/sql/create_scores.sql
```

###  Batch mode to create Production DB & populate tables with field data:
```sh
  % bin/init_db.sh production
  % app/python/production/main.py
```
###  Batch mode to create Ground DB & populate tables with faked data:
```sh
  % bin/init_db.sh ground
  % app/python/ground/generate_fakes.py
```
##
### Data Analysis
```
  TBD
```