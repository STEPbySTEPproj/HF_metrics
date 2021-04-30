# HF_metrics

[script.py](script.py) takes as an input the data files (in .csv format) related to the HF protocols for both with and without the use of exoskeleton. Datafile names should be provided with .csv extension and relative to where the script is run from. Arguments related to the execution time for asending/descending task are also required as an input.

It then computes the related metrics. It also optionally accepts the output filename (in .yaml format).

## Installation

python3 is used.

Under Linux, a standard installation in a local environment is obtained using:

```term
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r src/pi_hf/requirements.txt
pip install -e src/pi_hf
#once done
deactivate
```

## Use

The command for using the script is below:

```console
python script.py --exo_datafile FILENAME_EXO --noexo_datafile FILENAME_WITHOUT_EXO
--exo_task_time TASK_TIME_EXO --noexo_task_time TASK_TIME_WITHOUT_EXO
--output_folder FILENAME_OUT
```

Using the reference data provided with the repository, one can call:

```console
run_pi_hf test/input/subject-1.csv test/input/subject-1.csv 1 1 out
# if the python package, has not been installed as indicated
python3 src/pi_hf/pi_hf/script.py -edf test/input/subject-1.csv -ndf test/input/subject-1.csv --exo_task_time 1 --noexo_task_time 1 --output_folder out
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
docker run --rm -v $PWD/test/input:/in -v $PWD/out:/out pi_sbs_hf run_pi_hf /in/subject-1.csv /in/subject-1.csv 1 1 /out
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
