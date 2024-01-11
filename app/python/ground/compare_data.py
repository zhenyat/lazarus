#! /usr/bin/env python3

########################################################################
#   Compares two samples as dataframes
#
#   11.12.2023  Rada Telyukova
########################################################################

import pandas as pd
import matplotlib.pyplot as plt
# import time   # time.sleep(3)

from params import DB_GROUND, SHOW_PLOTS, SAVE_PLOTS, DATA_FRAMES_DIR, SCATTERS_DIR
import db
import charts

def main():
    first_frame_name = "1570-9-standard"
    second_frame_name = "lyceum-11-standard"
    first_frame = pd.read_pickle(DATA_FRAMES_DIR + first_frame_name)
    print(f"\n{first_frame_name}")
    print(first_frame.describe())
    
    second_frame = pd.read_pickle(DATA_FRAMES_DIR + second_frame_name)
    print(f"\n{second_frame_name}")
    print(second_frame.describe())
    print(second_frame.columns)

    charts.histograms(first_frame, first_frame_name)
    charts.histograms(second_frame, second_frame_name)
    
    exit()
    conn = db.create_connection(DB_GROUND)
    sql = "SELECT id, rus FROM Scales ORDER BY id"
    scales = pd.read_sql(sql, conn)
    # print(scales)
    # print(scales['rus'][1])
 

    
    id = 0 
    for scale in df11.columns:
        id += 1
        plt.scatter(df11[scale], df9[scale], label=scales['rus'][id])
        plt.legend(loc='best', fontsize=16)
        plt.title('1570 standard')
        plt.xlabel('11th Form')
        plt.ylabel('9th Form')

        if SHOW_PLOTS:
            plt.show()
        if SAVE_PLOTS:
            plot_file_name = SCATTERS_DIR + '-' + x + '-' + y + '.pdf'
            plt.savefig(plot_file_name)
        plt.close()

if __name__ == '__main__':
    main()
