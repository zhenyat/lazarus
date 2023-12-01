#! /usr/bin/env python3

from params import DB_PRODUCTION, SCHOOLS, FORMS
import db
import csv
from termcolor import cprint
import process_data


def main():
    print('hello from main')
    conn = db.create_connection(DB_PRODUCTION)
    print(conn)

    for school in SCHOOLS:
        print(school)
        for form in FORMS:
            print(form)
            csv_file = 'db/csv/' + school + '-' + str(form) + '.csv'
            print(csv_file)
            raw_data = csv.get_raw_data(csv_file)

            process_data.populate(conn, school, form, raw_data)

    conn.close()
    cprint('==== Well Done!', 'green')

if __name__ == '__main__':
    main()
