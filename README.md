# scene-study-text-analysis-2026 / Final Project Check-in #3

## Abstract
When we look at a scene, we rapidly and automatically extract a wealth of information from it, including its “gist” writ large (e.g., categorizing the scene as a kitchen vs. a beach). However, while much work has been done to characterize how we recognize scenes, little has been done to understand how we evaluate scenes in terms of the impressions they evoke in us. The current study investigates the impressions people form when viewing photographs of outdoor environments, focusing on the words they naturally generate. By analyzing the text responses participants provide under unspeeded scene viewing, this study aims to uncover the key dimensions people use when evaluating scenes. One hundred adults, to be recruited from SONA and Prolific, will view 10 images (one at a time) and provide at least six short descriptions of characteristics that come to mind when viewing each image. Written responses will be analyzed by identifying recurring patterns in word use, such as co-occurrence. These patterns are expected to reveal the conceptual domains that underlie scene perception – for example, whether a place is perceived as safe (safety), pleasant (valence), or visually appealing (aesthetics). By characterizing these representations, this study will contribute to our understanding of how people interpret and interact with complex visual environments. More broadly, it will demonstrate how analyzing free-response language can provide insight into the structure of human scene perception.

_Keywords: scene perception; scene evaluation; visual perception; natural language processing; scene understanding_

## How to run the analysis pipeline

pip install -r requirements.txt


## Project logic & motivation 
This project aims to understand which conceptual domains people spontaneously rely on when perceiving visual scenes, addressing a gap in prior research that has focused mainly on predefined categories in scene perception/categorization. By analyzing free-response language, this study intends to implement a data-driven approach to understand the underlying structure of scene perception and mental representations.

## Input data format or requirements
The input data consists of written responses from participants. The participants will be asked to spontaneously generate six short text impressions for each presented scene image, and their entries will be structured in a CSV file with six respective columns, besides other columns that include other necessary information, such as participant ID, image ID, response time, etc. 

## Example use cases
The text analysis pipeline that I intend to create for the final project can be used to analyze other kinds of free-response data for data cleaning and topic modeling (i.e., identifying recurring semantic domains) purposes. We can extend the pipeline to visual perception experiments that investigate not only scenes but also other subjects.

## Python Script Files & Test Plan
Currently, this repository contains two main directories: 1) data/ folder, which stores raw and processed datasets in a .csv format and 2) src/ folder, which stores Python scripts for data analysis. 

So far, src/ folder has a pipeline up to word frequency analysis. The clean_text.py preprocesses raw responses, including extracting text from dictionary-formatted entries, lowercasing, and removing punctuation. Then, the word_frequency.py takes over the cleaned data to compute word frequency using vectorization.

In the next step, the scripts will be reorganized into a more structured project directory structure, and new scripts for analysis will be implemented. 

Specifically, the pipeline will be extended to include a dictionary-based content analysis framework used in Nicholas, Uddenberg, and Todorov (2025), as I plan to refer to their R code recorded in [OSF](https://osf.io/pmtxw/overview?view_only=a485688056a8495ba37082f38c690833). After performing the word frequency analysis, the responses will be mapped onto a high-dimensional taxonomy of semantic content, which will allow the computation of key metrics such as coverage, prevalence, and direction, enabling the identification of recurring conceptual domains in scene perception.

## Implementation Plan
The project is structured as an analysis pipeline:

- Data loading (clean_text.py)  
  - Load raw CSV data from the data/ folder  
  - Extract text responses from dictionary-formatted entries  
  - Status: completed  
- Text preprocessing (clean_text.py)  
  - Lowercasing, punctuation removal, whitespace trimming  
  - Output: clean.csv  
  - Status: completed  
- Word frequency analysis (word_frequency.py)  
  - Tokenization and vectorization using CountVectorizer  
  - Output: word_frequency.csv  
  - Status: completed  
- Dictionary-based domain mapping (planned)  
  - Map responses to semantic categories based on Nicolas et al. (2025)  
  - Compute coverage, prevalence, and direction  
  - Status: pending  
- Pipeline integration (main.py, planned)  
  - Combine all steps into a single executable workflow  
  - Status: pending  
