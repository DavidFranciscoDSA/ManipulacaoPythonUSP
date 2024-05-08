# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:10:47 2024

@author: david - 

Aula 1 - Manipulação de dados com Python

"""
#Instalando as bibliotecas necessárias
#%%
!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install plotly
!pip install seaborn
#%%

#Importando as bibliotecas
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly as ptl
#%%

#Series com pandas
#%%
nomes = ['David','Ana','Fernanda']
idades = [44,11,38]
peso = [85,32,55]
pessoas = pd.Series([nomes,idades,peso])
pessoasdf = pd.DataFrame([nomes,idades,peso])
#%%
# [linha][coluna]
#%%
pessoas[2][2]
#%%

#Imprimindo todos os elementos do data frame
#%%
for i in range(len(pessoasdf)):
    print(20*'-*')
    for j in range(len(pessoasdf)):
        colunas = ['Nome: ','Idade: ','Peso: ']
        print(f'{colunas[j]}\t{pessoasdf[i][j]}\tTipo: {type(pessoasdf[i][j])}')
print(20*'-*')
#%%

#Dicionario
#%%
cidades = {"Cidades": ['Bebedouro', 'Ribeirao Preto', 'Caraguatatuba', 'Americana'],
           "DistanciaSP": [381, 308, 200, 125],
           "nHabitantes": [79856, 719350, 129121, 278954]}
cidades = pd.DataFrame(cidades)
#%%

##Importando a base de dados - Excel
#%%
diretorio = r"C:\Users\david\Desktop\ESTUDOS\1-USP\26-Manipulação de dados em Python\ManipulacaoPythonUSP\Aula1/"
arquivo = 'receita_empresas.xlsx'
df = pd.read_excel(diretorio+arquivo)
#%%

#
#%%
df.describe()
#%%

#Importando a base de dados csv
#%%
notas_pisa = pd.read_csv(diretorio+'notas_pisa.csv', sep=',', decimal='.')
#%%

#Importando a base de dados de uma API
#%%
dataInicial = '01/01/2021'
dataFinal = '01/01/2024'
filtro = f'&dataInicial={dataInicial}&dataFinal={dataFinal}'
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv'+filtro
ipca = pd.read_csv(url, sep=';', decimal=',')
#%%

