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
    'faculty': {
             'filename': 'faculty.csv',
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
    'faculty_normalised': {
        'filename': 'faculty_normalised.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Respondents as percentage of all staff in faculty?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.15,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 12,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'funders': {
             'filename': 'funders.csv',
             'plot_type': 'bar',
             'y1_axis': 'percentage',
             'y2_axis': False,
             'x_title': False,
             'x_rot': 90,
             'x_max_len': 10,
             'y_title': False,
             'chart_title': 'Which of the following fund your research?',
             'show_values': True,
             'skip_labels': False,
             'skip_data_labels': False,
             'bottom_size': 0.2,
             'left_size' : 0.08,
             'title_font_size': 18,
             'axis_font_size': 15,
             'value_font_size': 15,
             'uniform_colour': False
             },
    'job_title': {
        'filename': 'job_title.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 13,
        'y_title': False,
        'chart_title': 'What is your job title?',
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
    'use_software': {
        'filename': 'use_software.csv',
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

    'faculties_use_software': {
        'filename': 'faculties_use_software.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Percentage of respondents using software',
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
    'importance_software': {
        'filename': 'importance_software.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'How important is research software to your work?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'develop_own_code': {
        'filename': 'develop_own_code.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Have you developed your own research software?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'job_title_develop_own_code': {
        'filename': 'job_title_develop_own_code.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 9,
        'y_title': False,
        'chart_title': 'Respondents who develop own code',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.11,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'faculties_develop_own_code': {
        'filename': 'faculties_develop_own_code.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 13,
        'y_title': False,
        'chart_title': 'Percentage of respondents developing software.',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.15,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'faculties_training': {
        'filename': 'faculties_training.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 13,
        'y_title': False,
        'chart_title': 'Percentage of respondents reliably trained.',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.15,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'development_expertise': {
        'filename': 'development_expertise.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'How do you rate your software development expertise?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'training': {
        'filename': 'training.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Received sufficient training to develop reliable software?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'want_to_commercialise': {
        'filename': 'want_to_commercialise.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Would you be interested in commercialising your research software?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'ready_to_share': {
        'filename': 'ready_to_share.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Do you feel that your software is ready to be shared?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'hpc_use': {
        'filename': 'hpc_use.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Have you used IRIDIS?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.15,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 12,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'version_control': {
        'filename': 'version_control.csv',
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
    },
    'continuous_integration': {
        'filename': 'continuous_integration.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'How confident are you with continuous integration?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'unit_testing': {
        'filename': 'unit_testing.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'How confident are you with unit testing?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'current_support': {
        'filename': 'current_support.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'How do you rate the University\'s current support for software development?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 15,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'hired_developer': {
        'filename': 'hired_developer.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 15,
        'y_title': False,
        'chart_title': 'Have you ever hired someone to develop software?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.1,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    },
    'funds_for_development': {
        'filename': 'funds_for_development.csv',
        'plot_type': 'bar',
        'y1_axis': 'percentage',
        'y2_axis': False,
        'x_title': False,
        'x_rot': 0,
        'x_max_len': 22,
        'y_title': False,
        'chart_title': 'Have you ever included costs for software development in a bid?',
        'show_values': True,
        'skip_labels': False,
        'skip_data_labels': False,
        'bottom_size': 0.15,
        'left_size': 0.08,
        'title_font_size': 18,
        'axis_font_size': 15,
        'value_font_size': 15,
        'uniform_colour': False
    }

    }
    
    
    
    
    
