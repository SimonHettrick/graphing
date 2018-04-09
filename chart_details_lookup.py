#!/usr/bin/env python
# encoding: utf-8

'''
global_specs sets up some global variables for the plots
'''

global_specs = {
    'plot_width': 5.8,
    'plot_height': 5.8,
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
11. bottom_size: fraction of chart dedicated to x-axis tick labels (0-1)
12. title_font_size: size of title font
13. axis_font_size: size of axis fonts
14. value_font_size: size of value label font
'''


plot_details = {
    'software_survey': {
            'filename': 'software_survey.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': False,
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'software_survey_training': {
            'filename': 'software_survey_training.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': False,
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'software_in_papers': {
            'filename': 'software_in_papers.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': False,
            'show_values': True,
            'skip_labels': 3,
            'bottom_size': 0.1,
            'left_size' : 0.08,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'all_funder_software_grant_percentage': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'software spend as percentage of spend on all grants',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Total RC investment (%)',
            'chart_title': False,
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : 0.08,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'all_funder_software_grant_cost': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'all funders software spend (Millions)',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Total RC investment (£ millions)',
            'chart_title': False,
            'show_values': False,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : 0.08,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'all_funder_software_grant_cost_plus_SSI': {
            'filename': 'yearly_all_grants_costs_by_funder_plus_SSI.csv',
            'plot_type': 'bar',
            'y1_axis': 'all funders software spend (Millions)',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Total RC investment (£ millions)',
            'chart_title': False,
            'show_values': False,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : 0.08,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'ahrc_software_grant_percentage': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'AHRC software spend %',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': 'AHRC',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'bbsrc_software_grant_percentage': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'BBSRC software spend %',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': 'BBSRC',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'epsrc_software_grant_percentage': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'EPSRC software spend %',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': 'EPSRC',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'esrc_software_grant_percentage': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'ESRC software spend %',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': 'ESRC',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'mrc_software_grant_percentage': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'MRC software spend %',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': 'MRC',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'nerc_software_grant_percentage': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'NERC software spend %',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': 'NERC',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },            
    'stfc_software_grant_percentage': {
            'filename': 'yearly_all_grants_costs_by_funder.csv',
            'plot_type': 'bar',
            'y1_axis': 'STFC software spend %',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': False,
            'chart_title': 'STFC',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'left_size' : False,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },            
            
    }
    
    
    
    
    