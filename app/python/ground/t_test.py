#! /usr/bin/env python3

########################################################################
#   T-Test of two independent samples
#
#   https://www.statology.org/pandas-t-test/
#   https://coffee-web.ru/blog/executing-a-t-test-in-python/
#
#   14.01.2024  Rada Telyukova
########################################################################
import pandas as pd
from scipy.stats import ttest_ind

from params import DB_GROUND, SCHOOL_NICKS, FORMS, DATA_FRAMES_DIR, SCALE_NAMES, ALPHA, TITLES
import db

def report(df_first_title, df_first, df_second_title, df_second, results):
    print(f"\nШкала копинга\t\t\t {df_first_title}\t{df_second_title}\t\t\tt-Test")
    print("\t\t\t\t    Сред.зн\t  Сред.зн\tstatistic\tp-value\t\tВердикт")
    print("-"*120)

    i = 0
    for col in df_first.columns:
        verdict = "Отклонить нуль-гипотезу" if results.pvalue[i] <= ALPHA else "Не удалось отклонить H0"
        pvalue_formatted = f"{results.pvalue[i]:8.4f}" if results.pvalue[i] >= 0.1 * ALPHA else " ~0.0   " #f"{results.pvalue[i]:8.2e}"
        print(SCALE_NAMES[col],
            f"{df_first[col].mean():5.2f} ± {df_first[col].std():4.2f}\t{df_second[col].mean():5.2f} ± {df_second[col].std():5.2f}",
            f"\t{results.statistic[i]:8.4f}\t{pvalue_formatted}",
            f"\t{verdict}"
        )
        i += 1
    return


def testing(df_first, df_second):
    results_by_scale = []
    for col in df_first.columns:
        group_first = df_first[col]
        group_second = df_second[col]
        results_by_scale.append(
            ttest_ind(group_first, group_second, equal_var=True))

    return results_by_scale

#   Generates cyrillic short titles of schools & forms for output tables
def set_titles():
    titles = []
    conn = db.create_connection(DB_GROUND)
    cur =conn.cursor()
    cur.execute("SELECT short_title FROM Schools")
    short_titles = cur.fetchall()

    for short_title in short_titles:
        for form in (9,11):
            titles.append(short_title[0]+' '+str(form)+' кл')

    return titles


def main():
    titles = set_titles()

    model = 'standard'
    results = {}

    # Results matrix
    #              L-9   L-11   1570-9   1570-11
    #   L-9         x    [0,1]   [0,2]    [0,3]
    #   L-11        x     x      [1,2]    [1,3]
    #   1570-9      x     x       x       [2,3],
    #   1570-11     x     x       x         x

    ### 1: Lyceum 9
    df_first_title = titles[0]
    df_first_name = '-'.join([SCHOOL_NICKS[0], str(FORMS[0]), model])
    df_first = pd.read_pickle(DATA_FRAMES_DIR + df_first_name)
    
    # 2: Lyceum 11
    df_second_title = titles[1]
    df_second_name = '-'.join([SCHOOL_NICKS[0], str(FORMS[1]), model])
    df_second = pd.read_pickle(DATA_FRAMES_DIR + df_second_name)
    results[0, 1] = ttest_ind(df_first, df_second, equal_var=True)
    report(df_first_title, df_first, df_second_title, df_second, results[0, 1])
 
    # 2: 1570 9
    df_second_title = titles[2]
    df_second_name = '-'.join([SCHOOL_NICKS[1], str(FORMS[0]), model])
    df_second = pd.read_pickle(DATA_FRAMES_DIR + df_second_name)
    results[0, 2] = ttest_ind(df_first, df_second, equal_var=True)
    report(df_first_title, df_first, df_second_title, df_second, results[0, 2])
 
    # 2: 1570 11
    df_second_title = titles[3]
    df_second_name = '-'.join([SCHOOL_NICKS[1], str(FORMS[1]), model])
    df_second = pd.read_pickle(DATA_FRAMES_DIR + df_second_name)
    results[0, 3] = ttest_ind(df_first, df_second, equal_var=True)
    report(df_first_title, df_first, df_second_title, df_second, results[0, 3])

    ### 1: Lyceum 11
    df_first_title = titles[1]
    df_first_name = '-'.join([SCHOOL_NICKS[0], str(FORMS[1]), model])
    df_first = pd.read_pickle(DATA_FRAMES_DIR + df_first_name)

    # 2: 1570 9
    df_second_title = titles[2]
    df_second_name = '-'.join([SCHOOL_NICKS[1], str(FORMS[0]), model])
    df_second = pd.read_pickle(DATA_FRAMES_DIR + df_second_name)
    results[1, 2] = ttest_ind(df_first, df_second, equal_var=True)
    report(df_first_title, df_first, df_second_title, df_second, results[1, 2])

    # 2: 1570 11
    df_second_title = titles[3]
    df_second_name = '-'.join([SCHOOL_NICKS[1], str(FORMS[1]), model])
    df_second = pd.read_pickle(DATA_FRAMES_DIR + df_second_name)
    results[1, 3] = ttest_ind(df_first, df_second, equal_var=True)
    report(df_first_title, df_first, df_second_title, df_second, results[1, 3])

    ### 1: 1570 9
    df_first_title = titles[2]
    df_first_name = '-'.join([SCHOOL_NICKS[1], str(FORMS[0]), model])
    df_first = pd.read_pickle(DATA_FRAMES_DIR + df_first_name)

    # 2: 1570 11
    df_second_title = titles[3]
    df_second_name = '-'.join([SCHOOL_NICKS[1], str(FORMS[1]), model])
    df_second = pd.read_pickle(DATA_FRAMES_DIR + df_second_name)
    results[2, 3] = ttest_ind(df_first, df_second, equal_var=True)
    report(df_first_title, df_first, df_second_title, df_second, results[2, 3])


if __name__ == '__main__':
    main()
