#Text Data Preprocessing Lib
import json
import nltk
from nltk.stem 
import PorterStemmer
import json
import numpy as np
import pickle



# function for appending stem words

words =[]
classes =[]
ignore_words =['?', '!',',','.', "'s", "'m"]
word_tags_list =[]
train_data_file =[open('intents.json').read()]
intents = json.loads(train_data_file)

def get_stem_words(words, ignore_words):
        stem_words = []
        for word in words:
                if word not in ignore_words:
                        w = stemmer.stem(word.lower())
                        stem_words.append()
        return stem_words
for intent in intents['intents']:
        for pattern in intent['patterns']:
                pattern_word =nltk.word_tokenize(pattern)
                words.extend(pattern_word)
                word_tags_list.append((pattern_word, intent['tag']))
        if intent['tag' not in classes]:
                classes.append(intent['tag'])
                stem_words=get_stem_words(words,ignore_words)

def create_bot_corpus(stem_words, classes):
        stem_words = sorted(list(set(stem_words)))
        classes = sorted(list(set(classes)))
        pickle.dump(stem_words, open('words.pkl','wb'))
        pickle.dump(classes, open('words.pkl','wb'))


    
        # Add all words of patterns to list
        
        # Add all tags to the classes list
         

#Create word corpus for chatbot

