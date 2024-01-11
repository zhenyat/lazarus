#! /usr/bin/env python3

########################################################################
#   Returns sample of Scores for given model, school, form
#   get()         - with sqlite3 module (just for reference)
#   get_frame()   - with Pandas module
#
#   06.12.2023  Rada Telyukova
########################################################################
import pandas as pd
import numpy as np

from params import DB_GROUND, SCHOOL_NICKS, FORMS, MODELS

#####
#   Gets data sample via SQL request
#####
def get_data(conn, model, school_nick, form):
    cur = conn.cursor()

    cur.execute(
        '''
            SELECT s1, s2, s3, s4, s5, s6, s7, s8 FROM Scores 
            WHERE model=? AND respondent_id IN 
                (SELECT id FROM Respondents 
                    WHERE form=? AND school_id IN 
                    (SELECT id FROM SCHOOLS WHERE nick=?));
        ''',
        (model, form, school_nick)
    )

    sample = cur.fetchall()  # List of tuples
    return sample

#####
#   Gets data sample via Pandas method
#   Retruns DataFrame
#####
def get_data_frame(conn, model, school_nick, form):

    sql= "SELECT s1, s2, s3, s4, s5, s6, s7, s8 FROM Scores WHERE model='"
    sql += model
    sql += "' AND respondent_id IN (SELECT id FROM Respondents WHERE form="
    sql += str(form)
    sql += " AND school_id IN (SELECT id FROM SCHOOLS WHERE nick='"
    sql += school_nick
    sql += "'));"
    # print(sql)

    data_frame = pd.read_sql_query(sql, conn)
    # print(data_frame)
    return data_frame

#####
#   Gets Points for Monte-Carlo calcs
#####
def get_points(conn, sex):
    if sex == 'M':
        sql = "SELECT scale_id, male_u20_points from Points ORDER BY id"
    else:
        sql = "SELECT scale_id, female_u20_points from Points ORDER BY id"

    data_frame = pd.read_sql_query(sql, conn)
    return data_frame

#####
#   Prints SELECT data - TBD
#####
def show_data(data, data_set_name):
    for scales in data:
        print("\n===== Data: ", data_set_name)
        # for scale in scales:

#####
#   Prints Data Frame data
#####
def show_statistics(df, data_set_name):
    print("\n===== DataFrame: ", data_set_name)
    # print("-----DataFrame head():\n", df.head())
    print("\t     (mean  ± std dev)")
    print("\ts1:   %5.2f ± %5.2f" % (df['s1'].mean(), df['s1'].std()))
    print("\ts2:   %5.2f ± %5.2f" % (df['s2'].mean(), df['s2'].std()))
    print("\ts3:   %5.2f ± %5.2f" % (df['s3'].mean(), df['s3'].std()))
    print("\ts4:   %5.2f ± %5.2f" % (df['s4'].mean(), df['s4'].std()))
    print("\ts5:   %5.2f ± %5.2f" % (df['s5'].mean(), df['s5'].std()))
    print("\ts6:   %5.2f ± %5.2f" % (df['s6'].mean(), df['s6'].std()))
    print("\ts7:   %5.2f ± %5.2f" % (df['s7'].mean(), df['s7'].std()))
    print("\ts8:   %5.2f ± %5.2f" % (df['s8'].mean(), df['s8'].std()))
