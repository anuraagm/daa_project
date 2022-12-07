# Design and Analysis of Algorithms Project

This repository contains the source code and certain output files for the design and analysis of algorithms project
carried out by Anuraag Muktevi and Jayanth Reddy Gundala, for the class 2228-CSE-5311-009-DSGN & ANLY ALGORITHMS.

## Please note, all the output graphs are already present for viewing in the './io/metrics_images' folder.


### System pre-requisites for running this project :

* The latest version of Python3.X needs to be downloaded from [here](https://www.python.org/downloads/) and installed.
* This project runs the sorting algorithm on an extremely large array size. Therefore, a system with at least 8GB of RAM or higher is recommended to quickly see the sorting functions in action.

### Library requirements :
* Numpy is required in order to generate the randomized array used in the comparitive study. This can be done using either one of the following commands : "pip install numpy" or "pip3 install numpy".
* Matplotlib is used in order to plot the time comparison graphs. This library can be installed using the commands : "pip install matplotlib" or "pip3 install matplotlib".

### Project setup :
* Download the zip file and unzip the folder contents on your system.
* Alternatively you can also run the "git clone https://github.com/anuraagm/daa_project.git" in a folder location of your choice.

### Running the main project :
There are 2 ways in which this project can be run :

#### Viewing direct outputs : 
In this method, the output files which are already generated, can be used in order to view the time graphs of the merge, merge-insert, quick and quick-insert sort comparisons.
To view this output :

* Open up a terminal in the project folder
* Run the command "python merge_vs_merge_insert_analysis.py" or "python3 merge_vs_merge_insert_analysis.py" for Merge Sort vs Insertion in Merge Sort, analysis outputs.
* Run the command "python quick_vs_quick_insert_analysis.py" or "python3 quick_vs_quick_insert_analysis.py" for Quick Sort vs Insertion in Quick Sort, analysis outputs.

#### Generating and viewing outputs :
In this method, the output files, which mention how long it took for each sorting algorithm to complete the sorting operation, are first generated from randomly generated array outputs.
Following this the plotting files can be called again to re-view the graphs on the updated timing values.

* Open up a terminal in the project folder
* Run the command "python merge_vs_merge_insert.py" or "python3 merge_vs_merge_insert.py" for Merge Sort vs Insertion in Merge Sort, output generation.
* Run the command "python quick_vs_quick_insert.py" or "python3 quick_vs_quick_insert.py" for Quick Sort vs Insertion in Quick Sort, output generation.
* Run the command "python merge_vs_merge_insert_analysis.py" or "python3 merge_vs_merge_insert_analysis.py" for Merge Sort vs Insertion in Merge Sort, analysis outputs.
* Run the command "python quick_vs_quick_insert_analysis.py" or "python3 quick_vs_quick_insert_analysis.py" for Quick Sort vs Insertion in Quick Sort, analysis outputs.

### Running other files :

#### Validating the sort algorithms :

* Open up a terminal in the project folder
* To check the outputs of the insertion sort algorithm, run "python insertion_sort.py" or "python3 insertion_sort.py". The output can be seen, for all iterations in the location './io/insertion_sort'.
* To check the outputs of the merge sort algorithm, run "python merge_sort.py" or "python3 merge_sort.py". The output can be seen, for all iterations in the location './io/merge_sort'.
* To check the outputs of the quick sort algorithm, run "python quick_sort.py" or "python3 quick_sort.py". The output can be seen, for all iterations in the location './io/quick_sort'.
* To check the outputs of the insert in merge sort algorithm, run "python merge_insert_sort.py" or "python3 merge_insert_sort.py". The output can be seen, for all iterations in the location './io/merge_insert_sort'.
* To check the outputs of the insert in quick sort algorithm, run "python quick_insert_sort.py" or "python3 quick_insert_sort.py". The output can be seen, for all iterations in the location './io/quick_insert_sort'.

#### Validating threshold check algorithms :
* Open up a terminal in the project folder
* To check the threshold calculation for when insertion sort should be used instead of merge sort, run "python insertion_vs_merge.py" or "python3 insertion_vs_merge.py". Then run the command "python insertion_vs_merge_analysis.py" or "python3 insertion_vs_merge_analysis.py". The outputs for the analysis will be displayed and can be accessed from './io/metrics_images'.
* To check the threshold calculation for when insertion sort should be used instead of quick sort, run "python insertion_vs_quick.py" or "python3 insertion_vs_quick.py". The outputs for the analysis will be displayed and can be accessed from './io/metrics_images'.
