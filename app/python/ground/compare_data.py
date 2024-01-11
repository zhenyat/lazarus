#! /usr/bin/env python3

########################################################################
#   Compare two samples as dataframes
#
#   11.12.2023  Rada Telyukova
########################################################################

import pandas as pd
import matplotlib.pyplot as plt
# import time   # time.sleep(3)

from params import DB_GROUND, SHOW_PLOTS, SAVE_PLOTS 
import db
import charts

def main():
    df11 = pd.read_pickle("db/data_frames/1570-11-standard")
    print(df11.describe())
    # print(df11.columns)
    df9 = pd.read_pickle("db/data_frames/1570-9-standard")
    print(df9.describe())

    charts.histograms(df11, '1570-11-standard')
    charts.histograms(df9, '1570-9-standard')
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
            plot_file_name = 'images/scatters/' + '-' + x + '-' + y + '.pdf'
            plt.savefig(plot_file_name)
        plt.close()

if __name__ == '__main__':
    main()
