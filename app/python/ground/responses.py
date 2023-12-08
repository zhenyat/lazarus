####### Faked data for Responses

from termcolor import colored
import random

def populate_with_fakes(conn):
    answers = ['never', 'rarely', 'sometimes', 'regularly']

    with conn:
        cur = conn.cursor()

        cur.execute("SELECT id from Respondents ORDER BY id")
        # List of tuples: [(1,), (2,), (3,), (4,), ... (199,), (200,)]
        respondent_ids = []
        for id, in cur:
            respondent_ids.append(id)   # [1,2,3,4 ... 199,200]

        cur.execute('SELECT id FROM Questionnaire ORDER BY id')
        questionnaire_ids = []
        for id, in cur:
            questionnaire_ids.append(id)    # [1,2 ... 50]

        # Save records into Responses
        for respondent_id in respondent_ids:
            for questionnaire_id in questionnaire_ids:

                answer = random.choice(answers)

                cur.execute(
                    'INSERT INTO Responses (respondent_id, questionnaire_id, answer) VALUES (?, ?, ?)',
                    (respondent_id, questionnaire_id, answer)
                )
                conn.commit()

    cur.execute("SELECT count(*) FROM Responses")
    count, = cur.fetchone()   # From tuple (400,)
    print(colored(f'===== Table "Responses": {count} records  total', 'green'))
    