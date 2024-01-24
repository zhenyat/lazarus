/************************************************
 * Creates table Respondents                    *
 *                                              *
 *    id          - Primary key                 *
 *    school_id   - Foreign key                 *
 *    gender         - enumerated  {'F' | 'M'}     *
 *    age         - 14 <= age <= 60 (Wasserman) *
 *    form        - enumerated  {9 | 11}        *
 *                                              *
 *  30.11.2023  Rada Telyukova                  *
 * * * * * * * * * * * * * * * * * * * * * * * **/
CREATE TABLE IF NOT EXISTS Respondents (
  id INTEGER PRIMARY KEY,
  school_id INTEGER NOT NULL,
  gender TEXT NOT NULL CHECK(gender IN ('F', 'M')) DEFAULT 'F',
  age INTEGER NOT NULL CHECK (
    age >= 14
    AND age <= 60
  ),
  form INTEGER NOT NULL CHECK(form IN (9, 11)) DEFAULT 9,
  FOREIGN KEY(school_id) REFERENCES Schools(id) ON DELETE CASCADE
);
.print "\nTable 'Respondents' has been created with schema:".schema Respondents