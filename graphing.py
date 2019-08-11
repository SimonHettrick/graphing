#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import glob
import matplotlib.font_manager

from textwrap import wrap

from chart_details_lookup import plot_details
from chart_details_lookup import global_specs

DATASTORE = './data/'
STOREFILENAME = './output/'
PLOTDETAILSSTORE = './plot_details/'
DEFAULTPLOTDETAILS = 'default.csv'

mpl.rc('font',family='Serif')

# If you want to know what fonts are available, uncomment the following four lines
#flist = matplotlib.font_manager.get_fontconfig_fonts()
#names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in flist]
#names.sort()
#print(names)


def import_csv_to_df(filename, index_col):
    """
    Imports a csv file into a Pandas dataframe
    :params: get an xls file and a sheetname from that file
    :return: a df
    """

    return pd.read_csv(filename, index_col=index_col)


def export_to_csv(df, location, filename, index_write):
    """
    Exports a df to a csv file
    :params: a df and a location in which to save it
    :return: nothing, saves a csv
    """

    return df.to_csv(location + filename + '.csv', index=index_write)


def get_graph_data():
    """
    Gets all the csv files in the data dir
    :return: a list of the dir path, filename and file extension for the csvs in the data dir
    """

    graph_datafiles = glob.glob(DATASTORE + '/*.csv')

    return graph_datafiles


def get_graph_details(graph_datafiles):
    """
    Creates a dict of dfs where each df contains the plot details for a single chart. For each chart, it
    looks to see if a csv exists in which the details are stored. It either reads these if they exist, or creates
    a new df based on the DEFAULTPLOTDETAILS and then saves that as a new csv.
    :param graph_datafiles: a list of the dir path, filename and file extension of the data to plot
    :return plot_details: a dict of dfs containing all the plot details
    """

    default_details = import_csv_to_df(PLOTDETAILSSTORE + DEFAULTPLOTDETAILS,'field')

    plot_details = {}

    for current_csv in graph_datafiles:
        name_of_graph = os.path.splitext(os.path.basename(current_csv))[0]
        filename = os.path.basename(current_csv)
        try:
            # If a csv already exists for the data, go and get it
            graph_df = import_csv_to_df(DATASTORE + filename, 'field')
        except:
            # If no csv exists, create it from the default, then add the fieldname
            # as a new row to identify it
            graph_df = default_details.copy()
            d = {'field': ['filename'], 'value': [filename]}
            filename_df = pd.DataFrame(data=d)
            filename_df.set_index('field', inplace=True)
            graph_df = graph_df.append(filename_df)
            # Save plot details df as a csv
            export_to_csv(graph_df, PLOTDETAILSSTORE, name_of_graph, True)
        # Save into a dict of dfs
        plot_details[name_of_graph] = graph_df

    return plot_details


def plot_bar_matplot(df, current_chart):
    """
    Create a basic plot for each question.
    :params: a dict of dataframe, the imported plot details
    :return: A list of saved charts
    """

    # To cut down on verbosity, rename the look_up dictionary
    current_plot = plot_details[current_chart]

    percent_symbol = '%'

    # Set the labels
    labels = df.index.map(str)

    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, current_plot['x_max_len'])) for l in labels ] # Change the number to change the max number of characters                                                                            per line

    # Sometimes there are simply too many x-labels. Based on a parameter
    # from the lookup table, this removes some labels to give the others roo
    if current_plot['skip_labels'] != False:
        count = 0
        for x in range(0,len(labels)):
            if count%(current_plot['skip_labels']+1) != 0:
                labels[count]=''
            count+=1

    # This sets parameters to ensure that charts look good with one
    # set of bars or two sets of bars
    if current_plot['y2_axis'] == False:
        y_values = [current_plot['y1_axis']]

        # If we want the same colour, set to single value, otherwise use a set colormap
        if current_plot['uniform_colour']:
            colourmap = '#1677b6'
        else:
            colourmap = [plt.cm.Paired(np.arange(len(df)))]
        legend_or_not = False
    else:
        y_values = [current_plot['y1_axis'], current_plot['y2_axis']]
        colourmap = [plt.cm.Spectral(np.arange(len(df))), plt.cm.coolwarm(np.arange(len(df)))]
        legend_or_not = True
        mpl.rcParams['legend.fontsize'] = current_plot['value_font_size']


    # Now plot
    fig = df.plot(kind='bar',                      # Plot a bar chart
                y = y_values,
                legend=legend_or_not,                                   # Turn the Legend off
                width=0.75,                                     # Set bar width as 75% of space available
                figsize=(global_specs['plot_width'],global_specs['plot_height']),  # Set size of plot in inches
                color=colourmap)      # cm is colormap, 'Paired' is the set of colours I chose


    # Add labels to the bars
    if current_plot['show_values'] == True:
        count = 0
        for p in fig.patches:
            # Insert a data value label if we're not supposed to skip this particular one
            if count % (current_plot['skip_data_labels']+1) == 0:
                fig.annotate(str(int(round(p.get_height(),0))) + percent_symbol,     # Get the height of the bar and round it to a nice looking value
                 (p.get_x()+p.get_width()/2, p.get_height()),  # Locate the mid point of the bar and it's height
                 ha='center',                                  # Start plotting at the centre of the horizotal coord
                 va='center',                                  # ...and the centre of the vertical coord
                 xytext=(4, 12),                               # Change these to move the text positioning to suit
                 textcoords='offset points',                   # Dunno what this does
                 fontsize=current_plot['value_font_size'])           # Set font size
            count += 1

    if current_plot['chart_title'] != False:
        plt.title(current_plot['chart_title'], fontsize=current_plot['title_font_size'], y=1.08)  # y increases the spacing between the title
                                                                                                 # and plot content

    # Make plot scale to fit plot area
    plt.tight_layout()

    # Set x- and y-axis tick label sizes
    plt.tick_params(labelsize=current_plot['axis_font_size'])

    # Use the bespoke labels, and rotate them if necessary
    fig.set_xticklabels(labels, rotation=current_plot['x_rot'], fontsize=current_plot['axis_font_size'])

    # Turn off the spines that are not needed
    fig.spines['right'].set_visible(False)
    fig.spines['top'].set_visible(False)

    # Read in the axis classes that may be used in the following
    # if statements to set axis-related stuff
    x_axe_class = fig.axes.get_xaxis()
    y_axe_class = fig.axes.get_yaxis()

    # X axis title
    if current_plot['x_title'] == False:
        x_axe_class.label.set_visible(False)    #Turn off x axis title
    else:
        fig.set_xlabel(current_plot['x_title'])

    # Y axis title
    if current_plot['y_title'] == False:
        y_axe_class.label.set_visible(False)    # Turn off y axis title
        y_axe_class.set_visible(False)           # Turn off y-axis lines
        fig.spines['left'].set_visible(False)   # Turn off y-axis spine
    else:
        fig.set_ylabel(current_plot['y_title'])
        y_axe_class.set_visible(True) 
        fig.spines['left'].set_visible(True)

    # Make gap at bottom and left side of plot bigger for text
    plt.subplots_adjust(bottom=current_plot['bottom_size'])
    if current_plot['left_size'] != False:
        plt.subplots_adjust(left=current_plot['left_size'])

    # Save the figure
    plt.savefig(STOREFILENAME + current_chart + '.png', format = 'png', dpi = global_specs['dpi'])

    # Show the figure
