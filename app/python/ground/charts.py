########################################################################
#   Draws charts for Data Frames through matplotlib
#
#   https://matplotlib.org/stable/users/explain/customizing.html
#
#   07.12.2023  Rada Telyukova
#   17.01.2023  Last update
########################################################################
import matplotlib.pyplot as plt

from params import SCALES, SHOW_PLOTS, SAVE_PLOTS, HISTOGRAMS_DIR, SCATTERS_DIR, FIGURE_SIZES, TITLE_FONT_SIZE, LEGEND_FONT_SIZE

######
#   ALL histoggrams for the Data Frame
######
def histograms(dataframe, data_frame_name, title):
    # Runtime Configuration
    plt.rcParams["figure.figsize"] = FIGURE_SIZES
    plt.rc('figure', titlesize=TITLE_FONT_SIZE)
    plt.rc('legend', fontsize=LEGEND_FONT_SIZE)

    # dataframe.hist()  # simple hist - different x-axis ranges - Not very good

    plot = dataframe.plot(kind='hist', subplots=True, title=title)   # Good one!
    for scale in range(SCALES):
        plot[scale].set_ylabel('Частота')

    if SAVE_PLOTS:
        plot_file_name = HISTOGRAMS_DIR + data_frame_name + '.pdf'
        plt.savefig(plot_file_name)
    if SHOW_PLOTS:
        plt.show()

######
#   Scatter plots of Scales for the given Sample
######
def sample_scatters(dataframe, data_frame_name):
    for first_scale in range(1, SCALES+1):
        for second_scale in range(first_scale+1, SCALES+1):
            x = 's'+str(first_scale)
            y = 's'+str(second_scale)
            dataframe.plot(
                x=x,
                y=y,
                kind='scatter',
                title=data_frame_name
            )
            # plt.xlim(0, 100)
            # plt.ylim(0, 100)
            plt.axis([0, 100, 0, 100])

            if SHOW_PLOTS:
                plt.show()
                plt.close()
            if SAVE_PLOTS:
                plot_file_name = SCATTERS_DIR + '-' + x + '-' + y + '.pdf'
                plt.savefig(plot_file_name)

######
#   Scales scatter plots of two Samples same Scales
######
def samples_scatters(df_first, df_second):
    for scale in range(SCALES):
        col = 's'+str(scale+1)
        plt.scatter(df_first[col], df_second[col], label=col)
        plt.xlim(0, 100)
        plt.ylim(0, 100)
        plt.show()
