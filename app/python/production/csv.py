################################################################
#   Gets raw data from a csv file specified by the name 'csv_file'
#
#   Returns raw data string
#
#   30.11.2023  Rada Telyukova
#################################################################
from termcolor import cprint

def get_raw_data(csv_file):
 
    try:
        raw_data = open(csv_file, 'r')

    except IOError as e:
        cprint(('csv.py: I/O error({0}): {1}').format(e.errno, e.strerror), 'red')
        exit()

    return raw_data
