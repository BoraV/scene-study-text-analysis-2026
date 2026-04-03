# This script is designed to clean text data from a CSV file. 

#imports

from turtle import save

import pandas as pd
from pathlib import Path
import ast
import string


#load data

data_path = Path(__file__).resolve().parent.parent / "data" / "main_data.csv"
raw_data = pd.read_csv(data_path)

#check
print(raw_data.head())



#select the response column
## can change "responses" to your actual column name
response_column = "responses"

#check if there are any missing values in the response column
print("Missing values:", raw_data[response_column].isna().any())
#If False, there is no NaN



#extract text from the dictionary & strip whitespace
##Now, the function assumes the target key is "Q0". Change "Q0" if your actual key is different.

def extract_and_strip_response(response_string):
    if pd.isna(response_string):
        return ""
    
    response_dict = ast.literal_eval(response_string)
    response_text = response_dict["Q0"]
    response_text = response_text.strip()
    return response_text


#lowercasing
def lowercase_text(text):
    return text.lower()


#remove punctuations

def remove_punctuation(text):
    clean_text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    return clean_text


#run all cleaning functions

def clean_pipeline(df, column):
    return (
        df[column]
        .apply(extract_and_strip_response)
        .apply(lowercase_text)
        .apply(remove_punctuation)
    )



#apply changes to the response column
clean_series = clean_pipeline(raw_data, response_column)

#make a new datafrmame with the cleaned text
clean_df = pd.DataFrame({"clean_text": clean_series})

#save it to the data directory
data_output_path = Path(__file__).resolve().parent.parent / "data" / "clean.csv"
clean_df.to_csv(data_output_path, index=False)



