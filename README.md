# Revealing the Domains of Scene Evaluation from Natural Language

This project aims to understand which conceptual domains people spontaneously rely on when perceiving visual scenes, addressing a gap in prior research that has focused mainly on predefined categories in scene perception/categorization. By analyzing free-response language, this study will use a data-driven approach to understand the underlying structure of scene perception and mental representations.

This text analysis was inspired by a dictionary-based content analysis framework used in Nicholas, Uddenberg, and Todorov (2025)[OSF](https://osf.io/pmtxw/overview?view_only=a485688056a8495ba37082f38c690833). 

## Repo Structure
This repository initially includes the following files. 
- analysis.ipynb: is a data analysis script 
- README.md: provides an overview of the repository
- requirements.txt: minimal required packages
- requirements_full.txt: complete environment backup generated with `pip freeze`
- data/: stores raw and processed datasets in a `.csv` format
    - main_data.csv: an example raw data

While the following `.csv` files are already included under `data/` in the repository, running `analysis.ipynb` will recreate them.
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
If package conflicts or installation issues occur, try the full dependency list instead:
```
pip install -r requirements_full.txt
```
2. Open `analysis.ipynb`
3. Activate the appropriate Python environment
4. Run `analysis.ipynb` cells sequentially
- Helpful keys are:
    - command/ctrl + enter (run the current cell and stay at the current cell)
    - shift + enter (run the current cell and go to the next cell)

## Further Use of This Repository
This text analysis pipeline can be adapted for other types of free-response data involving natural language processing, exploratory analysis, and topic modeling. The present analysis may also be extended to visual perception research not only on scenes, but also on other subjects.