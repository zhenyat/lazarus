#! /usr/bin/env python3

########################################################################
#   Reviews Scores sample by sample: data & charts
#
#   06.12.2023  Rada Telyukova
#   16.01.2024  Last update
########################################################################

from params import DB_GROUND, SCHOOL_NICKS, FORMS, MODELS, DATA_FRAMES_DIR, SCALES, SCALE_NAMES_LOCALIZED
import db
import sample
import charts

def main():
    conn = db.create_connection(DB_GROUND)

    data_frames = {}

    for school_nick in SCHOOL_NICKS:
        for form in FORMS:
            for model in MODELS:
                # df_name = school_nick + '-' + str(form) + '-' + model
                df_name = '-'.join([school_nick, str(form), model])

                # List of tuples (just for reference)
                # data = sample.get_data(conn, model, school_nick, form)
                # sample.show_data(data, df_name)

                # Data frame
                df = sample.get_data_frame(conn, model, school_nick, form)
                sample.show_statistics(df, df_name)
                print("\n",df.describe())
                # print(df.corr())

                file_path = DATA_FRAMES_DIR + df_name
                df.to_pickle(file_path)

                # print(np.asarray(df))
                data_frames[df_name] = df
                # print(df[0])

                cur = conn.cursor()
                cur.execute("SELECT title FROM Schools WHERE nick=?", (school_nick,))
                title, = cur.fetchone()
                title = title + ', ' + str(form) + '-й класс'

                df_localized = df.copy()    # Data frame copy for localized charts

                df_localized = df_localized.rename(
                    columns={
                      # 's1': SCALE_NAMES_LOCALIZED[0] + "\n    mean = %5.2f ± %3.2f" % (df['s1'].mean(), df['s1'].std()),
                        's1': f"{SCALE_NAMES_LOCALIZED[0]}\n    сред.зн. = {df['s1'].mean():5.2f} ± {df['s1'].std():3.2f}",
                        's2': f"{SCALE_NAMES_LOCALIZED[0]}\n    mean = {df['s2'].mean():5.2f} ± {df['s2'].std():3.2f}",
                        's3': f"{SCALE_NAMES_LOCALIZED[0]}\n    mean = {df['s3'].mean():5.2f} ± {df['s3'].std():3.2f}",
                        's4': f"{SCALE_NAMES_LOCALIZED[0]}\n    mean = {df['s4'].mean():5.2f} ± {df['s4'].std():3.2f}",
                        's5': f"{SCALE_NAMES_LOCALIZED[0]}\n    mean = {df['s5'].mean():5.2f} ± {df['s5'].std():3.2f}",
                        's6': f"{SCALE_NAMES_LOCALIZED[0]}\n    mean = {df['s6'].mean():5.2f} ± {df['s6'].std():3.2f}",
                        's7': f"{SCALE_NAMES_LOCALIZED[0]}\n    mean = {df['s7'].mean():5.2f} ± {df['s7'].std():3.2f}",
                        's8': f"{SCALE_NAMES_LOCALIZED[0]}\n    mean = {df['s8'].mean():5.2f} ± {df['s8'].std():3.2f}"
                    }
                )

                charts.histograms(df_localized, df_name, title)
                # charts.sample_scatters(df_localized, df_name)

    conn.close()

if __name__ == '__main__':
    main()
