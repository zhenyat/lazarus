#! /usr/bin/env python3

###############################################################################
#   Replaces 'standard' scores with pseudo-random values according to pattern
#
#   08.12.2023  Rada Telyukova
###############################################################################
from termcolor import colored
import numpy as np
import pandas as pd
import random

import params
import db
import sample

# def main():
#     list = [0,1,2,3]
#     weights = []
#     random.choices(list, weights=None, cum_weights=None, k=1)
#     return


def get_points():
    print('===== get_points')
    df = pd.read_csv('db/csv/points.csv', header=None)

    arr = [0]*158
    for i in range(len(df)):
        arr[i] = [df.iloc[i, 1], df.iloc[i, 3], df.iloc[i, 7]]
    print(arr)


def replace_scores(pattern, data_frame):
    match pattern:
        case 'strong':
            return
        case 'weak':
            return
        case _:
            print(
                colored(f'----- Incorrect pattern: {pattern}'), 'red')
            exit()


def weights(conn, sex):
    df_male = sample.get_points(conn, 'M')
    print(df_male)
    df_female = sample.get_points(conn, 'F')
    print(df_female)
    exit()


def main():
    # min_male = [22, 24,  7, 18, 20, 27, 11, 18]
    # max_male = [79, 81, 71, 72, 67, 81, 69, 75]

    # min_score_male = np.sum(min_male)
    # max_score_male = np.sum(max_male)

    # min_female = [16, 21,  4, 15, 17, 21, 13, 18]
    # max_female = [86, 82, 76, 71, 60, 84, 69, 74]

    # min_score_female = np.sum(min_female)
    # max_score_female = np.sum(max_female)

    # get_points()
    conn = db.create_connection(params.DB_GROUND)

    school_nick = params.SCHOOL_NICKS[0]
    form = params.FORMS[0]
    model = params.MODELS[0]

    df = sample.get_data_frame(conn, model, school_nick, form)
    print(df)
    print(df.describe())


if __name__ == '__main__':
    main()
