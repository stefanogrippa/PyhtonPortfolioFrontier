# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# http://tesi.luiss.it/25592/1/214651_LORETI_LORENZO.pdf

#import pip
#pip.main(['install', 'pandas_datareader'])

import pandas_datareader.data as web
nome_titoli=["QQQ", "FTSE", "FCA.MI"]
data_inizio='2019-9-14'
data_fine='2020-9-14'
print('inizio caricamento')
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
indice = 0
#lunghezza = len(nome_titoli)

init_notebook_mode(connected=True)
cf.go_offline()


for titolo in nome_titoli:
    # MAMMA
    try:
        dataframe=web.get_data_yahoo(titolo, data_inizio, data_fine, interval='d')
    except:
        print ('titolo non trovato:' + titolo)
        continue
    print(titolo,dataframe.shape)
    print(titolo + 'last' ,dataframe.tail())
    print('fine caricamento')


    quotazioni=dataframe.values
    lista_chiusura=quotazioni[:,5]
    lista_rendimenti=np.array([])
    i=0
    lunghezza=lista_chiusura.size
    indice += 1
    returns = dataframe['Close'].pct_change()
    ((1 + returns).cumprod() - 1).plot(title= titolo + ' Cumulative Returns')
    #dataframe.plot(title= titolo + 'Adj. Closing Price')
    #dataframe.set_index('Date')['Adj'].plot()
    #dataframe.plot(x='Date',y='Close')
    plt.show()
    nomefilegrafico = titolo + '.jpg';
    plt.savefig(nomefilegrafico);

#https://michaelsaruggia.com/data-visualization-plotly/

#init_notebook_mode(connected=True)
#cf.go_offline()
#for titolo in enumerate(nome_titoli):
#data.head();



# Prepare the data
#x = np.linspace(0, 10, 100)

# Plot the data
#plt.plot(x, x, label='linear')

# Add a legend
#plt.legend()

# Show the plot
#plt.show()
#data.iplot(x=mioViettorex,y=mioVettorey,mode='lines+markers')



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
