# This script is designed to perform a word frequency analysis after cleaning the responses. 


#imports

import pandas as pd
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer



#load cleaned data
clean_data_path = Path(__file__).resolve().parent.parent / "data" / "clean.csv"
cleaned_data = pd.read_csv(clean_data_path)



### Calcualte word frequency

#vectorizer
vectorizer = CountVectorizer(
    stop_words="english",
    max_df=0.95,
    min_df=5,
    ngram_range=(1, 2)
)


texts = cleaned_data["clean_text"].dropna().tolist()

x = vectorizer.fit_transform(texts)

#counts
word_counts = np.asarray(X.sum(axis=0)).ravel()
feature_names = vectorizer.get_feature_names_out()

#dataframe
freq_df = pd.DataFrame({
    "word": feature_names,
    "count": word_counts
})

freq_df = freq_df.sort_values("count", ascending=False)


#check by printing the most frequent 30 words
print(freq_df.head(30))


#save the word freqneucy list to a csv file

output_path = Path(__file__).resolve().parent.parent / "data" / "most_frequent_words.csv"
freq_df.to_csv(output_path, index=False)

