#! /usr/bin/env python3

###############################################################################
#   Calculates original (Kryukova et el.) & standard (Wasserman et al.) scores
#   for all respondents
#
#   01.12.2023  Rada
###############################################################################
from sqlite3 import Error
from termcolor import colored
# import db

def populate(conn):
    with conn:
        cur = conn.cursor()

        cur.execute("SELECT id, sex, age FROM Respondents ORDER BY id")
        respondents = cur.fetchall()
        # respondents = cur.fetchmany(10)

        for id, sex, age in respondents:     ### Respondents Loop
            respondent_id = id
            # print('-- ', respondent_id, sex, age)

            # Reset Score arrays
            original_score = [0]*9   # Original Scores by Scale (original_score[0] = 'original')
            original_score[0] = 'original'
            standard_score = [0]*9   # Standard Scores by Scale (standard_score[0] = 'standard')
            standard_score[0] = 'standard'

            # Get all responses of the given Responder
            cur.execute(
                '''
                    SELECT questionnaire_id, answer 
                    FROM Responses
                    WHERE respondent_id=?
                ''',
                (respondent_id,)
            )
            responses = cur.fetchall()

            for questionnaire_id, answer in responses:  # Responses Loop

                # Get Scale
                cur.execute("SELECT scale_id FROM Questionnaire WHERE id=?", 
                    (questionnaire_id,)
                )
                for scale_id, in cur.fetchall():
                    match answer:     # Calculate Original score for the Respondent
                        case 'never':
                            original_score[scale_id] += 0
                        case 'rarely':
                            original_score[scale_id] += 1
                        case 'sometimes':
                            original_score[scale_id] += 2
                        case 'regularly':
                            original_score[scale_id] += 3
                        case _:
                            print(colored("Unacceptable 'answer'!", 'red'))
                            exit()
            # print(original_score)

            ### Standard scores
            for scale_id in range(1,9):
                cur.execute(
                    '''
                        SELECT male_u20_points, male_21_30_points, male_31_45_points, male_46_60_points,
                            female_u20_points, female_21_30_points, female_31_45_points, female_46_60_points  
                        FROM Points 
                        WHERE scale_id=? AND original_points=?
                    ''',
                    (scale_id, original_score[scale_id])
                )

            #   wasserman_points = cur.fetchall() # List of tuples e.g. [(22, 22, 15, 14, 16, 22, 17, 19)]
                wasserman_points = cur.fetchone() # Tuple e.g. (22, 22, 15, 14, 16, 22, 17, 19)
                                                    #             |     male    |     female  
                # print(type(wasserman_points))
                # print(wasserman_points)
                # print(wasserman_points[0], wasserman_points[7])

                if age < 20:
                    standard_score[scale_id] = wasserman_points[0] if sex == 'M' else wasserman_points[4]
                elif age < 30:
                    standard_score[scale_id] = wasserman_points[1] if sex == 'M' else wasserman_points[5]
                elif age < 45:
                    standard_score[scale_id] = wasserman_points[2] if sex == 'M' else wasserman_points[6]
                elif age <= 60:
                    standard_score[scale_id] = wasserman_points[4] if sex == 'M' else wasserman_points[7]
                else:
                    print(colored("Unacceptable 'age'!", 'red'))
                    exit()
                
            rows = [
                (respondent_id, original_score[0], original_score[1], original_score[2], original_score[3], original_score[4], original_score[5],  original_score[6], original_score[7], original_score[8]),
                (respondent_id, standard_score[0], standard_score[1], standard_score[2], standard_score[3], standard_score[4], standard_score[5],  standard_score[6], standard_score[7], standard_score[8])
            ]
            # print(respondent_id, original_score, standard_score)
            try:
                cur.executemany(
                    '''
                        INSERT INTO Scores (respondent_id, kind, v1, v2, v3, v4, v5, v6, v7, v8) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    rows
                )
                conn.commit()

            except Error as e:
                print(colored(e, 'red'))
