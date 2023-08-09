import pandas as pd
import requests
from datetime import datetime
from decouple import config
from pathlib import Path

# link do open_weather: https://openweathermap.org/

api_secret = config('API_KEY')



def requisita_tempo(nome_da_cidade):
    
    print('-----------------------------')
    print('-Começando extração de dados-')
    print('-----------------------------')

    link = f'https://api.openweathermap.org/data/2.5/forecast?q={nome_da_cidade}&appid={api_secret}&lang=pt_br'
    requisicao = requests.get(link, verify=False)

    if requisicao.status_code == 200:
        requisicao_dic = requisicao.json()
        
        for i in range(requisicao_dic['cnt']):
            dados_cidade = [{
                'pais': requisicao_dic['city']['country'],
                'cidade': requisicao_dic['city']['name'],
                'temperatura': requisicao_dic['list'][i]['main']['temp'] - 273.15,
                'temperatura_min': requisicao_dic['list'][i]['main']['temp_min'] - 273.15,
                'temperatura_max': requisicao_dic['list'][i]['main']['temp_max'] - 273.15,
                'descricao': requisicao_dic['list'][i]['weather'][0]['description'],
                'data_requisicao': datetime.now().strftime('%y%m%d')             
            }]
            cidade_df = pd.DataFrame(dados_cidade)
            cidade_df.to_csv('sharknado/hist/cities_weather_req.csv', mode='a', index=False, header=False)        
    else:
        print('Algo deu errado.\r\nStatus code: %s' % requisicao.status_code)
        print('Você pode saber mais sobre o erro em: https://www.google.com.br/search?q=http+status+code+%s' % requisicao.status_code)



print(requisita_tempo('recife'))

# descricao = requisicao_dic['weather'][0]['description']
# temperatura = int(requisicao_dic['main']['temp'] - 273.15)
# temperatura_min = int(requisicao_dic['main']['temp_min'] - 273.15)
# temperatura_max = int(requisicao_dic['main']['temp_max'] - 273.15)
# #print(requisicao_dic)
# print(requisicao_dic['sys']['country'])
# print(str(requisicao_dic['coord']['lon']) + ' ' + str(requisicao_dic['coord']['lat']))
# print(requisicao_dic['name'])
# print(requisicao_dic['weather'][0]['description'])
# print('Temperatura ' + str(temperatura) + 'º')
# print('Temperatura mínima ' + str(temperatura_min) + 'º')
# print('Temperatura máxima ' + str(temperatura_max) + 'º')
