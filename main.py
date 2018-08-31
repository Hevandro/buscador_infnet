# -*- coding: utf-8 -*-

from util.database import Database
from listaInvertida.listaInvertida import ListaInvertida
from indexador.indexador import Indexador

if __name__ == "__main__":
      
    # Lê os arquivos XML
    db = Database()  
    f = db.readXML('.\data\\cf74.xml')
    
    #Total de documentos
    len_docs = len(f)
    
    # Cria lista invertida
    li = ListaInvertida()
    li.cria_lista(f)       
    
    # Grava a lista invertida em disco
    Database.write_to_disk(li.inverted_list, '.\data\\lista_invertida.json')
    
    idx = Indexador()
    m = idx.create_term_matrix(li.inverted_list)
    
    # Chama o indexador
    #term_idf = Indexador.calc_idf(li, len_docs)
    #Database.write_to_disk(term_idf)