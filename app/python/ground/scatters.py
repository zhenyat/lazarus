#! /usr/bin/env python3

import pandas as pd
from params import SCHOOL_NICKS, FORMS, DATA_FRAMES_DIR
import charts
def main():
    model = 'standard'
    # for school_nick in SCHOOL_NICKS:
    #     for form in FORMS:

    ### 1: Lyceum 9
    # df_first_title = "L-9"
    df_first_name = '-'.join([SCHOOL_NICKS[0], str(FORMS[0]), model])
    print("--- ",DATA_FRAMES_DIR+df_first_name)
    df_first = pd.read_pickle(DATA_FRAMES_DIR + df_first_name)
    print(df_first)
    
    # 2: Lyceum 11
    # df_second_title = "L-11"
    df_second_name = '-'.join([SCHOOL_NICKS[0], str(FORMS[1]), model])
    print("--- ", DATA_FRAMES_DIR+df_second_name)
    df_second = pd.read_pickle(DATA_FRAMES_DIR + df_second_name)
    print(df_second)

    charts.samples_scatters(df_first, df_second)


if __name__ == '__main__':
    main()
