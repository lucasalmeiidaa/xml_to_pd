#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xmltodict
import pandas as pd
from os.path import join
from os import listdir
import numpy as np
# with open('bases/13190504501136000136550010009435231024529034_9e11f85798f4e4bc8e8425a2274a217b866de706.xml') as fd:
#     doc = xmltodict.parse(fd.read())


# In[2]:


def busca_xml():
    lst_dados = []
    for nf in doc['nfeProc']['NFe']['infNFe']['det']:
        lst_aux = []
        try:
            cod_prod = nf['prod']['cProd']
        except:
            cod_prod = np.nan
        try:
            desc_prod = nf['prod']['xProd']
        except:
            desc_prod = np.nan
        try:
            nom = nf['prod']['NCM']
        except:
            nom = np.nan
        try:
            tipo = nf['prod']['uCom']
        except:
            tipo = np.nan
        try:    
            qtd = nf['prod']['qCom']
        except:
            qtd = np.nan
        try:
            valor_unit = nf['prod']['vUnCom']
        except:
            valor_unit = np.nan
        try:
            valor_total = nf['prod']['vProd']
        except:
            valor_total = np.nan
        try:
            desc_total = nf['prod']['vDesc']
        except:
            desc_total = np.nan
            
        lst_aux.append(cod_prod)
        lst_aux.append(desc_prod)
        lst_aux.append(nom)
        lst_aux.append(tipo)
        lst_aux.append(qtd)
        lst_aux.append(valor_unit)
        lst_aux.append(valor_total)
        lst_aux.append(desc_total)
        lst_dados.append(lst_aux)
    
    df = pd.DataFrame(data=lst_dados, columns=['cod_produto', 'descricao_prod', 
                                     'nomenclatura', 'tipo', 'quantidade', 
                                     'valor_unit', 'valor_total',
                                     'desc_total'])
    
    return df


# In[3]:


path_xml = 'bases'

files_xml = []

for file in listdir(path_xml):
    files_xml.append(file)


# In[5]:


for file in files_xml:
    # Abrindo xml
    with open(join(path_xml, file)) as fd:
        doc = xmltodict.parse(fd.read())
    
    df = busca_xml()
    # Transformando colunas em float
    df['desc_total'] = df['desc_total'].astype(float)
    df['quantidade'] = df['quantidade'].astype(float)
    df['valor_total'] = df['valor_total'].astype(float)
    
    # Fazendo operações de cálculo
    df['Coluna1'] = df['desc_total'] / df['quantidade']
    df['Coluna2'] = df['valor_total'] - df['desc_total']
    
    # Exportando para excel
    df.to_excel("{}.xlsx".format(file), index=False)

