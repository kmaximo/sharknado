import pandas as pd
import requests
from datetime import datetime
from decouple import config
from pathlib import Path

# link do open_weather: https://openweathermap.org/

api_secret = config('API_KEY')


def requisita_tempo(nome_da_cidade):
    
    print("-----------------------------")
    print("-Começando extração de dados-")
    print("-----------------------------")

    link = f'https://api.openweathermap.org/data/2.5/weather?q={nome_da_cidade}&appid={api_secret}&lang=pt_br'

    requisicao = requests.get(link, verify=False)

    if requisicao.status_code != 200:
        requisicao_dic = 'Não foi possível obter a localização.'
        return requisicao_dic
    else:
        requisicao_dic = requisicao.json()
        dados_cidade = [{
            "pais": requisicao_dic['sys']['country'],
            "cidade": requisicao_dic["name"],
            "temperatura": int(requisicao_dic["main"]["temp"] - 273.15),
            "temperatura_min": int(requisicao_dic["main"]["temp_min"] - 273.15),
            "temperatura_max": int(requisicao_dic["main"]["temp_max"] - 273.15),
            "descricao": requisicao_dic["weather"][0]["description"],
            "icon": requisicao_dic["weather"][0]["icon"],
            "data_requisicao": datetime.now().strftime("%y%m%d")     
        }]
        cidade_df = pd.DataFrame(dados_cidade)
        cidade_df.to_csv('sharknado/hist/cities_weather_req.csv', mode='a', index='', header=False)
        
         


requisita_tempo('recife')

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
