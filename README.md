#   Lazarus Ways of Coping Checklist

## Author: Rada Telyukova

## IDE
* OS:       macOS
* RDBMS:    SQLite3
* Editor:   VS Code
* Programming languages: Python, SQL

### DB GUI:
  - DB Browser for SQLite
  - Valentina Studio

## Commands to create and populate Production DB:
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
