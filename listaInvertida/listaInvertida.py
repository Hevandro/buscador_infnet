# -*- coding: utf-8 -*-

from indexador.textParser import TextParser
from util.logger import logger

class ListaInvertida():
    log_path = '.\\logs\\lista_invertida.log'
    
    def __init__(self):
        self.inverted_list = {}
    
    @logger(log_path=log_path)
    def cria_lista(self,docs):      
        idx = {}
        
        for doc in docs:
            sentence = docs[doc]
            
            parsed_sentence = TextParser.parser(sentence)
            tokens_dict = TextParser.freq_dist(parsed_sentence)            
                 
            for key, value in zip(tokens_dict.keys(),tokens_dict.values()):
                if key in idx.keys():                    
                    idx[key] = idx[key] + [doc.strip()]*value
                else:
                    idx[key] = [] 
                    idx[key] = [doc.strip()]*value
                    
            self.inverted_list = idx   