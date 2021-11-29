# HF_metrics

_To be extended to cover the two other scripts_
[script.py](script.py) takes as an input the data files (in .csv format) related to the HF protocols for both with and without the use of exoskeleton.
Datafile names should be provided with .csv extension.
Condition data file (in.yaml format) related to the execution time for ascending/descending task is also required as an input.

It then computes the related metrics. It also optionally accepts the output folder name.

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

Using the reference data provided with the repository, one can call:

```console
run_hf test/input/subject_1_platformData_exo.csv test/input/subject_1_platformData_noexo.csv test/input/subject_1_condition.yaml out
# if the python package, has not been installed as indicated
python3 src/pi_hf/pi_hf/script.py -edf test/input/subject_1_platformData_exo.csv -ndf test/input/subject_1_platformData_noexo.csv --condition test/input/subject_1_condition.yaml --output_folder out
# use py instead of python3 under windows
```

## Docker image

### Build from source

_(only tested under Linux)_

Run the following command in order to create the docker image for this PI:

```console
docker build . -t pi_sbs_hf
```

### Launch the docker image

Assuming `test/input` contains the input data, and that the directory `out/` is **already created**, and will contain the PI output:

```shell
docker run --rm -v $PWD/test/input:/in -v $PWD/out:/out pi_sbs_hf run_pi_hf /in/subject_1_platformData_exo.csv /insubject_1_platformData_noexo.csv /in/subject_1_condition.yaml /out
```

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
