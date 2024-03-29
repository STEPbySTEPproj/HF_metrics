"""
Created on Thu Sept  16 13:35:41 2021

@author: marco
run it like:  python3 src/pi_hf/pi_hf/scriptUEI.py --input_file test/input/inputs_1_UEI.csv  --output_folder out

"""

import argparse
from operator import is_
import os
import pandas as pd
import yaml
import sys
from termcolor import colored

USAGE = """ usage: run it like:python3 src/pi_hf/pi_hf/scriptUEI.py --input_file test/input/inputs_1_UEI.csv  --output_folder out
input_file file where the input csv file will be loaded
output_folder:  folder where the output csv file will be stored
"""

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default=None,
                        help='Name of the file where the input csv file will be loaded')
    parser.add_argument('--output_folder', type=str, default='./',
                        help='Name of the folder where the output yaml file will be stored')
    return parser.parse_args(args)


def load_data(filename):
    # data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    return pd.read_csv(filename)


def checkInput(area, lowB, upB):
    print("values from ", lowB, " to ", upB)
    while True:
        # var = lowB+1
        var = int(input(area))
        if lowB <= var < upB:
            return var
        else:
            print("value must be in [", lowB, ",", upB, "]")


def checkInputBool(area):
    print("1 if yes, 0 if no")
    while True:
        var = int(input(area))
        # var = 1
        if var == 0:
            return False
        elif var == 1:
            return True
        print("value must be 0 or 1")


def getValues(input_file=None):
    if input_file is None:
        q1_1 = checkInput("1.1. Time required to donning the exoskeleton. ", 0, 10000)
        q1_2 = checkInput("1.2. Time required to doffing the exoskeleton.", 0, 10)
        q1_3 = checkInput("1.3. Number of stair levels climbed up.", 0, 6)
        q1_4 = checkInput("1.4. Number of stair levels climbed down.", 0, 6)
        q1_5 = checkInput("1.5. Number of steps walked up.", 6, 12)
        q1_6 = checkInput("1.6. Number of steps walked down.", 6, 12)
        q1_7 = checkInput("1.7. Number of times the user stumbled while ascending the stairs. ", 0, 10000)
        q1_8 = checkInput("1.8. Number of times the user stumbled while descending the stairs.", 0, 10000)
        q1_9 = checkInputBool("1.9. Is the crutch used during the test?")
        q1_10 = checkInputBool(
            "1.10. In general, is the torso bent forward (provoke high load of upper limbs when crutches are used) to avoid falling backwards?")
        q1_11 = checkInputBool(
            "1.11. During the Anterolateral shifting of body centre of gravity, is the swing leg adequately relieved to correctly initiate the stride?")
        q1_12 = checkInput("1.12. Number of error messages sent by the HMI (Human-Machine Interface). ", 0, 10000)
        q1_13 = checkInput(
            "1.13. Number of times the safe mode has been activated (the system switched off) when the situation did not require it?",
            0, 1000000)
        q1_14 = checkInputBool(
            "1.14. Has the safe mode not been activated (the system did not switch off) when the situation did require it?")
    else:
        result = pd.read_csv(input_file, sep=',')
        q1_1 = int(result[result["itemID"] == 1]["answer"])
        q1_2 = int(result[result["itemID"] == 2]["answer"])
        q1_3 = int(result[result["itemID"] == 3]["answer"])
        q1_4 = int(result[result["itemID"] == 4]["answer"])
        q1_5 = int(result[result["itemID"] == 5]["answer"])
        q1_6 = int(result[result["itemID"] == 6]["answer"])
        q1_7 = int(result[result["itemID"] == 7]["answer"])
        q1_8 = int(result[result["itemID"] == 8]["answer"])
        q1_9 = bool(int(result[result["itemID"] == 9]["answer"]))
        q1_10 = bool(int(result[result["itemID"] == 10]["answer"]))
        q1_11 = bool(int(result[result["itemID"] == 11]["answer"]))
        q1_12 = int(result[result["itemID"] == 12]["answer"])
        q1_13 = int(result[result["itemID"] == 13]["answer"])
        q1_14 = bool(int(result[result["itemID"] == 14]["answer"]))
    return q1_1, q1_2, q1_3, q1_4, q1_5, q1_6, q1_7, q1_8, q1_9, q1_10, q1_11, q1_12, q1_13, q1_14


