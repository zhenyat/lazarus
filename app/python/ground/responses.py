####### Faked data for Responses
from termcolor import colored

import monte_carlo as mc

def populate_with_fakes(conn):

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

        for respondent_id in respondent_ids:
            cur.execute("SELECT school_id, form from Respondents WHERE id=?", (respondent_id,))
            (school_id, form) = cur.fetchone()

            cur.execute("SELECT nick from Schools WHERE id=?", (school_id,))
            school_nick, = cur.fetchone()

            for questionnaire_id in questionnaire_ids:
                answer = mc.generate_answer(cur, school_nick, form, questionnaire_id)

                # Save records into Responses
                cur.execute(
                    'INSERT INTO Responses (respondent_id, questionnaire_id, answer) VALUES (?, ?, ?)',
                    (respondent_id, questionnaire_id, answer)
                )
                conn.commit()

    cur.execute("SELECT count(*) FROM Responses")
    count, = cur.fetchone()   # From tuple (400,)
    print(colored(f'===== Table "Responses": {count} records  total', 'green'))
    