"""
Created on Thu Sept  16 12:10:41 2021

@author: marco
This script requires only --output_folder option.
run it like: python3 src/pi_hf/pi_hf/scriptLPP.py --input_file test/input/inputs_1_LPP.csv  --output_folder out

"""

import argparse
import os
import pandas as pd
import yaml
import sys
from termcolor import colored


USAGE = """ usage: run it like: python3 src/pi_hf/pi_hf/scriptLPP.py --input_file test/input/inputs_1_LPP.csv  --output_folder out
input_file file where the input csv file will be loaded
output_folder:  folder where the output csv file will be stored
"""

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default=None,
                        help='Name of the file where the input csv file will be loaded')
    parser.add_argument('--output_folder', type=str, default='./',
                        help='Name of the folder where the output csv file will be stored')
    return parser.parse_args(args)


def load_data(filename):
    return pd.read_csv(filename)


def checkInput(area, lowB, upB):
    while True:
        var = int(input(area))
        if lowB <= var < upB:
            return var
        else:
            print("value must be in [", lowB, ",", upB, "]")


def getValues(input_file=None):
    if input_file is None:
        a = checkInput("Shoulders ", 0, 10)
        b = checkInput("Right upper back ", 0, 10)
        c = checkInput("Right lower back and hip ", 0, 10)
        d = checkInput("Right upper leg ", 0, 10)
        e = checkInput("Left upper leg ", 0, 10)
        f = checkInput("Left lower back and hip ", 0, 10)
        g = checkInput("Left upper back ", 0, 10)
        h = checkInput("Right lower arm ", 0, 10)
        i = checkInput("Right upper arm ", 0, 10)
        j = checkInput("Right lower back and hip ", 0, 10)
        k = checkInput("Left lower back and hip ", 0, 10)
        l = checkInput("Chest ", 0, 10)
        m = checkInput("Left upper arm ", 0, 10)
        n = checkInput("Left lower arm ", 0, 10)
    else:
        result = pd.read_csv(input_file, sep=',')
        a = int(result[result["itemID"] == "A"]["answer"])
        b = int(result[result["itemID"] == "B"]["answer"])
        c = int(result[result["itemID"] == "C"]["answer"])
        f = int(result[result["itemID"] == "F"]["answer"])
        g = int(result[result["itemID"] == "G"]["answer"])
        d = int(result[result["itemID"] == "D"]["answer"])
        e = int(result[result["itemID"] == "E"]["answer"])
        h = int(result[result["itemID"] == "H"]["answer"])
        i = int(result[result["itemID"] == "I"]["answer"])
        m = int(result[result["itemID"] == "M"]["answer"])
        n = int(result[result["itemID"] == "N"]["answer"])
        j = int(result[result["itemID"] == "J"]["answer"])
        k = int(result[result["itemID"] == "K"]["answer"])
        l = int(result[result["itemID"] == "L"]["answer"])

    return a, b, c, d, e, f, g, h, i, j, k, l, m, n


def getThresholds(val):
    if 0 <= val < 3:
        return "Low pressure"
    elif 3 <= val < 5:
        return "Medium pressure"
    else:
        return "High pressure"



def main(config):
    a, b, c, d, e, f, g, h, i, j, k, l, m, n = getValues(config.input_file)

    back_shoulders_v = (a + b + c + f + g) / 5
    arm_v = (h + i + m + n) / 4
    chest_v = l
    belly_hips_v = (j + k) / 2
    legs_v = (d + e) / 2

    back_shoulders_t = getThresholds(back_shoulders_v)
    arm_t = getThresholds(arm_v)
    chest_t = getThresholds(chest_v)
    belly_hips_t = getThresholds(belly_hips_v)
    legs_t = getThresholds(legs_v)

    # writeCSV(arm_t, arm_v, back_shoulders_t, back_shoulders_v, belly_hips_t, belly_hips_v, chest_t, chest_v, config,
    #         legs_t, legs_v)

    str_score = "type: vector\n"
    str_score += 'label: [back_shoulders, arm, chest, belly_hips, legs]\n'
    str_score += f'value: [{back_shoulders_v:.1f}, {arm_v:.1f}, {chest_v:.1f}, {belly_hips_v:.1f}, {legs_v:.1f}]\n'

    if not os.path.exists(config.output_folder):
        os.makedirs(config.output_folder)

    file_output = config.output_folder + "/pi_lpp.yaml"
    with open(file_output, 'w') as file:
        file.write(str_score)

def writeCSV(arm_t, arm_v, back_shoulders_t, back_shoulders_v, belly_hips_t, belly_hips_v, chest_t, chest_v, config,
             legs_t, legs_v):
    result = pd.read_csv(config.input_file, sep=',')
    mask = result.Area == "Arm"
    result.loc[mask, "Score"] = arm_v
    result.loc[mask, "Bench"] = arm_t
    mask = result.Area == "Back/Shoulders"
    result.loc[mask, "Score"] = back_shoulders_v
    result.loc[mask, "Bench"] = back_shoulders_t
    mask = result.Area == "Belly/Hips"
    result.loc[mask, "Score"] = belly_hips_v
    result.loc[mask, "Bench"] = belly_hips_t
    mask = result.Area == "Chest"
    result.loc[mask, "Score"] = chest_v
    result.loc[mask, "Bench"] = chest_t
    mask = result.Area == "Legs"
    result.loc[mask, "Score"] = legs_v
    result.loc[mask, "Bench"] = legs_t

    s = config.input_file.split("_")[1]

    if not os.path.exists(config.output_folder):
        os.makedirs(config.output_folder)

    result.to_csv(config.output_folder + "/" + s + "_questionnaire_LPP.csv", sep=",", index=False)


ENTRY_USAGE = """ usage: run_lpp input_file output_folder
input_file: questionnaire data
output_folder: folder where the generated PI yaml files will be stored
"""


def entry_point():
    if len(sys.argv) != 3:
        print(colored("Wrong input parameters !", "red"))
        print(colored(ENTRY_USAGE, "yellow"))
        sys.exit(1)

    file_in = sys.argv[1]
    folder_out = sys.argv[2]

    if not os.path.exists(file_in):
        print(colored("Input file {} does not exist".format(file_in), "red"))
        sys.exit(-1)

    if not os.path.isfile(file_in):
        print(colored("Input path {} is not a file".format(file_in), "red"))
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

    l_argument = ['--input_file', file_in, '--output_folder', folder_out]

    args = parse_args(l_argument)
    sys.exit(main(args))


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)
