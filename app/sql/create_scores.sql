/********************************************************************
 *  Creates table Scores - final (summary) table of the field data    *
 *                                                                  *
 *      id                - Primary key                             *
 *      respondent_id     - Foreign key                             *
 *      kind              - enum { 'original' | 'standard'  }       *
 *      v1 ... v8         - Score values for Scales 1...8           *
 *                                                                  *
 *  20.11.2023  Rada                                                *
 ********************************************************************/
CREATE TABLE IF NOT EXISTS Scores (
  id INTEGER PRIMARY KEY,
  respondent_id INTEGER NOT NULL,
  kind TEXT NOT NULL CHECK(kind IN ('original', 'standard')),
  v1 INTEGER NOT NULL,      -- value for scale 1
  v2 INTEGER NOT NULL,      -- value for scale 2
  v3 INTEGER NOT NULL,      -- value for scale 3
  v4 INTEGER NOT NULL,      -- value for scale 4
  v5 INTEGER NOT NULL,      -- value for scale 5
  v6 INTEGER NOT NULL,      -- value for scale 6
  v7 INTEGER NOT NULL,      -- value for scale 7
  v8 INTEGER NOT NULL,      -- value for scale 8
  FOREIGN KEY(respondent_id) REFERENCES Respondents(id) ON DELETE CASCADE
);
.print "\nTable 'Scores' has been created with schema:"
.schema Scores
