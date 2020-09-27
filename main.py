# http://tesi.luiss.it/25592/1/214651_LORETI_LORENZO.pdf

# import pip
# pip.main(['install', 'pandas_datareader'])
import traceback

import pandas_datareader.data as web
import json
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import init_notebook_mode
import cufflinks as cf


class ScritturaDati:
    def __init__(self, nomemiofile):
        self.nomefile = nomemiofile

    def riempitabella(self):
        data['people'] = []
        data['people'].append({
            'name': 'QQQ',
            'website': '',
            'from': ''
        })
        data['people'].append({
            'name': 'FCA.MI',
            'website': '',
            'from': ''
        })
        data['people'].append({
            'name': 'L100.L',
            'website': '',
            'from': ''
        })

        with open(self.nomefile, 'w') as outfile:
            json.dump(data, outfile)


with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')


for p in data['people']:
    print('titolo da file di testo=' + p['name'])

data_inizio = '2019-9-14'
data_fine = '2020-9-14'
print('inizio caricamento')

init_notebook_mode(connected=True)
cf.go_offline()


for p in data['people']:
    print('titolo da vettore=' + p['name'])
    ticker = p['name']
    try:
        data = web.DataReader(ticker, 'iex', data_inizio, data_fine)
        data.index = web.to_datetime(data.index)

        data = web.get_data_yahoo(ticker, data_inizio, data_fine, interval='d')
    except:
        print ('titolo non trovato su iex:' + p['name'])
        try:
            data = web.get_data_yahoo(ticker, data_inizio, data_fine, interval='d')
        except:
            print('titolo non trovato su yahoo:' + p['name'] + ':' + traceback.format_exc())
            continue
    nomefilecsv = p['name'] + 'storico.csv'
    # dataframe.tocsv(nomefilecsv)
    print(p['name'], data.shape)
    print(p['name'] + 'last', data.tail())
    print('fine caricamento')

    quotazioni = data.values
    lista_chiusura = quotazioni[:, 5]
    lista_rendimenti = np.array([])

    lunghezza = lista_chiusura.size

    quotaChiusura = data['Close']
    quotaChiusura.plot(title=p['name'] + ' quota')
    # returns = dataframe['Close'].pct_change()
    # ((1 + returns).cumprod() - 1).plot(title= titolo + ' Cumulative Returns')
    # dataframe.plot(title= titolo + 'Adj. Closing Price')
    # dataframe.set_index('Date')['Adj'].plot()
    # dataframe.plot(x='Date',y='Close')
    plt.show()
    nomefilegrafico = p['name'] + '.jpg'
    plt.savefig(nomefilegrafico)

# https://michaelsaruggia.com/data-visualization-plotly/

# init_notebook_mode(connected=True)
# cf.go_offline()
# for titolo in enumerate(nome_titoli):
# data.head();

# Prepare the data
# x = np.linspace(0, 10, 100)

# Plot the data
# plt.plot(x, x, label='linear')

# Add a legend
# plt.legend()

# Show the plot
# plt.show()
# data.iplot(x=mioViettorex,y=mioVettorey,mode='lines+markers')

# while(i < lunghezza - 1):
#    rendimento = np.log(lista_chiusura[i+1]/lista_chiusura[i])
#    lista_rendimenti = np.append(lista_rendimenti, [rendimento])
#    i = i + 1

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
