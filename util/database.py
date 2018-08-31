# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:57:24 2018

@author: hevandro.veiga
@author: renata.santos
"""

import json
import pandas as pd
from xml.dom.minidom import parse

from util.logger import logger

class Database():
    log_path = '.\\logs\\database.log'
    
    @logger(log_path)
    def read_from_disk(self):
        if self.db[-3:] == 'csv':                
            return pd.read_csv(self.db, index_col=0)
        else:
            with open(self.db, 'r') as read_file:
                return json.load(read_file)

    @staticmethod  
    @logger(log_path)
    def write_to_disk(data, filename):
        if isinstance(data, pd.DataFrame):
            pass
            #data.to_csv(db)
        else:            
            with open(filename, 'w') as file:
                json.dump(data, file, sort_keys=True, indent=4)

    @staticmethod
    @logger(log_path)
    def readXML(filename):
        #invIndGen.info('Reading '+filename+' file')
        
        dictionary = {}
        DOMTree = parse(filename)
        collection = DOMTree.documentElement
        
        records = collection.getElementsByTagName("RECORD")
        
        for record in records:
            recordNumber = record.getElementsByTagName('RECORDNUM')[0].childNodes[0].data
            
            try:
                dictionary[recordNumber] = record.getElementsByTagName('ABSTRACT')[0].childNodes[0].data
            except IndexError:
                try:
                    dictionary[recordNumber] = record.getElementsByTagName('EXTRACT')[0].childNodes[0].data
                except IndexError:
                    pass
                    #invIndGen.warning("Document["+recordNumber+"] doesn't have abstract neither extract!")
        
        #invIndGen.info('%s records read succesfully.' % str(len(dictionary)))
        return dictionary