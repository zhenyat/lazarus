/************************************************************
 *  Creates and populates table Schools                     *
 *                                                          *
 *     id           - Primary key                           *
 *     nick         - short name for reference              *
 *     title        - Full name of school (cyrillic)        *
 *     short_title  - Short title of school (cyrillic)      *
 *                                                          *
 *  28.11.2023  Rada Telyukova                              *
 *  13.01.2024  Last update                                 *
 ************************************************************/
CREATE TABLE IF NOT EXISTS Schools (
  id INTEGER PRIMARY KEY,
  nick TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL,
  short_title TEXT NOT NULL
);
.print "\nTable 'Schools' has been created with schema:"
.schema Schools

INSERT INTO Schools (nick, title, short_title)
VALUES 
  ('lyceum', 'Лицей НИУ ВШЭ', 'Лицей'),
  ('1570', 'ГБОУ Школа № 1570 г. Москвы', 'Шк.1570');

.print "\nTable 'Schools' has been populated:"
.mode columns
SELECT * FROM Schools;
