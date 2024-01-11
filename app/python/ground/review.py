#! /usr/bin/env python3

########################################################################
#   Reviews Scores sample by sample
#
#   06.12.2023  Rada Telyukova
########################################################################

from params import DB_GROUND, SCHOOL_NICKS, FORMS, MODELS, DATA_FRAMES_DIR
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
                # sample.show_data(data, data_set_name)

                # Data frame
                df = sample.get_data_frame(conn, model, school_nick, form)
                sample.show_statistics(df, df_name)
                print(df.describe())
                # print(df.corr())

                df = df.rename(
                    columns={
                        's1': 'Конфронтационный копинг',
                        's2': 'Дистанцирование',
                        's3': 'Самоконтроль',
                        's4': 'Поиск социальной поддержки',
                        's5': 'Принятие ответственности',
                        's6': 'Бегство-избегание',
                        's7': 'Планирование решения проблемы',
                        's8': 'Положительная переоценка'
                    }
                )

                file_path = DATA_FRAMES_DIR + df_name
                df.to_pickle(file_path)

                # print(np.asarray(df))
                data_frames[df_name] = df
                # print(df[0])

                cur = conn.cursor()
                cur.execute("SELECT title FROM Schools WHERE nick=?", (school_nick,))
                title, = cur.fetchone()
                title = title + ', ' + str(form) + '-й класс'

                charts.histograms(df, df_name, title)
                # charts.sample_scatters(df, df_name)

    conn.close()


if __name__ == '__main__':
    main()
