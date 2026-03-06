# scene-study-text-analysis-2026 / Final Project Plan

## 1. Project Description

This project intends to develop a Jupyter notebook that implements a data analysis pipeline for a scene perception study. In the experiment, participants will view outdoor scene images from the SUN397 dataset and provide six spontaneous text impressions for each image/trial. The goal of the Jupyter notebook is to analyze this written response to identify what type of conceptual domains people use when perceiving scenes.

The analysis will focus on organizing, cleaning, and processing the collected text response. After cleaning the data, the project will investigate word usage/occurrence patterns and perform topic modeling to extract several domains around which the words cluster.

## 2. Functions

### a. clean_data
a will include lowercasing, punctuation removal, trailing whitespace, and grammar check. 

### b. compute_word_frequency
b will include splitting the string into words and creating an output of a word frequency table, which lists all words from the highest to lowest frequency.
The words with high frequency but are meaningless analysis-wise, such as "scene" or "environment," may be removed at this stage. 

### c. perform_topic_modeling
c will identify where words cluster based on their occurrence, relevance in meaning, etc. The exact method (e.g., SBERT, LDA) will be determined soon, but the goal is to detect patterns in how participants describe scenes. I may create multiple functions for the topic modeling.
