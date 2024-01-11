###################################################################
#   Monte-Carlo pseudo-random generation of values
#
#   09.12.2023  Rada
###################################################################
from termcolor import colored
import random

from params import UNIFORM_RANDOM_MODE, ANSWERS, CONSTRUCTIVE_WEIGHTS, NON_CONSTRUCTIVE_WEIGHTS, REL_CONSTRUCTIVE_WEIGHTS

def generate_answer(cur, school_nick, form, questionnaire_id):
   
    if UNIFORM_RANDOM_MODE:
        return random.choice(ANSWERS)
    else:
        cur.execute("SELECT scale_id FROM Questionnaire WHERE id=?", (questionnaire_id,))
        scale_id, = cur.fetchone()

        if school_nick == '1570' and form == 9:
            answers = random.choices(ANSWERS, weights=NON_CONSTRUCTIVE_WEIGHTS[scale_id], k=1)
        elif school_nick == '1570' and form == 11:
            answers = random.choices(ANSWERS, weights=REL_CONSTRUCTIVE_WEIGHTS[scale_id], k=1)
        elif school_nick == 'lyceum' and form == 9:
            answers = random.choices(ANSWERS, weights=NON_CONSTRUCTIVE_WEIGHTS[scale_id], k=1)
        elif school_nick == 'lyceum' and form == 11:
            answers = random.choices(ANSWERS, weights=CONSTRUCTIVE_WEIGHTS[scale_id], k=1)
        else:
            print(colored(f'===== Responses: incorrect school_nick, form: {school_nick},  {form}', 'red'))
            exit()

    return answers[0]   # First and the only element in the list