def getThresholds(input_file):
    result = pd.read_csv(input_file, sep=',')
    q1_1 = int(result[result["itemID"] == 1]["answer"])
    q1_2 = int(result[result["itemID"] == 2]["answer"])
    q1_3 = int(result[result["itemID"] == 3]["answer"])
    q1_4 = int(result[result["itemID"] == 4]["answer"])
    q1_5 = int(result[result["itemID"] == 5]["answer"])
    q1_6 = int(result[result["itemID"] == 6]["answer"])
    q1_7 = int(result[result["itemID"] == 7]["answer"])
    q1_8 = int(result[result["itemID"] == 8]["answer"])
    q1_9 = int(result[result["itemID"] == 9]["answer"])
    q1_10 = int(result[result["itemID"] == 10]["answer"])
    q1_11 = int(result[result["itemID"] == 11]["answer"])
    q1_12 = int(result[result["itemID"] == 12]["answer"])
    q1_13 = int(result[result["itemID"] == 13]["answer"])
    q1_14 = int(result[result["itemID"] == 14]["answer"])
    return q1_1, q1_2, q1_3, q1_4, q1_5, q1_6, q1_7, q1_8, q1_9, q1_10, q1_11, q1_12, q1_13, q1_14



def getThresholds1(val, A, B):
    if 0 <= val < A:
        return 1
    elif A <= val < B:
        return 2
    else:
        return 3


def getThresholds2(val, A, B):
    if 0 <= val < A:
        return 3
    elif A <= val < B:
        return 2
    else:
        return 1


def getThresholds3(val):
    if val:
        return 3
    return 1


def getThresholds4(val):
    if not val:
        return 3
    return 1


def main(config, is_pre_processed=False):

    if is_pre_processed:
        q1_1t, q1_2t, q1_3t, q1_4t, q1_5t, q1_6t, q1_7t, q1_8t, q1_9t, q1_10t, q1_11t, q1_12t, q1_13t, q1_14t = getThresholds(config.input_file)
    else:
        q1_1_v, q1_2_v, q1_3_v, q1_4_v, q1_5_v, q1_6_v, q1_7_v, q1_8_v, q1_9_v, q1_10_v, q1_11_v, q1_12_v, q1_13_v, q1_14_v = getValues(
            config.input_file)
        # bounds can be changed
        q1_1t = getThresholds1(q1_1_v, 5, 10)
        q1_2t = getThresholds1(q1_2_v, 5, 10)
        q1_3t = getThresholds2(q1_3_v, 2, 4)
        q1_4t = getThresholds2(q1_4_v, 2, 4)
        q1_5t = getThresholds2(q1_5_v, 6, 9)
        q1_6t = getThresholds2(q1_6_v, 6, 9)
        q1_7t = getThresholds1(q1_7_v, 2, 5)
        q1_8t = getThresholds1(q1_8_v, 2, 5)
        q1_9t = getThresholds3(q1_9_v)
        q1_10t = getThresholds3(q1_10_v)
        q1_11t = getThresholds4(q1_11_v)
        q1_12t = getThresholds1(q1_12_v, 2, 3)
        q1_13t = getThresholds1(q1_13_v, 2, 3)
        q1_14t = getThresholds3(q1_14_v)

    print(f'1: {q1_1t}')
    print(f'2: {q1_2t}')
    print(f'3: {q1_3t}')
    print(f'4: {q1_4t}')
    print(f'5: {q1_5t}')
    print(f'6: {q1_6t}')
    print(f'7: {q1_7t}')
    print(f'8: {q1_8t}')
    print(f'9: {q1_9t}')
    print(f'10: {q1_10t}')
    print(f'11: {q1_11t}')
    print(f'12: {q1_12t}')
    print(f'13: {q1_13t}')
    print(f'14: {q1_14t}')

    sum = q1_1t + q1_2t + q1_3t + q1_4t + q1_5t + q1_6t + q1_7t + q1_8t + q1_9t + q1_10t + q1_11t + q1_12t + q1_13t + q1_14t
    avg = sum / 14

    print(f'sum: {sum}')
    print(f'avg: {avg}')
    if avg < 1.5:
        avg_t = "High EUI quality"
    elif 1.5 <= avg < 2:
        avg_t = "Medium EUI quality"
    else:
        avg_t = "Low EUI quality"

    str_score = 'type: scalar\n'
    str_score += f'value: {avg:.1f}\n'

    if not os.path.exists(config.output_folder):
        os.makedirs(config.output_folder)

    file_output = config.output_folder + "/pi_uei.yaml"
    with open(file_output, 'w') as file:
        file.write(str_score)


