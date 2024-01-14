#! /usr/bin/env python3

import pandas as pd
from scipy.stats import ttest_ind
from params import SCHOOL_NICKS, FORMS, MODELS, DATA_FRAMES_DIR

def main():
    model = MODELS[0]
    indices = []
    df_first_name = '-'.join([SCHOOL_NICKS[0], str(FORMS[0]), model])
    df_first = pd.read_pickle(DATA_FRAMES_DIR + df_first_name)
    # my_list = list(df_first)
    # print(my_list)
    # print(df_first.head())
    for col in df_first.columns:
        print(col)
    
    # indices = df_first.index.tolist()
    # print(indices)
    exit()
    df_second_name = '-'.join([SCHOOL_NICKS[0], str(FORMS[1]), model])
    df_second = pd.read_pickle(DATA_FRAMES_DIR + df_second_name)
    print(ttest_ind(df_first, df_second, equal_var=True))


if __name__ == '__main__':
    main()