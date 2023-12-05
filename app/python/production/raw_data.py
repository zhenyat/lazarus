########################################################################
#   Cleans and populates raw data to DB tables Respondents & Responses
#
#   30.11.2023  Rada Telyukova
########################################################################
from termcolor import cprint, colored

from params import AGE_MIN, AGE_MAX, NUMBER_OF_QUESTIONS

def populate(conn, school_nick, form, data):

    # Handle raw data row by row
    for row in data:
        # respondent_id += 1
        # row string into Array
        cells = []
        cells = row.strip().split(',')
        if len(cells) != NUMBER_OF_QUESTIONS:
            cprint(('process_data.py: Incorrect number of elements: {0}').format(len(cells)), 'red')
            exit()

        sex = 'M' if (cells.pop(0) == 'Мужской') else 'F'  # Translate sex

        age = int(cells.pop(0))
        # Clean raw data by age
        if age < AGE_MIN or age > AGE_MAX:
            cprint('Age {0} is not allowed'.format(age), 'red')
            continue
        # print(sex, age)

        cur = conn.cursor()
        cur.execute('SELECT id FROM Schools WHERE nick=?', (school_nick, ))
        school_id = cur.fetchone()[0]   # First element of tuple
        # print(school_id)

        # Populate data into Respondent
        cur.execute('''
                INSERT INTO Respondents (school_id, sex, age, form) 
                VALUES (?, ?, ?, ?)
            ''',
                    (school_id, sex, age, form)
                    )
        conn.commit()
        current_respondent_id = cur.lastrowid   # Current (last) Respondent

        # Populate data into 'Responses'
        for i in range(len(cells)):
            questionnaire_id = i + 1   # i starts from 0; questionnaire_id - from 1
            match cells.pop(0):
                case 'никогда':
                    answer = 'never'
                case 'редко':
                    answer = 'rarely'
                case 'иногда':
                    answer = 'sometimes'
                case 'часто':
                    answer = 'regularly'
                case _:
                    print(colored(f'----- Incorrect answer: {answer}'), 'red')
                    exit()
            cur.execute('INSERT INTO Responses (respondent_id, questionnaire_id, answer) VALUES (?, ?, ?)',
                        (current_respondent_id, questionnaire_id, answer)
                        )
            conn.commit()
