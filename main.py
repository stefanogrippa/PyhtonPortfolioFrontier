# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# http://tesi.luiss.it/25592/1/214651_LORETI_LORENZO.pdf

import pip
pip.main(['install', 'pandas_datareader'])

import pandas_datareader.data as web
nome_titoli=["QQQ", "BP"]
data_inizio='2015-9-3'
data_fine='2020-9-3'
print('inizio caricamento')
import numpy as np
#import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
indice = 0
#lunghezza = len(nome_titoli)
for titolo in nome_titoli:
    # MAMMA
    data=web.get_data_yahoo(titolo, data_inizio, data_fine, interval='d')
    print(titolo,data.shape)
    #print(titolo + 'last' ,data.tail())
    print('fine caricamento')


    quotazioni=data.values
    lista_chiusura=quotazioni[:,5]
    lista_rendimenti=np.array([])
    i=0
    lunghezza=lista_chiusura.size
    indice += 1

#https://michaelsaruggia.com/data-visualization-plotly/

init_notebook_mode(connected=True)
cf.go_offline()
#for titolo in enumerate(nome_titoli):
#data.head();
mioVettorex = range(0,10)
mioVettorey = np.linspace(-np.pi, np.pi, 10)
data.iplot(x=mioVettore.,y=mioVettorey,mode='lines+markers')



while(i < lunghezza - 1):
    rendimento = np.log(lista_chiusura[i+1]/lista_chiusura[i])
    lista_rendimenti = np.append(lista_rendimenti, [rendimento])
    i = i + 1

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
