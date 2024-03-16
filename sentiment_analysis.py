'''This module creates a program that compares the sentiment of customer reviews.
It uses SpaCyTextBlob to print polarity and sentiment scores. 
It chooses a sample of 3 reviews to test the accuracy of the predicted sentiment score'''


'''Start
1. import spacy and load the small language model, import pandas, install spacytextblob
2. read the csv file into a pandas data frame
3. remove stop words, change to lowercase, covert to string and strip of extra symbols etc
4. remove nan values from the reviews column
5. create a function input product review, predict the sentiment using spacy/textblob
6. test the function to verify accuracy
7. use polarity and sentiment from textblob to compare and analyse the reviews
8. write a report
End'''


# import spacy and the small language model to tokenise the reviews
import spacy
nlp = spacy.load('en_core_web_sm')


# import pandas to read the csv file
# import spacytextblob to predict the sentiment
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob


# read in the csv file into a data frame and rename the reviews column as review_text so that
# I can refer to it easily as the text that I am analysing
reviews_df = pd.read_csv ('Consumer Reviews of Amazon products.csv')
reviews_df.dropna()
reviews_df = reviews_df.rename(columns={'reviews.text':'review_text'})


# choose only the text column and convert it to string to be able to use string methods
reviews_df['review_text']= reviews_df['review_text'].astype('string')
reviews = reviews_df


# change the strings to all lowercase and strip of any unwanted symbols
reviews['review_text'].str.lower().str.strip()


# choose a sample of the data frame and print out the review_text column to check 
reviews = reviews.sample(n=100, replace = False)
print(reviews['review_text'])


# function to tokenise the text in the data frame and remove the stop words
def tokenize_remove_stopwords(text):
    doc = nlp(text)
    tokens_no_stopwords = [token.text for token in doc if not token.is_stop]
    return tokens_no_stopwords


reviews['tokenized_text'] = reviews['review_text'].apply(lambda x:tokenize_remove_stopwords(x))
reviews = reviews['tokenized_text']


# ensure that the type is a string so that spacy features can be used on the reviews
reviews = reviews.astype('string')


# add new pipeline to use the polarity and sentiment features of spacy
nlp.add_pipe('spacytextblob')


# function to iterate through the reviews and add the polarity score and sentiment score to predict the sentiment of each review
def sentiment_review(reviews):
    polarity_sentiment = []

    for text in reviews:
        doc = nlp(text)
        polarity = doc._.blob.polarity
        polarity_sentiment.append(polarity)
        sentiment = doc._.blob.sentiment
        polarity_sentiment.append(sentiment)
        
            
    print(polarity_sentiment)


# call the function on the sample of reviews to test the function
sentiment_review(reviews)


# choose 3 reviews from the sample to predict the sentiment for to test accuracy
my_review_1 = reviews.iloc[0]
my_review_2 = reviews.iloc[50]
my_review_3 = reviews.iloc[75]


# print the reviews chosen to evaluate scores against
print (f'''{my_review_1},
{my_review_2},
{my_review_3}''')


# put chosen reviews into one variable to use as a parameter for the function
compare_reviews = my_review_1,my_review_2,my_review_3


# call the function on the 3 chosen reviews
sentiment_review(compare_reviews)


