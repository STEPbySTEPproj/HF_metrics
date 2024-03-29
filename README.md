# HF_metrics

Todo: _To be extended to cover the two other scripts_

[scriptDualTask.py](src/pi_hf/scriptDualTask.py) takes as an input the data files (in .csv format) related to the HF protocols for both with and without the use of exoskeleton.
Datafile names should be provided with .csv extension.
Condition data file (in .yaml format) related to the execution time for ascending/descending task is also required as an input.

It then computes the related metrics.
It also optionally accepts the output folder name.

2 other algorithms are also proposed, `uei` and `lpp` (to be detailed).

## Installation

python3 is used.

Under Linux, a standard installation in a local environment is obtained using:

```term
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -e src/pi_hf
# once done
deactivate
```

Under Windows:

```term
py -m venv venv
.\venv\Scripts\activate
pip install -U --upgrade pip
pip install -e .\src\pi_hf
# once done
deactivate
```

## Use

Using the reference data provided with the repository, one can call (assuming folder `out` exists):

```console
run_dualtask test/dualtask/input/subject_1_platformData_exo.csv test/dualtask/input/subject_1_platformData_noexo.csv test/dualtask/input/subject_1_condition.yaml out
# if the python package, has not been installed as indicated
python3 src/pi_hf/pi_hf/scriptDualTask.py -edf test/dualtask/input/subject_1_platformData_exo.csv -ndf test/dualtask/input/subject_1_platformData_noexo.csv --condition test/dualtask/input/subject_1_condition.yaml --output_folder out
# use py instead of python3 under windows
```

Similarly:

```console
run_lpp test/lpp/input/inputs_1_LPP.csv out
# if package not installed (if input_file is not indicated, will read from command line)
python3 src/pi_hf/pi_hf/scriptLPP.py --input_file test/lpp/input/inputs_1_LPP.csv --output_folder out
run_uei test/uei/input/inputs_1_UEI.csv out
# if package not installed (if input_file is not indicated, will read from command line)
python3 src/pi_hf/pi_hf/scriptUEI.py --input_file test/uei/input/inputs_1_UEI.csv --output_folder out
```

Note that the uei script expect values already preprocessed (i.e values in `[1,2,3]`).
To use raw data:

```console
run_uei test/uei/input/inputs_1_UEI_raw.csv False out
```

## Docker image

The use of Docker image is only available for Linux machine

### Build from source

Caution: _(only tested under Linux)_

Run the following command in order to create the docker image for this PI:

```console
docker build . -t pi_sbs_hf
```

### Get official image

An image ready to be used is available on Docker Hub, and can be directly installed and used:

```console
docker pull eurobenchtest/pi_sbs_human_factor
```

### Launch the docker image

Assuming `test/input` contains the input data, and that the directory `out/` is **already created**, and will contain the PI output:

```shell
docker run --rm -v $PWD/test/dualtask/input:/in -v $PWD/out:/out pi_sbs_hf run_dualtask /in/subject_1_platformData_exo.csv /in/subject_1_platformData_noexo.csv /in/subject_1_condition.yaml /out
docker run --rm -v $PWD/test/lpp/input:/in -v $PWD/out:/out pi_sbs_hf run_lpp /in/inputs_1_LPP.csv /out
docker run --rm -v $PWD/test/uei/input:/in -v $PWD/out:/out pi_sbs_hf run_uei /in/inputs_1_UEI.csv /out
```

## Questionnaire input

A simple tool is proposed to collected the questionnaire data, for the `lpp` and `uei` protocol.
The tool can be installed as a regular python package:

```term
# follow the guidelines provided above to set and activate a virtual environment
pip install -e src/questionnaire
run_questionnaire
```

A web page is mounted at direction: http://127.0.0.1:5000/.
Follow the indication to enter the questionnaire values and generate the csv files needed to feed the `lpp` and `uei` scripts.

## Acknowledgements

<a href="http://eurobench2020.eu">
  <img src="http://eurobench2020.eu/wp-content/uploads/2018/06/cropped-logoweb.png"
       alt="rosin_logo" height="60" >
</a>

Supported by Eurobench - the European robotic platform for bipedal locomotion benchmarking.
More information: [Eurobench website][eurobench_website]

<img src="http://eurobench2020.eu/wp-content/uploads/2018/02/euflag.png"
     alt="eu_flag" width="100" align="left" >

This project has received funding from the European Union’s Horizon 2020
research and innovation programme under grant agreement no. 779963.

The opinions and arguments expressed reflect only the author‘s view and
reflect in no way the European Commission‘s opinions.
The European Commission is not responsible for any use that may be made
of the information it contains.

[eurobench_logo]: http://eurobench2020.eu/wp-content/uploads/2018/06/cropped-logoweb.png
[eurobench_website]: http://eurobench2020.eu "Go to website"
