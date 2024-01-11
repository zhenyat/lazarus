########################################################################
#   Returns draws charts for Data Frames through matplotlib
#
#   07.12.2023  Rada Telyukova
########################################################################
import matplotlib.pyplot as plt

from params import SCALES, SHOW_PLOTS, SAVE_PLOTS

######
#   ALL histoggrams for the Data Frame
######
def histograms(dataframe, data_frame_name):
    dataframe.hist()

    plot_file_name = 'images/histograms/' + data_frame_name + '.pdf'
    if SAVE_PLOTS:
        plt.savefig(plot_file_name)
    if SHOW_PLOTS:
        plt.show()

######
#   Scatter plots of Scales of the given Sample
######
def sample_scatters(dataframe, data_frame_name):
    for first_scale in range(1,SCALES+1):
        for second_scale in range(first_scale+1, SCALES+1):
            x = 's'+str(first_scale)
            y='s'+str(second_scale)
            dataframe.plot(
                x=x, 
                y=y, 
                kind='scatter',
                title=data_frame_name
                )
            if SHOW_PLOTS:
                plt.show()
                plt.close()
            if SAVE_PLOTS:
                plot_file_name = 'images/scatters/' + '-' + x + '-' + y + '.pdf'
                plt.savefig(plot_file_name)

######
#   Scales scatter plots of two Samples
######
def samples_scatters(dataframe_first, data_frame_first__name, dataframe_second, data_frame_second__name,):
    print()