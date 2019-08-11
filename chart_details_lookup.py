#!/usr/bin/env python
# encoding: utf-8

'''
global_specs sets up some global variables for the plots
'''

global_specs = {
    'plot_width': 10,
    'plot_height': 7.2,
    'dpi': 300,
    'font_name': 'Serif'
    }

'''
plot_details is a dictionary of lists. The lists are of the form:
 0. filename: the file used to draw graph
 1. Plot type: bar or line
 2. y1_axis: first column to plot
 3. y2_axis: second column to plot (or False, if none)
 4. x_title: title for x axis, or use False if no title to be shown
 5. x_rot: rotation of x-axis tick labels (0 is horizontal)
 6. x_man_length: max length of x-axis tick labels before they start a new line
 7. y_title: title for y axis, or use False if no title to be shown
 8. chart_title: title of chart, or use False if no title
 9. show_values: whether to show data labels on bars (True/False)
10. skip_labels: how many x labels to remove after each one shown (or False to keep all)
11. skip_data_labels: how many x data value labels to remove after each one shown (or False to keep all)
12. bottom_size: fraction of chart dedicated to x-axis tick labels (0-1)
13. title_font_size: size of title font
14. axis_font_size: size of axis fonts
15. value_font_size: size of value label font
16. uniform_colour: whether to use a uniform colour for bars, default False
'''


plot_details = {

    'default_settings': {
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': False,
        'show_values': False,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 12,
        'axis_font_size': 16,
        'value_font_size': 16,
        'uniform_colour': False
    },

    'faculty': {
             'plot_type': 'bar',
             'y1_axis': 'percentage',
             'y2_axis': False,
             'x_title': False,
             'x_rot': 0,
             'x_max_len': 15,
             'y_title': False,
             'chart_title': 'In which faculty are you based?',
             'show_values': True,
             'skip_labels': False,
             'skip_data_labels': False,
             'bottom_size': 0.15,
             'left_size' : 0.08,
             'title_font_size': 18,
             'axis_font_size': 12,
             'value_font_size': 15,
             'uniform_colour': False
             },

    'use_software': {
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Do you use research software?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 12,
        'value_font_size': 15,
        'uniform_colour': False
    },

    'version_control': {
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'How confident are you with version control?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    }

    }
    
    
    
    
    
