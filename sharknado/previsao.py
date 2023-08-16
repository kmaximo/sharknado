"""
Módulo de previsão de tempo.

Attributes:
   nome_da_cidade: Nome da Cidade que deseja saber a previsão do tempo
   imperial: Para temperaturas em Fahrenheit e ventos miles/hour. Por default Temperatura Celsius e metros/sec


# PREVISAO

Os dados da previsão do tempo são obtidas através da api do [open_weather](https://openweathermap.org/).
Após a requisição é gerado um arquivo .csv para armazenar historio e para gerar os gráficos
"""
from configparser import ConfigParser
from urllib import parse

import pandas as pd
import requests
from datetime import datetime
from decouple import config
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


api_secret = config('API_KEY')


def get_data(nome_da_cidade: str, imperial: bool=False, forecast: bool=False) -> dict[str, list[str]]:
    """
    Realiza requisição para obter informações da previsão do tempo da cidade escolhida.

    Args:
        nome_da_cidade: Nome da Cidade que deseja saber o tempo
        imperial: Para temperaturas em Fahrenheit e ventos miles/hour. Por default Temperatura Celsius e metros/sec

    Returns:
        requisicao: Um dicionário com dados da previsão do tempo de hoje da cidade escolhida.

    """

    BASE_WEATHER_API_URL = f'https://api.openweathermap.org/data/2.5/'
    query = 'forecast' if forecast else 'weather'
    api_key = config('API_KEY')
    city_name = nome_da_cidade.lower()
    url_encoded_city_name = parse.quote_plus(city_name)
    units = 'imperial' if imperial else 'metric'
    url = (
        f'{BASE_WEATHER_API_URL}{query}?q={url_encoded_city_name}'
        f'&units={units}&appid={api_key}&lang=pt_br'
    )

    requisicao = requests.get(url, verify=False)

    return requisicao


def previsao_hoje(nome_da_cidade: str, imperial: bool=False, forecast: bool=False) -> dict[str, list[str]]:
    """
    Gera previsão do tempo da cidade escolhida.

    Args:
        nome_da_cidade: Nome da Cidade que deseja saber o tempo
        imperial: Para temperaturas em Fahrenheit e ventos miles/hour. Por default Temperatura Celsius e metros/sec

    Returns:
        Um dicionário com dados da previsão do tempo de hoje da cidade escolhida.

    Raises:
        ValueError: A definir.
        KeyError: A definir.

    Examples:
        previsao_hoje('recife')
        {'pais': 'BR', 'cidade': 'Recife', 'temperatura': 23, 'temperatura_min': 23, 'temperatura_max': 23, 'sensacao_termica': 24, 'vento': 5.45, 'tempo_id': 500, 'descricao': 'chuva leve', 'data': '2023-08-15 00:00:00'}

    """
    requisicao_hoje = get_data(nome_da_cidade, imperial, forecast)
    

    if requisicao_hoje.status_code == 200:
        requisicao_dic = requisicao_hoje.json()

        dados_cidade_hoje = [{
                'pais': requisicao_dic['sys']['country'],
                'cidade': requisicao_dic['name'],
                'lat': requisicao_dic['coord']['lat'],
                'lon': requisicao_dic['coord']['lon'],
                'temperatura': int(requisicao_dic['main']['temp']),
                'temperatura_min': int(
                    requisicao_dic['main']['temp_min']
                ),
                'temperatura_max': int(
                    requisicao_dic['main']['temp_max']
                ),
                'sensacao_termica': int(
                    requisicao_dic['main']['feels_like']
                ),
                'vento': requisicao_dic['wind']['speed'],
                'tempo_id': requisicao_dic['weather'][0]['id'],
                'descricao': requisicao_dic['weather'][0][
                    'description'
                ],
                'data': datetime.now().strftime("%y%m%d") ,
            }
        ]
    else:
        print(
            'Algo deu errado.\r\nStatus code: %s' % requisicao_hoje.status_code
        )
        print(
            'Você pode saber mais sobre o erro em: https://www.google.com.br/search?q=http+status+code+%s'
            % requisicao_hoje.status_code
        )
    return dados_cidade_hoje

def previsao_dias(nome_da_cidade: str, imperial: bool=False, forecast: bool=True) -> dict[str, list[str]]:
    """
    Gera previsão do tempo da cidade escolhida.

    Args:
        nome_da_cidade: Nome da Cidade que deseja saber o tempo
        imperial: Para temperaturas em Fahrenheit e ventos miles/hour. Por default Temperatura Celsius e metros/sec

    Returns:
        Um dicionário com dados da previsão do tempo de hoje da cidade escolhida.

    Raises:
        ValueError: A definir.
        KeyError: A definir.

    Examples:
        previsao_hoje('recife')
        {'pais': 'BR', 'cidade': 'Recife', 'temperatura': 23, 'temperatura_min': 23, 'temperatura_max': 23, 'sensacao_termica': 24, 'vento': 5.45, 'tempo_id': 500, 'descricao': 'chuva leve', 'data': '2023-08-15 00:00:00'}

    """
    requisicao_hoje = get_data(nome_da_cidade, imperial, forecast)
    
    lista_hoje_3h = []

    if requisicao_hoje.status_code == 200:
        requisicao_dic = requisicao_hoje.json()

        for i in range(0,40):
            dados_cidade_hoje = {
                    'pais': requisicao_dic['city']['country'],
                    'cidade': requisicao_dic['city']['name'],
                    'lat': requisicao_dic['city']['coord']['lat'],
                    'lon': requisicao_dic['city']['coord']['lon'],
                    'temperatura': int(requisicao_dic['list'][i]['main']['temp']),
                    'temperatura_min': int(
                        requisicao_dic['list'][i]['main']['temp_min']
                    ),
                    'temperatura_max': int(
                        requisicao_dic['list'][i]['main']['temp_max']
                    ),
                    'sensacao_termica': int(
                        requisicao_dic['list'][i]['main']['feels_like']
                    ),
                    'vento': requisicao_dic['list'][i]['wind']['speed'],
                    'tempo_id': requisicao_dic['list'][i]['weather'][0]['id'],
                    'descricao': requisicao_dic['list'][i]['weather'][0][
                        'description'
                    ],
                    'data': requisicao_dic['list'][i]['dt_txt'],
                }
            lista_hoje_3h.append(dados_cidade_hoje)
    else:
        print(
            'Algo deu errado.\r\nStatus code: %s' % requisicao_hoje.status_code
        )
        print(
            'Você pode saber mais sobre o erro em: https://www.google.com.br/search?q=http+status+code+%s'
            % requisicao_hoje.status_code
        )
    return lista_hoje_3h