#    plt.show()
    # Clear figure so that parameters can be set clean by next figure
    plt.close()

    return


def plot_line_matplot(df, current_chart):
    """
    Create a basic plot for each question. Plots of more specific interest will
    be created in a separate function, because it's impossible to automate it.
    Uses Seaborn to try and make things prettier
    :params: a dict of dataframe, the imported plot details
    :return: A list of saved charts
    """

    # Set the labels

    labels = df.index

    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, current_plot['x_max_len'])) for l in labels ] # Change the number to change the max number of characters per line

    # Set x and y ticks
    x_tick_values = range(0,len(df))
    y_tick_values = range(0,int(df[current_plot['y1_axis']].max()),20)

    if current_plot['skip_labels'] != False:
        count = 0
        for x in range(0,len(labels)):
            if count%(current_plot['skip_labels']+1) != 0:
                labels[count]=''
            count+=1
    
    fig = df[current_plot['y1_axis']].plot(kind='line',                      # Plot a bar chart
                legend=False,                                   # Turn the Legend off
                xticks = x_tick_values,
                yticks = y_tick_values,
                figsize=(global_specs['plot_width'],global_specs['plot_height']))

    fig.line.set_linewidth(8)

    if current_plot['chart_title'] != False:
        plt.title(current_plot['chart_title'], fontsize=current_plot['title_font_size'], y=1.08)  # y increases the spacing between the title and plot content

    # Make plot scale to fit plot area
    plt.tight_layout()

    # Use the bespoke labels, and rotate them if necessary
    fig.set_xticklabels(labels, rotation=current_plot['x_rot'], fontsize=current_plot['axis_font_size'])
    fig.set_yticklabels(y_tick_values, fontsize=current_plot['axis_font_size'])

    # Turn off the spines
    fig.spines['left'].set_visible(False)
    fig.spines['right'].set_visible(False)
    fig.spines['top'].set_visible(False)

    # Read in the axis classes that may be used in the following
    # if statements to set axis-related stuff
    x_axe_class = fig.axes.get_xaxis()
    y_axe_class = fig.axes.get_yaxis()

    # X axis title
    if current_plot['x_title'] == False:
        x_axe_class.label.set_visible(False)    #Turn off x axis title
    else:
        fig.set_xlabel(current_plot['x_title'])

    # Y axis title
    if current_plot['y_title'] == False:
        y_axe_class.label.set_visible(False)    #Turn off y axis title
    else:
        fig.set_ylabel(current_plot['y_title'], fontsize=current_plot['axis_font_size'])

    # Remove the y-axis stuff
    y_axe_class.set_visible(True)  

    # Make gap at bottom bigger for labels
    plt.subplots_adjust(bottom=current_plot['bottom_size'])

    # Show the figure
    plt.show()
    # Clear figure so that parameters can be set clean by next figure
    plt.clf()

    return

    
def main():
    """
    Main function to run program
    """

    # Go through a dir and create a list of paths to the csv files that exist
    graph_datafiles = get_graph_data()

    # Either read in or create parameters to use for creating a chart for
    # each csv
    plot_details = get_graph_details(graph_datafiles)

    for current_chart in plot_details:
        print('Currently working on... ' + current_chart)
        temp_df = plot_details[current_chart]
        current_details = temp_df.to_dict('dict')
        # Annoyingly, the 'to_dict" function stores the dict under a new dict with
        # only one key drawn from the 'value' field. No idea why. Anyway, this
        # removes that annoying and pointless layer of abstraction
        current_details = current_details['value']
        print(current_details)


    # Go through the list of csv files that exist, get the data and create a list of
    # the parameters used to create the graphs
    #for current_graph_data in graph_datafiles:
    #    df = import_csv_to_df(current_graph_data, 'answers')
    #    shortname = os.path.splitext(os.path.basename(current_graph_data))[0]
    #    print('Currently working on: ' + shortname)
    #    graph_details = get_graph_details(current_graph_data)


if __name__ == '__main__':
    main()
