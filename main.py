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
import datetime


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

nomeFileDati = 'data.json'
with open(nomeFileDati) as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')


for p in data['people']:
    print('titolo da file di testo=' + p['name'])


data_inizio = datetime.date.fromordinal(datetime.date.today().toordinal()-365)
str_data_inizio = data_inizio.__str__()
print ("data inizio = " + str_data_inizio)



data_fine = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
str_data_fine = data_fine.__str__()
print ("data fine = " + str_data_fine)
print('inizio caricamento')

init_notebook_mode(connected=True)
cf.go_offline()


for p in data['people']:
    print('titolo da vettore=' + p['name'])
    ticker = p['name']
    try:
        data = web.get_data_yahoo(ticker, str_data_inizio, str_data_fine, interval='d')
        # data.index = web.to_datetime(data.index)
    except:
        print('titolo non trovato su yahoo:' + p['name'])
        # try:
        #    data = web.get_data_yahoo(ticker, data_inizio, data_fine)
        # except:
        print(traceback.format_exc())
        continue
    nomefilecsv = p['name'] + '_storico.csv'
    data.to_csv(nomefilecsv)
    print(data.info)
    print(p['name'], data.shape)
    print(p['name'] + 'last', data.tail())
    print('fine caricamento')

    quotazioni = data.values
    lista_chiusura = quotazioni[:, 5]
    lista_rendimenti = np.array([])

    lunghezza = lista_chiusura.size

    quotaChiusura = data['Close']
    quotaChiusura.plot(title= p['from'] + ' quota')
    # returns = dataframe['Close'].pct_change()
    # ((1 + returns).cumprod() - 1).plot(title= titolo + ' Cumulative Returns')
    # dataframe.plot(title= titolo + 'Adj. Closing Price')
    # dataframe.set_index('Date')['Adj'].plot()
    # dataframe.plot(x='Date',y='Close')
    plt.plot()
    plt.show()
    nomefilegrafico = p['name'] +  '.jpg'
    plt.savefig(nomefilegrafico)


#plt.show()
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
