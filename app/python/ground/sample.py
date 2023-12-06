#! /usr/bin/env python3

########################################################################
#   Returns sample of Scores for given model, school, form
#
#   06.12.2023  Rada Telyukova
########################################################################
import pandas as pd
from params import DB_GROUND, SCHOOL_NICKS, FORMS, MODELS
import db

def get(conn, model, school_nick, form):
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

def get_frame(conn, model, school_nick, form):

    sql= "SELECT s1, s2, s3, s4, s5, s6, s7, s8 FROM Scores WHERE model='"
    sql += model
    sql += "' AND respondent_id IN (SELECT id FROM Respondents WHERE form="
    sql += str(form)
    sql += " AND school_id IN (SELECT id FROM SCHOOLS WHERE nick='"
    sql += school_nick
    sql += "'));"
    # print(sql)

    data_frame = pd.read_sql_query(sql, conn)
    # print(df)
    return data_frame