def writeCSV(avg, avg_t, config, q1_10t, q1_11t, q1_12t, q1_13t, q1_14t, q1_1t, q1_2t, q1_3t, q1_4t, q1_5t, q1_6t,
             q1_7t, q1_8t, q1_9t):
    result = pd.read_csv(config.input_file, sep=',')
    mask = result.Type == "1.1"
    result.loc[mask, "Bench"] = q1_1t
    mask = result.Type == "1.2"
    result.loc[mask, "Bench"] = q1_2t
    mask = result.Type == "1.3"
    result.loc[mask, "Bench"] = q1_3t
    mask = result.Type == "1.4"
    result.loc[mask, "Bench"] = q1_4t
    mask = result.Type == "1.5"
    result.loc[mask, "Bench"] = q1_5t
    mask = result.Type == "1.6"
    result.loc[mask, "Bench"] = q1_6t
    mask = result.Type == "1.7"
    result.loc[mask, "Bench"] = q1_7t
    mask = result.Type == "1.8"
    result.loc[mask, "Bench"] = q1_8t
    mask = result.Type == "1.9"
    result.loc[mask, "Bench"] = q1_9t
    mask = result.Type == "1.10"
    result.loc[mask, "Bench"] = q1_10t
    mask = result.Type == "1.11"
    result.loc[mask, "Bench"] = q1_11t
    mask = result.Type == "1.12"
    result.loc[mask, "Bench"] = q1_12t
    mask = result.Type == "1.13"
    result.loc[mask, "Bench"] = q1_13t
    mask = result.Type == "1.14"
    result.loc[mask, "Bench"] = q1_14t
    mask = result.Type == "Score"
    result.loc[mask, "Value"] = avg
    mask = result.Type == "Benchmark"
    result.loc[mask, "Value"] = avg_t
    s = config.input_file.split("_")[1]
    if not os.path.exists(config.output_folder):
        os.makedirs(config.output_folder)
    result.to_csv(config.output_folder + "/" + s + "_questionnaire_UEI.csv", sep=",", index=False)


ENTRY_USAGE = """ usage: run_uei input_file output_folder
input_file: questionnaire data
pre_processed: whether data is already preprocessed (optional, default: True)
output_folder: folder where the generated PI yaml files will be stored
"""


def entry_point():
    if len(sys.argv) not in [3, 4]:
        print(colored("Wrong input parameters !", "red"))
        print(colored(ENTRY_USAGE, "yellow"))
        sys.exit(1)
    file_in = sys.argv[1]
    if len(sys.argv) == 3:
        is_preprocessed = True
        folder_out = sys.argv[2]
    else:
        is_preprocessed = sys.argv[2].lower() in ("yes", "true", "t", "1")
        folder_out = sys.argv[3]

    if not os.path.exists(file_in):
        print(colored(f'Input file {file_in} does not exist', "red"))
        sys.exit(-1)

    if not os.path.isfile(file_in):
        print(colored(f'Input path {file_in} is not a file', "red"))
        sys.exit(-1)

    if not os.path.exists(folder_out):
        print(colored(f'Output folder {folder_out} does not exist', "red"))
        sys.exit(-1)

    if not os.path.isdir(folder_out):
        print(colored(f'{folder_out} is not a folder', "red"))
        sys.exit(-1)

    l_argument = ['--input_file', file_in, '--output_folder', folder_out]

    args = parse_args(l_argument)
    sys.exit(main(args, is_pre_processed=is_preprocessed))


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)
