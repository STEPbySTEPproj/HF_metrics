# HF_metrics

[STEPbySTEP_HF_metrics.ipynb](STEPbySTEP_HF_metrics.ipynb) allows to upload data related to HF protocols with and without the use of the exoskeleton, computing the related metrics. The metrics are saved in a .csv file.

[script.py](script.py) takes as an input the data files (in .csv format) related to the HF protocols for both with and without the use of exoskeleton. Datafiles should be provided relative to where the script is run from. 
It then computes the related metrics. It also optionally accepts the output filename (in .yaml format). 

After executing the script, the user is asked to insert the total time taken for performing the asending/descending task with and without using esoskeleton 

The usage is like this:
```
python script.py --exo_datafile FILENAME_EXO --normal_datafile FILENAME_WITHOUT_EXO 
--output_file FILENAME_OUT
```
