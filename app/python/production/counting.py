########################################################################
#   Counts number of records in the DB table
#
#   05.12.2023  Rada Telyukova
########################################################################
from termcolor import colored

def total_records(conn, table_name):
    cur = conn.cursor()

    sql = "SELECT count(*) FROM " + table_name + ";"
    cur.execute(sql)
    count = cur.fetchone()
    print(colored(f'===== Table "{table_name}": {count[0]} records  total', 'green'))
