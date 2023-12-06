#! /usr/bin/env python3

########################################################################
#   Analyzes Scores sample by sample
#
#   06.12.2023  Rada Telyukova
########################################################################
import matplotlib.pyplot as plt

from params import DB_GROUND, SCHOOL_NICKS, FORMS, MODELS
import db
import sample

def main():
    conn = db.create_connection(DB_GROUND)

    for model in MODELS:
        if model == 'original': 
            continue
        for school_nick in SCHOOL_NICKS:
            for form in FORMS:
                # data = sample.get(conn, model, school_nick, form)
                df = sample.get_frame(conn, model, school_nick, form)

                df_name = model + '-' + school_nick + '-' + str(form)
               
                print("\n===== DataFrame: ", df_name)
                # print("-----DataFrame head():\n", df.head())
                print("\t****  mean  ± std dev: ")
                print("\ts1:   %5.2f ± %5.2f" % (df['s1'].mean(), df['s1'].std()))
                print("\ts2:   %5.2f ± %5.2f" % (df['s2'].mean(), df['s2'].std()))
                print("\ts3:   %5.2f ± %5.2f" % (df['s3'].mean(), df['s3'].std()))
                print("\ts4:   %5.2f ± %5.2f" % (df['s4'].mean(), df['s4'].std()))
                print("\ts5:   %5.2f ± %5.2f" % (df['s5'].mean(), df['s5'].std()))
                print("\ts6:   %5.2f ± %5.2f" % (df['s6'].mean(), df['s6'].std()))
                print("\ts7:   %5.2f ± %5.2f" % (df['s7'].mean(), df['s7'].std()))
                print("\ts8:   %5.2f ± %5.2f" % (df['s8'].mean(), df['s8'].std()))
                
                df.hist()
                file_name = 'images/' + df_name + '.pdf'

                plt.savefig(file_name)

    conn.close()

if __name__ == '__main__':
    main()
