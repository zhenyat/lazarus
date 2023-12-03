/*******************************************************************************
 *  Creates table 'Points' and populates it with CSV data                      *
 *    Includes:                                                                *
 *        original points (Kryukova et el.)                                    *
 *        standard (Wasserman et al.) points                                   *
 *     https://psylab.info/Опросник_«Способы_совладающего_поведения»_Лазаруса  *
 *                                                                             *
 *    id                  - Primary key                                        *
 *    scale_id            - Foreign key                                        *
 *    original_points     - Original values                                    *
 *    male_u20_points     - Standard values for males under 20                 *
 *    male_21_30_points   - Standard values for males under 21-30              *
 *    male_31_45_points   - Standard values for males under 31-45              *
 *    male_46_60_points   - Standard values for males under 46-60              *
 *    female_u20_points   - Standard values for females under 20               *
 *    female_21_30_points - Standard values for females under 21-30            *
 *    female_31_45_points - Standard values for females under 31-45            *
 *    female_46_60_points - Standard values for females under 46-60            *
 *                                                                             *
 *  29.11.2023  Rada                                                           *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
CREATE TABLE IF NOT EXISTS Points (
  id INTEGER PRIMARY KEY,
  scale_id INTEGER NOT NULL,
  original_points INTEGER NOT NULL,
  male_u20_points INTEGER NOT NULL,
  male_21_30_points INTEGER NOT NULL,
  male_31_45_points INTEGER NOT NULL,
  male_46_60_points INTEGER NOT NULL,
  female_u20_points INTEGER NOT NULL,
  female_21_30_points INTEGER NOT NULL,
  female_31_45_points INTEGER NOT NULL,
  female_46_60_points INTEGER NOT NULL,
  FOREIGN KEY(scale_id) REFERENCES Scales(id) ON DELETE CASCADE
);
.print "\nTable 'Points' has been created with schema:"
.schema Points

-- Get CSV data
.mode csv
.header off
.import db/csv/points.csv Points

.mode columns
.print "\nTable 'Points' has been populated"
.print "\nNumber of rows:"
SELECT count(*) FROM Points;

.print "\nFirst and last rows:"
SELECT * FROM Points WHERE (id = 1 OR id = 158);
