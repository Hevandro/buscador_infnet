# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from time import time

from indexador.textParser import TextParser
from util.logger import logger

class Indexador():
    log_path = '.\\logs\\indexador.log'
    
    def __init__(self):
        pass
    
    @classmethod
    @logger(log_path)
    def calc_idf(cls, df, len_docs):
        return np.log2(len_docs/(df != 0).sum(1)) 
    
    @staticmethod
    @logger(log_path)
    def calc_tf_idf(df, s):
        return df.mul(s, axis=0)
        
    
    @staticmethod
    @logger(log_path)
    def calc_doc_length(df):
        d = np.power(df, 2)
        d = np.sqrt(d.sum(axis=1))          
        
        return d
    
    #@staticmethod
    @logger(log_path)
    def create_term_matrix(self, lista_invertida):      
        df = pd.DataFrame()
                
        x = []
        for key, value in lista_invertida.items():
            df2 = pd.DataFrame()
            result_fd = TextParser.freq_dist(value)   
           
            data = list(result_fd.values())
            idx = result_fd.keys()
            
            #df2[key] = pd.Series(data, index=idx)
            
            x.append(pd.Series(data, index=idx ))

            #df2[key] = pd.DataFrame(data, index=idx)
        #df = pd.concat([df, df2], axis = 1)
        print(x)
        df = pd.concat(x, axis = 1)
            
        df.fillna(0, inplace=True)
            
        return df
        
        
        # freq dist most_common
        
        #for key, values in lista_invertida.items():
        #    for value in values()
        
#            word_count = len(parsed_sentence)
#            tokens_dict = TextParser.freq_dist(parsed_sentence)   
#            
#            df2 = pd.DataFrame()
#            # Calcula o tf
#            df2[doc] = pd.Series(list(tokens_dict.values()), index=tokens_dict.keys())/word_count 
#            df = pd.concat([df, df2], axis=1)
#            df.fillna(0, inplace=True)
#            
#        self.term_matrix = df  
