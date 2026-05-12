# Revealing the Domains of Scene Evaluation from Natural Language

This project aims to understand which conceptual domains people spontaneously rely on when perceiving visual scenes, addressing a gap in prior research that has focused mainly on predefined categories in scene perception/categorization. By analyzing free-response language, this study intends to implement a data-driven approach to understand the underlying structure of scene perception and mental representations.

The pipeline refers to a dictionary-based content analysis framework used in Nicholas, Uddenberg, and Todorov (2025)[OSF](https://osf.io/pmtxw/overview?view_only=a485688056a8495ba37082f38c690833). 

## Repo Structure
This repository initially includes the following files. 
- analysis.ipynb: is a data analysis script 
- README.md: provides an overview of the repository
- requirements.txt
- data/: stores raw and processed datasets in a `.csv` format
    - main_data.csv: an example raw data

The following `.csv` files will be created and saved under `data/` after running `analysis.ipynb`. 
While these files will already be included in the repository, they can be deleted before rerunning the notebook
    - main_clean.csv
    - LDA_4_topics.csv
    - LDA_6_topics.csv
    - LDA_8_topics.csv
    - 05_semantic_dimension_assignment.csv
    - 06_domain_prevalence.csv

## Environment
This project was developed using:
- Python 3.13
- Jupyter Notebook

## Running the Analysis
1. Install the required dependencies
```
pip install -r requirements.txt
```
2. Open analysis.ipynb
3. Go to the Python environment
   
5. and run the notebook cells sequentially.
- Helpful keys are:
    - command/ctrl + enter (run the current cell and stay at the current cell)
    - shift + enter (run the current cell and go to the next cell)

## Input Data
The intended input data are written responses from participants. The participants will be asked to spontaneously generate six short text impressions for each presented scene image, and their entries will be structured in a CSV file, six entries recorded in six respective columns (next to other necessary information, such as participant ID, image ID, and response time). 

## Further Use of This Repository
This text analysis pipeline can be applied to other types of free-response data for data cleaning and topic modeling purposes. It can be extended to visual perception experiments that investigate not only scenes but also other subjects.
