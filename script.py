#!/usr/bin/env python3
"""
Created on Tue Apr  6 15:10:41 2021

@author: asad
"""

import argparse
import os
import pandas as pd
import yaml


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--exo_datafile', '-edf', type=str, required=True,
                        help='Name of the exoskeleton datafile (write with .csv extension)')  # relative to this script
    parser.add_argument('--noexo_datafile', '-ndf', type=str, required=True,
                        help='Name of the normal datafile without exo (write with .csv extension)')
    parser.add_argument('--output_file', type=str, default='HR_metrics',
                        help='Name of the output yaml file (write without .yaml extension)')
    parser.add_argument('--exo_task_time', '-et', type=float, required=True,
                        help='Total time for task execution time in seconds with exoskeleton')
    parser.add_argument('--noexo_task_time', '-nt', type=float, required=True,
                        help='Total time for task execution in seconds without exoskeleton')

    return parser.parse_args()


def load_data(filename):

    data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    return pd.read_csv(data_path)


def main(config):

    df_no_exo = load_data(config.noexo_datafile)
    df_exo = load_data(config.exo_datafile)

    #######################
    # NO EXOSKELETON DATA
    #######################

    # total wrong asnwers
    total_resp_df_no_exo = df_no_exo.filter(regex='total_responses')
    total_resp_correct_df_no_exo = df_no_exo.filter(regex='total_correct')

    dim_df_no_exo = total_resp_df_no_exo.size

    total_resp_no_exo = total_resp_df_no_exo.iloc[dim_df_no_exo-1, :].values
    total_resp_correct_no_exo = total_resp_correct_df_no_exo.iloc[dim_df_no_exo-1, :].values

    total_err_no_exo = float(total_resp_no_exo - total_resp_correct_no_exo)

    print("***** NO EXOSKELETON DATA *****")
    print(f"Total number of responses: {total_resp_no_exo}")
    print(f"Total number of correct responses: {total_resp_correct_no_exo}")
    print(f"Total number of wrong responses: {total_err_no_exo}")

    # total time: sum of times from question to answer
    total_time_df_no_exo = df_no_exo.filter(regex='total_response_time')
    total_time_no_exo = float(total_time_df_no_exo.iloc[dim_df_no_exo-1, :].values/1000)  # [s]

    print(f"Total time taken for the responses [s]: {total_time_no_exo}")

    # execution time: total time ascending/descending
    exe_time_ad_no_exo = config.noexo_task_time

    #######################
    # EXOSKELETON DATA
    #######################

    total_resp_df_exo = df_exo.filter(regex='total_responses')
    total_resp_correct_df_exo = df_exo.filter(regex='total_correct')

    dim_df_exo = total_resp_df_exo.size

    total_resp_exo = total_resp_df_exo.iloc[dim_df_no_exo-1, :].values
    total_resp_correct_exo = total_resp_correct_df_exo.iloc[dim_df_no_exo-1, :].values

    total_err_exo = float(total_resp_exo - total_resp_correct_exo)

    print("***** EXOSKELETON DATA *****")
    print(f"Total number of responses: {total_resp_exo}")
    print(f"Total number of correct responses: {total_resp_correct_exo}")
    print(f"Total number of wrong responses: {total_err_exo}")

    # total time: sum of times from question to answer
    total_time_df_exo = df_exo.filter(regex='total_response_time')
    total_time_exo = float(total_time_df_exo.iloc[dim_df_exo-1, :].values/1000)  # [s]

    print(f"Total time taken for the responses [s]: {total_time_exo}")

    # execution time: total time ascending/descending
    exe_time_ad_exo = config.exo_task_time
    
    # data differences
    total_err_resp_diff = total_err_exo - total_err_no_exo
    tot_time_diff = total_time_exo - total_time_no_exo
    tot_ad_time_diff = float(exe_time_ad_exo) - float(exe_time_ad_no_exo)

    print("***** DATA DIFFERENCES *****")
    print(f"Difference in total number of wrong responses: {total_err_resp_diff}")
    print(f"Difference in total time taken for the responses: {tot_time_diff}")
    print(f"Difference in total execution time: {tot_ad_time_diff}")

    f_metrics_dict = {'total_errors': {'no exo': total_err_no_exo, 'exo': total_err_exo,
                                       'difference': total_err_resp_diff},
                      'total_responses_time': {'no exo': total_time_no_exo, 'exo': total_time_exo,
                                               'difference': tot_time_diff},
                      'total_execution_time': {'no exo': tot_ad_time_diff, 'exo': exe_time_ad_no_exo,
                                               'difference': exe_time_ad_exo}}

    with open(config.output_file, 'w') as file:
        yaml.dump(f_metrics_dict, file)


if __name__ == '__main__':
    args = parse_args()
    main(args)
