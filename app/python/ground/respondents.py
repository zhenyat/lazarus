####### Faked data for Respondents

from termcolor import colored
from faker import Faker

from params import SCHOOL_NICKS, FORMS, FAKED_RESPONDENTS

def populate_with_fakes(conn):
    faker = Faker('ru_RU')

    with conn:

        for school_nick in SCHOOL_NICKS:    # School cycle
            cur = conn.cursor()
            cur.execute("SELECT id FROM Schools WHERE nick=?", (school_nick,))
            school_id, = cur.fetchone()

            for form in FORMS:                  # Form cycle
                age = 15 if form == 9 else 17
                for respondent_id in range(FAKED_RESPONDENTS):
                    p = faker.profile()
                    sex = p['sex']

                    cur.execute(
                        'INSERT INTO Respondents (school_id, sex, age, form) VALUES (?, ?, ?, ?)',
                        (school_id, sex, age, form)
                    )
                    conn.commit()

    cur.execute("SELECT count(*) FROM Respondents")
    count, = cur.fetchone()
    print(colored(f'===== Table "Respondents": {count} records  total', 'green'))
