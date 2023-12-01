#! /usr/bin/env python3

from params import DB_PRODUCTION, SCHOOL_NICKS, FORMS
import db
import csv
from termcolor import cprint
import raw_data
import scores


def main():
    # print('hello from main')
    conn = db.create_connection(DB_PRODUCTION)
    # print(conn)

    for school_nick in SCHOOL_NICKS:
        # print(school_nick)
        for form in FORMS:
            # print(form)
            csv_file = 'db/csv/' + school_nick + '-' + str(form) + '.csv'
            # print(csv_file)
            data = csv.get_raw_data(csv_file)

            raw_data.populate(conn, school_nick, form, data)

    scores.populate(conn)
    conn.close()
    # cprint('==== Well Done!', 'green')

if __name__ == '__main__':
    main()
