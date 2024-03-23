# Importing libraries 
import spacy # for natural language processing
import pandas as pd # for sentimental analysis

from textblob import TextBlob # for polarity and subjectivity

# Reviewing the dataset
dataframe = pd.read_csv('amazon_product_reviews.csv', usecols=['reviews.text'], nrows =1000)
dataframe.shape
reviews_data = dataframe[['reviews.text']]
reviews_data.head()

# Getting rid of null values
clean_data = dataframe.dropna(subset=['reviews.text'])
reviews_data.isna().sum()
nlp = spacy.load('en_core_web_sm')

# Getting rid of stopwords
def preprocess(data):
    text = data.strip()
    doc = nlp(text)

    processed = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(processed)

# Applying function to dataframe
reviews_data['processed.text'] = reviews_data['reviews.text'].apply(preprocess)

# A view of the top five rows of the data
reviews_data.head()

import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Add SpacyTextBlob extension to the pipeline
nlp.add_pipe("spacytextblob")

# Application process of 'Natural Language Processing' to the text
def spacy_polarity(text):
    doc = nlp(str(text))  # Convert to string
    polarity_value = doc._.polarity
    sentiment_value = doc._.subjectivity
    return polarity_value, sentiment_value

# Use spacy_polarity function to each row in the DataFrame and add new columns for polarity and subjectivity
reviews_data['polarity'], reviews_data['subjectivity'] = zip(*reviews_data['reviews.text'].map(spacy_polarity))

# Results for Polarity and Subjectivity
average_polarity = reviews_data['polarity'].mean()
median_polarity = reviews_data['polarity'].median()
std_dev_polarity = reviews_data['polarity'].std()

average_subjectivity = reviews_data['subjectivity'].mean()
median_subjectivity = reviews_data['subjectivity'].median()
std_dev_subjectivity = reviews_data['subjectivity'].std()

print("Polarity:")
print("Average:", round(average_polarity, 2))
print("Median:", round(median_polarity, 2))
print("Standard Deviation:", round(std_dev_polarity, 2))

print("\nSubjectivity:")
print("Average:", round(average_subjectivity, 2))
print("Median:", round(median_subjectivity, 2))
print("Standard Deviation:", round(std_dev_subjectivity, 2))

# Display the first 10 rows of reviews_data with added polarity and subjectivity columns
reviews_data.head(10)