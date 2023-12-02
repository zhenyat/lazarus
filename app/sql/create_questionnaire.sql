/*********************************************************************
 *   Creates table Questionnaire and populates it with CSV file data  *
 *                                                                   *
 *     id        - Primary key                                       *
 *     scale_id  - Foreign key                                       *
 *     item  - Text of Lazarus 'thoughts or behavior'                *
 *                                                                   *
 *   28.11.2023  Rada                                                *
 *********************************************************************/

CREATE TABLE IF NOT EXISTS Questionnaire (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  scale_id INTEGER NOT NULL,
  item TEXT NOT NULL UNIQUE,
  FOREIGN KEY(scale_id) REFERENCES Scales(id) ON DELETE CASCADE
);

.print "\nTable 'Questionnaire' has been created with schema:"
.schema Questionnaire

-- Get CSV data
.mode csv
.header off
.import db/csv/questionnaire.csv Questionnaire

.mode columns
.print "\nTable 'Questionnaire' has been populated"
.print "\nNumber of rows:"
SELECT count(*) FROM Questionnaire;
.print "\nFirst and last rows:"
SELECT * FROM Questionnaire WHERE (id=1 OR id=50);
