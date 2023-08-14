"""
Módulo de previsão de tempo.

Attributes:
   nome_da_cidade: Nome da Cidade que deseja saber a previsão do tempo


# PREVISAO

Os dados da previsão do tempo são obtidas através da api do [open_weather](https://openweathermap.org/).
Após a requisição é gerado um arquivo .csv para armazenar historio e para gerar os gráficos


```py title="No seu shell interativo"
>>> from sharknado.previsao import requisita_tempo
>>> requisita_tempo('nome_da_cidade')
arquivo gerado -> sharknado/hist/cities_weather_req.csv

```
"""

import json
from configparser import ConfigParser
from urllib import parse

import pandas as pd
import requests
from decouple import config
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Set `verify=False` on `requests.post`.
# requests.post(url='https://example.com', data={'bar':'baz'}, verify=False)


api_secret = config('API_KEY')


def get_data(nome_da_cidade: str, imperial=False):
    """
    Realiza requisição para obter informações da previsão do tempo da cidade escolhida.

    Args:
        nome_da_cidade: Nome da Cidade que deseja saber o tempo
        imperial: Para temperaturas em Fahrenheit = True. Por default está False (Celsius)

    Returns:
        url: Um dicionário com dados da previsão do tempo de hoje da cidade escolhida.

    """

    # nome_cidade = nome_da_cidade.lower()
    BASE_WEATHER_API_URL = f'https://api.openweathermap.org/data/2.5/forecast'
    api_key = config('API_KEY')
    city_name = nome_da_cidade.lower()
    url_encoded_city_name = parse.quote_plus(city_name)
    units = 'imperial' if imperial else 'metric'
    url = (
        f'{BASE_WEATHER_API_URL}?q={url_encoded_city_name}'
        f'&units={units}&appid={api_key}&lang=pt_br'
    )

    requisicao = requests.get(url, verify=False)

    return requisicao


def previsao_hoje(nome_da_cidade: str, imperial=False) -> dict[str, list[str]]:
    """
    Gera previsão do tempo da cidade escolhida.

    Args:
        nome_da_cidade: Nome da Cidade que deseja saber o tempo
        imperial: Para temperaturas em Fahrenheit = True. Por default está False (Celsius)

    Returns:
        Um dicionário com dados da previsão do tempo de hoje da cidade escolhida.

    Raises:
        ValueError: A definir.
        KeyError: A definir.

    Examples:
        >>> previsao_hoje('recife')
        [{'pais': 'BR', 'cidade': 'Recife', 'temperatura': 28, 'temperatura_min': 28, 'temperatura_max': 28, 'descricao': 'nuvens dispersas', 'data_requisicao': '230810'}]

    """
    requisicao_hoje = get_data(nome_da_cidade, imperial)

    if requisicao_hoje.status_code == 200:
        requisicao_dic = requisicao_hoje.json()

        dados_cidade_hoje = [
            {
                'pais': requisicao_dic['city']['country'],
                'cidade': requisicao_dic['city']['name'],
                'temperatura': int(requisicao_dic['list'][0]['main']['temp']),
                'temperatura_min': int(
                    requisicao_dic['list'][0]['main']['temp_min']
                ),
                'temperatura_max': int(
                    requisicao_dic['list'][0]['main']['temp_max']
                ),
                'descricao': requisicao_dic['list'][0]['weather'][0][
                    'description'
                ],
                'data': requisicao_dic['list'][0]['dt_txt'],
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
    return dados_cidade_hoje[0]


def previsao_dias(nome_da_cidade: str, imperial=False) -> dict[str, list[str]]:
    """
    Gera previsão do tempo de 5 dias da cidade escolhida.

    Args:
        nome_da_cidade: Nome da Cidade que deseja saber o tempo
        imperial: Para temperaturas em Fahrenheit = True. Por default está False (Celsius)

    Returns:
        Um dicionário com dados da previsão do tempo de hoje da cidade escolhida.

    Raises:
        ValueError: A definir.
        KeyError: A definir.

    Examples:
        >>> previsao_hoje('recife')
        [{'pais': 'BR', 'cidade': 'Recife', 'temperatura': 28, 'temperatura_min': 28, 'temperatura_max': 28, 'descricao': 'nuvens dispersas', 'data_requisicao': '230810'}]

    """

    requisicao_dias = get_data(nome_da_cidade, imperial)

    if requisicao_dias.status_code == 200:
        requisicao_dic = requisicao_dias.json()

        for i in range(requisicao_dic['cnt']):
            dados_cidade_dias = [
                {
                    'pais': requisicao_dic['city']['country'],
                    'cidade': requisicao_dic['city']['name'],
                    'temperatura': int(
                        requisicao_dic['list'][i]['main']['temp']
                    ),
                    'temperatura_min': int(
                        requisicao_dic['list'][i]['main']['temp_min']
                    ),
                    'temperatura_max': int(
                        requisicao_dic['list'][i]['main']['temp_max']
                    ),
                    'descricao': requisicao_dic['list'][i]['weather'][0][
                        'description'
                    ],
                    'data': requisicao_dic['list'][i]['dt_txt'],
                }
            ]
    else:
        print(
            'Algo deu errado.\r\nStatus code: %s' % requisicao_dias.status_code
        )
        print(
            'Você pode saber mais sobre o erro em: https://www.google.com.br/search?q=http+status+code+%s'
            % requisicao_dias.status_code
        )
    return dados_cidade_dias


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
