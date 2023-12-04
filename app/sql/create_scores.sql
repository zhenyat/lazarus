/********************************************************************
 *  Creates table Scores - final (summary) table of the field data    *
 *                         for futher analysis                      *
 *                                                                  *
 *      id                - Primary key                             *
 *      respondent_id     - Foreign key                             *
 *      model             - enum { 'original' | 'standard'  }       *
 *      s1 ... s8         - Score for Scales 1..8                   *
 *                                                                  *
 *  03.12.2023  Rada                                                *
 ********************************************************************/
CREATE TABLE IF NOT EXISTS Scores (
  id INTEGER PRIMARY KEY,
  respondent_id INTEGER NOT NULL,
  model TEXT NOT NULL CHECK(model IN ('original', 'standard')),
  s1 INTEGER NOT NULL,      -- score for scale 1
  s2 INTEGER NOT NULL,      -- score for scale 2
  s3 INTEGER NOT NULL,      -- score for scale 3
  s4 INTEGER NOT NULL,      -- score for scale 4
  s5 INTEGER NOT NULL,      -- score for scale 5
  s6 INTEGER NOT NULL,      -- score for scale 6
  s7 INTEGER NOT NULL,      -- score for scale 7
  s8 INTEGER NOT NULL,      -- value for scale 8
  FOREIGN KEY(respondent_id) REFERENCES Respondents(id) ON DELETE CASCADE
);
.print "\nTable 'Scores' has been created with schema:"
.schema Scores
