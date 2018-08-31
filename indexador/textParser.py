# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from string import punctuation

class TextParser():
    
    @classmethod 
    def parser(cls, sentence):
       parsed_sentence = sentence
       parsed_sentence = cls.lower_case(parsed_sentence)
       parsed_sentence = cls.tokenize(parsed_sentence)
       parsed_sentence = cls.remove_stop_words(parsed_sentence)
       parsed_sentence = cls.stemming_words(parsed_sentence)          
    
       return parsed_sentence
    
    @staticmethod 
    def lower_case(sentence):
        return sentence.lower()
     
    @staticmethod    
    def tokenize(sentence):
        return nltk.tokenize.word_tokenize(sentence)
    
    @staticmethod
    def remove_stop_words(sentence):
        stop_words = set(stopwords.words('english')  + list(punctuation) )
        word_tokens = sentence
        
        return [w for w in word_tokens if not w in stop_words if not w.isdigit()]        
            
    @staticmethod
    def stemming_words(sentence):
        pstemmer = PorterStemmer()
        sstemmer = SnowballStemmer('english')
    
        return [sstemmer.stem(pstemmer.stem(w)) for w in sentence]
    
    @staticmethod
    def freq_dist(sentence):
        return nltk.FreqDist(sentence)   