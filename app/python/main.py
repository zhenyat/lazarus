#! /usr/bin/env python3

import settings
import db
import csv
from termcolor import cprint
import process_data

def main():
    print('hello from main')
    conn = db.create_connection(settings.db_production)
    print(conn)

    for school in settings.schools:
        print(school)
        for form in settings.forms:
            print(form)
            csv_file = 'db/csv/' + school + '-' + str(form) + '.csv'
            print(csv_file)
            raw_data = csv.get_raw_data(csv_file)

            process_data.populate(conn, school, form, raw_data)

            # raw_data.closed() 

    conn.close()
    cprint('==== Well Done!', 'green')

if __name__ == '__main__':
    main()
