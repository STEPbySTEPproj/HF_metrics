"""
Created on Tue Apr  6 15:10:41 2021

@author: asad
"""

import argparse
import os
import pandas as pd
import yaml
import sys
from termcolor import colored


def parse_args(args):

    parser = argparse.ArgumentParser()
    parser.add_argument('--exo_datafile', '-edf', type=str, required=True,
                        help='Name of the exoskeleton datafile (write with .csv extension)')  # relative to this script
    parser.add_argument('--noexo_datafile', '-ndf', type=str, required=True,
                        help='Name of the normal datafile without exo (write with .csv extension)')
    parser.add_argument('--output_folder', type=str, default='./',
                        help='Name of the folder where the output yaml file will be stored')
    parser.add_argument('--condition', type=str, required=True,
                        help='Name of the file containing total time for the task execution')

    return parser.parse_args(args)


def load_data(filename):

    #data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    return pd.read_csv(filename)


def main(config):

    df_no_exo = load_data(config.noexo_datafile)
    df_exo = load_data(config.exo_datafile)

    #######################
    # NO EXOSKELETON DATA
    #######################

    # total wrong asnwers
    total_resp_df_no_exo = df_no_exo.filter(regex='total_responses')
    total_resp_correct_df_no_exo = df_no_exo.filter(regex='total_correct')

    dim_df_no_exo = total_resp_df_no_exo[8:].size # first 8 experiments are omitted

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

    #######################
    # EXOSKELETON DATA
    #######################

    total_resp_df_exo = df_exo.filter(regex='total_responses')
    total_resp_correct_df_exo = df_exo.filter(regex='total_correct')

    dim_df_exo = total_resp_df_exo[8:].size # first 8 experiments are omitted

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

    #######################
    # DATA DIFFERENCES
    #######################
    
    # execution time: total time ascending/descending

    with open(config.condition, 'r') as file:
        times = yaml.safe_load(file)
    
    exe_time_ad_no_exo = times['noexo_task_time']
    exe_time_ad_exo = times['exo_task_time']
    
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
    
    if not os.path.exists(config.output_folder):
        os.makedirs(config.output_folder)

    file_output = config.output_folder + "/pi_hf.yaml"
    with open(file_output, 'w') as file:
        yaml.dump(f_metrics_dict, file)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)

USAGE = """ usage: run exo_datafile noexo_datafile exo_task_time no_exo_task_time output_folder
-->exo_datafile: Name of the exoskeleton datafile (write without .csv extension)
-->noexo_datafile: Name of the normal datafile without exo (write without .csv extension)
-->exo_task_time: Total time for task execution time in seconds with exoskeleton
-->noexo_task_time: Total time for task execution in seconds without exoskeleton
-->output_folder: folder where the generated PI yaml files will be stored
"""

def entry_point():
    if len(sys.argv) != 5:
        print(colored("Wrong input parameters !", "red"))
        print(colored(USAGE, "yellow"))
        sys.exit(-1)

    fn_exo_datafile = sys.argv[1]
    fn_noexo_datafile = sys.argv[2]
    fn_condition = sys.argv[3]
    folder_out = sys.argv[4]

    if not os.path.exists(fn_exo_datafile):
        print(colored("Input file {} does not exist".format(fn_exo_datafile), "red"))
        sys.exit(-1)

    if not os.path.isfile(fn_exo_datafile):
        print(colored("Input path {} is not a file".format(fn_exo_datafile), "red"))
        sys.exit(-1)

    if not os.path.exists(fn_noexo_datafile):
        print(colored("Input file {} does not exist".format(fn_noexo_datafile), "red"))
        sys.exit(-1)

    if not os.path.isfile(fn_noexo_datafile):
        print(colored("Input path {} is not a file".format(fn_noexo_datafile), "red"))
        sys.exit(-1)

    if not os.path.exists(fn_condition):
        print(colored("Input file {} does not exist".format(fn_condition), "red"))
        sys.exit(-1)

    if not os.path.isfile(fn_condition):
        print(colored("Input path {} is not a file".format(fn_condition), "red"))
        sys.exit(-1)


    if not os.path.exists(folder_out):
        print(colored(
            "Output folder {} does not exist".format(folder_out),
            "red"))
        sys.exit(-1)

    if not os.path.isdir(folder_out):
        print(colored(
            "{} is not a folder".format(folder_out),
            "red"))
        sys.exit(-1)


    l_argument = ['-edf', fn_exo_datafile, '-ndf', fn_noexo_datafile, '--condition', fn_condition, '--output_folder', folder_out]

    args = parse_args(l_argument)
    sys.exit(main(args))
