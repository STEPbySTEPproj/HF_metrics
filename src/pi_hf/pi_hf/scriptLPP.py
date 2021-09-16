#!/usr/bin/env python3
"""
Created on Thu Sept  16 12:10:41 2021

@author: marco
This script requires only --output_folder option.
run it like: python3 src/pi_hf/pi_hf/scriptLPP.py  --output_folder out

"""

import argparse
import os
import pandas as pd
import yaml
import sys



def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_folder', type=str, default='./',
                        help='Name of the folder where the output yaml file will be stored')
    return parser.parse_args(args)


def load_data(filename):
    return pd.read_csv(filename)


def checkInput(area, lowB, upB):
    while True:
        var =  int(input(area))
        if var >= lowB and var < upB:
            return var
        else:
            print("value must be in [", lowB, ",", upB, "]")


def getValues():
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

    return a, b, c, d, e, f, g, h, i, j, k, l, m, n


def getThresholds(val):
    if val >= 0 and val < 3:
        return "Low pressure"
    elif val >= 3 and val < 5:
        return "Medium pressure"
    else:
        return "High pressure"


def main(config):

    a, b, c, d, e, f, g, h, i, j, k, l, m, n = getValues()

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



    f_metrics_dict = {
        'Back/Shoulders':
            {
                'A': a,
                'B': b,
                'C': c,
                'F': f,
                'H': h,
                'Score': back_shoulders_v,
                'Bench': back_shoulders_t
            },
        'Arm':
            {
                'H': a,
                'I': b,
                'M': c,
                'N': f,
                'Score': arm_v,
                'Bench': arm_t
            },
        'Chest':
            {
                'L': l,
                'Score': chest_v,
                'Bench': chest_t
            },
        'Belly/Hips':
            {
                'J': j,
                'K':k,
                'Score': belly_hips_v,
                'Bench': belly_hips_t
            },
        'Legs':
            {
                'D': d,
                'E': e,
                'Score': legs_v,
                'Bench': legs_t
            }
    }

    if not os.path.exists(config.output_folder):
        os.makedirs(config.output_folder)

    file_output = config.output_folder + "/lpp.yaml"
    with open(file_output, 'w') as file:
        yaml.dump(f_metrics_dict, file)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)
