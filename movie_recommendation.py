'''
Start
1. Read in text file 
2. Write function to compare film with text file'''

import spacy
nlp = spacy.load('en_core_web_md')

with open('movies.txt', 'r')as file:
    movies = file.read()
    print(movies)

def tokenize(text):
    doc = nlp(text)
    return ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

def get_doc(text):
    return nlp(text)
        

movies['processed_overview'] = movies[](tokenize)
movies['doc'] = movies['processed_overview'].apply(get_doc)



