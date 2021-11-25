

import sys
import os
from pi_hf.script import main, parse_args
from termcolor import colored

USAGE = """ usage: run exo_datafile noexo_datafile exo_task_time no_exo_task_time output_folder
-->exo_datafile: Name of the exoskeleton datafile (write without .csv extension)
-->noexo_datafile: Name of the normal datafile without exo (write without .csv extension)
-->exo_task_time: Total time for task execution time in seconds with exoskeleton
-->noexo_task_time: Total time for task execution in seconds without exoskeleton
-->output_folder: folder where the generated PI yaml files will be stored
"""

def main_script():
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
