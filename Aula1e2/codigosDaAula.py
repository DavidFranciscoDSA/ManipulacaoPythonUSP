# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:10:47 2024

@author: david - 

Aula 1 - Manipulação de dados com Python

"""
#Instalando as bibliotecas necessárias
#%%
#!pip install pandas
#!pip install numpy
#!pip install matplotlib
#!pip install plotly
#!pip install seaborn
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
cidades = {"Cidades": ['Bebedouro', 'Ribeirao Preto', 'Caraguatatuba', 'Americana','Itapoa'],
           "DistanciaSP": [381, 308, 200, 125, 1102],
           "nHabitantes": [79856, 719350, 129121, 278954, 32154]}
cidades = pd.DataFrame(cidades)
#%%

#IF, ELIF e ELSE
#%%
for index, row in cidades.iterrows():
    distancia = row['DistanciaSP']
    if 300 < distancia <= 1000:
        cidades.loc[index, 'Status'] = 'longe'
    elif distancia <= 300:
        cidades.loc[index, 'Status'] = 'Perto'
    else:
        cidades.loc[index, 'Status'] = 'Muito longe'
#%%

##Importando a base de dados - Excel
#%%
diretorio = r"C:\Users\david\Desktop\ESTUDOS\1-USP\26-Manipulação de dados em Python\ManipulacaoPythonUSP\Aula1e2/"
arquivo = 'receita_empresas.xlsx'
receitas = pd.read_excel(diretorio+arquivo)
#%%

#
#%%
receitas.describe()
#%%

#Importando a base de dados csv
#%%
notas_pisa = pd.read_csv(diretorio+'notas_pisa.csv', sep=',', decimal='.')
#%%

#Importando a base de dados de uma API
#%%
dataInicial = '01/01/2021'
dataFinal = '01/05/2024'
filtro = f'&dataInicial={dataInicial}&dataFinal={dataFinal}'
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv'+filtro
ipca = pd.read_csv(url, sep=';', decimal=',')
#%%

#Salvando o arquivo IPCA baixado, para o computador é feito após tratamento se necessário
#%%
ipca.to_excel('ipca.xlsx', index = False)
#%%

#Lista + append + função + For
#%%
numeros = [1,2,3,4,5,6]
lista_vazia = []
def triplicar(x):
    for i in range(len(numeros)):
        num = numeros[i] * 3
        lista_vazia.append(num)
    return lista_vazia

triplicar(numeros)

#%%

#Processo de capitalização
#%%
saldo_investimento = 80000
lista_investimento = []
while saldo_investimento < 120000:
    saldo_investimento = (saldo_investimento*1.008)
    lista_investimento.append(saldo_investimento)
    
print(lista_investimento)

# index, valor inicial
lista_investimento.insert(0, 80000)
#%%

#--------------------------- MANIPULAÇÂO DE DADOS ----------------------------------
#%%
import pandas as pd
import numpy as np
#%%

#Importando a base de dados csv
#%%
diretorio = r"C:\Users\david\Desktop\ESTUDOS\1-USP\26-Manipulação de dados em Python\ManipulacaoPythonUSP\Aula1e2/"
pisa = pd.read_csv(diretorio+'notas_pisa.csv', sep=',', decimal='.')
#%%

#Observando os dados
pisa.head(10)

#Verificando as colunas existentes
pisa.columns

#Verificando os tipos das variaveis
pisa.dtypes

#informações
pisa.info()

#Numero de linhas e colunas
print('Linhas',pisa.shape[0])
print('Colunas',pisa.shape[1])

#Selecionando colunas
paises = pisa.country  #ou pisa['country'] 
print(paises)

#selecionando as colunas que queremos
pisa2018Math = pisa[['country', 'mathematics_2018']]

#Excluindo colunas
pisa_2022 = pisa.drop(columns=['mathematics_2018', 'reading_2018', 'science_2018'])

pisa_2022.drop(columns=['group'], inplace=True)

#Removendo objeto do ambiente
del pisa2018Math

# encontrando posiçoes especificas coluna 2
print(pisa_2022.iloc[46,2])

# encontrando posiçoes especificas todas as colunas
print(pisa_2022.iloc[46,])

# encontrando todas as colunas das 7 primeiras colocações
print(pisa_2022.iloc[0:7,])

# Todas as linhas, colunas especificas 
print(pisa.iloc[:,[0,2,5]])

# Todas as linhas, colunas 0 a 2 excluindo o ultimo valor(2)
print(pisa.iloc[:,0:2])

#Ajustando colunas
pisa_ajuste = pisa.reindex([ 'group', 'country', 'science_2022', 'mathematics_2022', 'reading_2022'],axis=1)

#Não vamos analizar os partners 38:96
pisa_OECD = pisa.drop(pisa.index[38:96])
pisa_Partners = pisa.drop(pisa.index[0:38])

#---------------- AULA 3 - Ultima Aula Do Curso --------------------------------------

# Convertendo as colunas notas que estão como objects para numeric - coerce (elementos faltantes)
#%%
pisa['mathematics_2022'] = pd.to_numeric(pisa['mathematics_2022'] , errors='coerce')
pisa['reading_2022'] = pd.to_numeric(pisa['reading_2022'] , errors='coerce')
pisa['science_2022'] = pd.to_numeric(pisa['science_2022'] , errors='coerce')
pisa['mathematics_2018'] = pd.to_numeric(pisa['mathematics_2018'] , errors='coerce')
pisa['reading_2018'] = pd.to_numeric(pisa['reading_2018'] , errors='coerce')
pisa['science_2018'] = pd.to_numeric(pisa['science_2018'] , errors='coerce')
#%%
pisa.dtypes

#Excluindo valores faltantes NaN
#%%
pisa_na = pisa.dropna()
#%%

#------------------- Gerando estatísticas descritivas -------------------------
#numericas
#%%
pisa_na[['mathematics_2018', 'reading_2018', 'science_2018']].describe()
pisa_na[['mathematics_2022', 'reading_2022', 'science_2022']].describe()
#%%

#categoricas - tabela de frequencia
#%%
pisa_na['group'].value_counts()
#%%

# Fitros 
acimaMediaMath18 = pisa_na[pisa_na['mathematics_2018'] > 457]
apenas_OECD = pisa_na[pisa_na['group'] == 'OECD']
Partiner_acimaMediaMath18 = (pisa_na[(pisa_na['mathematics_2018'] > 457) & (pisa_na['group'] == 'PARTNERS')])

#Menores notas de leitura
menoresLeitura2022 = (pisa_na[(pisa_na['reading_2018'] < 412) & (pisa_na['reading_2022'] < 404)])

#Groupby
pisa_grupo = pisa_na.groupby(by=['group'])
pisa_grupo.describe().T

#Ordem crescente
math_crescente = pisa_na.sort_values(by=['mathematics_2018'], ascending = True)

#Ordem Decrescente
math_decrescente = pisa_na.sort_values(by=['mathematics_2022'], ascending = False)

#Alterando nome das variaveis - mesma ordem da original
novas_colunas = ['Pais', 
                 'Grupo',
                 'Matematica2022',
                 'Leitura2022',
                 'Ciencia2022',
                 'Matematica2018',
                 'Leitura2018',
                 'Ciencia2018']

pisa_na.columns=novas_colunas

#Trocando pela posição da coluna
pisa_na.columns.array[1] = 'Grupo_paises'


#-----------------------  Visualização de Dados -------------------------------
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
import plotly.graph_objects as go

comercio = pd.read_excel('comercio_global.xlsx')

#Grafico de barras - usado para variaveis qualitativas - basico
sns.countplot(data=comercio, x='market')

#Grafico de barras - usado para variaveis qualitativas - com parametros
sns.countplot(data=comercio, x='market', order=['APAC','LATAM','US','EU','EMEA','Africa','Canada'])

#Grafico de barras - usado para variaveis qualitativas - com parametros e camadas de formatação
sns.countplot(data=comercio, x='market', order=['APAC','LATAM','US','EU','EMEA','Africa','Canada'])
