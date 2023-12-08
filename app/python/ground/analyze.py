#! /usr/bin/env python3

########################################################################
#   Analyzes Scores sample by sample
#
#   06.12.2023  Rada Telyukova
########################################################################

from params import DB_GROUND, SCHOOL_NICKS, FORMS, MODELS
import db
import sample
import charts

def main():
    conn = db.create_connection(DB_GROUND)

    data_frame_collection = {}

    for school_nick in SCHOOL_NICKS:
        for form in FORMS:
            for model in MODELS:
                data_frame_name = school_nick + '-' + str(form) + '-' + model

                # List of tuples (just for reference)
                # data = sample.get_data(conn, model, school_nick, form)
                # sample.show_data(data, data_set_name)

                # Data frame
                df = sample.get_data_frame(conn, model, school_nick, form)
                sample.get_statistics(df, data_frame_name)
                print(df.describe())
                # print(np.asarray(df))
                # data_frame_collection[data_frame_name] = df
                # print(df[0])
                # charts.histograms(df, data_frame_name)
                charts.sample_scatters(df, data_frame_name)

    conn.close()

if __name__ == '__main__':
    main()
