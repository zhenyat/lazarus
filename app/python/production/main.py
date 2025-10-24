#! /usr/bin/env python3

###############################################################################
#   Main module to clean up raw data and calculate data for further analysis
#
#   05.12.2023  Rada Telyukova. HSE Lyceum
###############################################################################
from termcolor import cprint

from params import DB_PRODUCTION, SCHOOL_NICKS, FORMS
import csv

import counting
import db
import raw_data
import scores

def main():
    # print('hello from main')
    conn = db.create_connection(DB_PRODUCTION)
    # print(conn)

    # Populate 'Respondents' & 'Responses'
    for school_nick in SCHOOL_NICKS:
        # print('===== school_nick: ', school_nick)
        for form in FORMS:
            # print('===== form: ', form)
            csv_file = 'db/csv/' + school_nick + '-' + str(form) + '.csv'
            # print('===== input csv_file: ', csv_file)
            data = csv.get_raw_data(csv_file)

            raw_data.populate(conn, school_nick, form, data)

    # counting.total_records(conn, 'Respondents')
    counting.total_records(conn, 'Responses')

    scores.populate(conn)
    counting.total_records(conn, 'Scores')

    conn.close()

if __name__ == '__main__':
    main()
