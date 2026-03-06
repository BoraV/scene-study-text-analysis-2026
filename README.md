# scene-study-text-analysis-2026 / Final Project Plan

## Project Description
This project intends to develop a Jupyter notebook that implements a data analysis pipeline for a scene perception study. In the experiment, participants will view outdoor scene images from the SUN397 dataset and provide six spontaneous text impressions for each image/trial. The goal of the Jupyter notebook is to analyze this written response to identify what type of conceptual domains people use when perceiving scenes.

The analysis will focus on organizing, cleaning, and processing the collected text response. After cleaning the data, the project will investigate word usage/occurrence patterns and perform topic modeling to extract several domains around which the words cluster.

## Functions
### a. clean_data
a will include lowercasing, punctuation removal, trailing whitespace, and grammar check. 

### b. compute_word_frequency
b will include splitting the string into words and creating an output of a word frequency table, which lists all words from the highest to lowest frequency.
The words with high frequency but are meaningless analysis-wise, such as "scene" or "environment," may be removed at this stage. 

### c. perform_topic_modeling
c will identify where words cluster based on their occurrence, relevance in meaning, etc. The exact method (e.g., SBERT, LDA) will be determined soon, but the goal is to detect patterns in how participants describe scenes. I may create multiple functions for the topic modeling.

## Abstract
Humans can rapidly make meaning of visual scenes. Yet, relatively little is known about the domains people rely on when spontaneously perceiving and evaluating scenes. The present study investigates the impressions individuals form when seeing naturalistic and artificial outdoor scenes to understand whether recurring linguistic patterns reveal underlying perceptual criteria. Understanding these perceptual criteria is significant because scene perception plays a central role in everyday cognition, guiding navigation, memory, and decision-making in complex surroundings. Rather than relying on predefined rating scales, this project adopts a data-driven approach that captures participants’ own language during scene perception. Seventy adults, including forty college students**, were recruited from SONA and Prolific will view images of scenes presented one at a time and produce six spontaneous impressions for each image. The responses will be cleaned and analyzed using computational text-analysis techniques, including word-frequency analysis and topic modeling using Principal Component Analysis (PCA)**, to extract latent topics from participants’ answers. Natural language processing will focus on identifying where co-occurring words cluster in the semantic dimension, which will be interpreted as candidate domains guiding scene perception and evaluation. For example, clusters may reflect perceptual dimensions such as aesthetic qualities, environmental features, or emotional responses. By identifying the domains people rely on during scene perception, this study seeks to address what visual aspects we prioritize when evaluating scenes. More broadly, the project contributes to research on visual perception and scene understanding by demonstrating how free-response language can reveal the conceptual structures underlying mental representation of scenes. 

Keywords: scene perception; scene evaluation; visual perception; natural language processing; scene understanding

**Number of participants and PCA are placeholders.
