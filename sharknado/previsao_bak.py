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

from datetime import datetime
from decouple import config
from rich.console import Console
import pandas as pd
import requests

console = Console()
api_secret = config('API_KEY')


def get_data(nome_da_cidade: str) -> dict[str, list[str]]:
    """
    Realiza requisição para obter informações da previsão do tempo da cidade escolhida.

    Args:
        nome_da_cidade: Nome da Cidade que deseja saber o tempo

    Returns:
        requisicao: Um dicionário com dados da previsão do tempo de hoje da cidade escolhida.

    Examples:
        >>> previsao_hoje('recife')
        [{"cod":"200","message":0,"cnt":40,"list":[{"dt":1691614800,"main":{"temp":300.17,"feels_like":301.63,"temp_min":297.63,"temp_max":300.17,}]

    """
    console.rule('Começando extração de dados')
    
    nome_cidade = nome_da_cidade.lower()
    link = f'https://api.openweathermap.org/data/2.5/forecast?q={nome_cidade}&appid={api_secret}&lang=pt_br'
    requisicao = requests.get(link, verify=False)
    return requisicao


def previsao_hoje(nome_da_cidade: str) -> dict[str, list[str]]:
    """
    Gera previsão do tempo da cidade escolhida.

    Args:
        nome_da_cidade: Nome da Cidade que deseja saber o tempo

    Returns:
        Um dicionário com dados da previsão do tempo de hoje da cidade escolhida.

    Raises:
        ValueError: A definir.
        KeyError: A definir.

    Examples:
        >>> previsao_hoje('recife')
        [{'pais': 'BR', 'cidade': 'Recife', 'temperatura': 28, 'temperatura_min': 28, 'temperatura_max': 28, 'descricao': 'nuvens dispersas', 'data_requisicao': '230810'}]

    """
    requisicao_hoje = get_data(nome_da_cidade)

    if requisicao_hoje.status_code == 200:
        requisicao_dic = requisicao_hoje.json()

        dados_cidade_hoje = [
            {
                'pais': requisicao_dic['city']['country'],
                'cidade': requisicao_dic['city']['name'],
                'temperatura': int(
                    requisicao_dic['list'][0]['main']['temp'] - 273.15
                ),
                'temperatura_min': int(
                    requisicao_dic['list'][0]['main']['temp_min'] - 273.15
                ),
                'temperatura_max': int(
                    requisicao_dic['list'][0]['main']['temp_max'] - 273.15
                ),
                'descricao': requisicao_dic['list'][0]['weather'][0][
                    'description'
                ],
                'data_requisicao': requisicao_dic['list'][0]['dt_txt'],
            }
        ]
    else:
        print('Algo deu errado.\r\nStatus code: %s' % requisicao_hoje.status_code)
        print(
            'Você pode saber mais sobre o erro em: https://www.google.com.br/search?q=http+status+code+%s'
            % requisicao_hoje.status_code
        )
    return dados_cidade_hoje


def previsao_dias(nome_da_cidade):

    requisicao_dias = get_data(nome_da_cidade)

    if requisicao_dias.status_code == 200:
        requisicao_dic = requisicao_dias.json()

        for i in range(requisicao_dic['cnt']):
            dados_cidade_dias = [
                {
                    'pais': requisicao_dic['city']['country'],
                    'cidade': requisicao_dic['city']['name'],
                    'temperatura': int(
                        requisicao_dic['list'][i]['main']['temp'] - 273.15
                    ),
                    'temperatura_min': int(
                        requisicao_dic['list'][i]['main']['temp_min'] - 273.15
                    ),
                    'temperatura_max': int(
                        requisicao_dic['list'][i]['main']['temp_max'] - 273.15
                    ),
                    'descricao': requisicao_dic['list'][i]['weather'][0][
                        'description'
                    ],
                    'data_requisicao': requisicao_dic['list'][i]['dt_txt'],
                }
            ]
    else:
        print('Algo deu errado.\r\nStatus code: %s' % requisicao_dias.status_code)
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
#    console.rule('Previsão do tempo hoje')
#    console.rule('Previsão do tempo para 5 dias')
""" cidade_df = pd.DataFrame(dados_cidade_hoje)
cidade_df.to_csv(
    'sharknado/hist/previsao_hoje.csv',
    mode='a',
    index=False,
    header=False,
)

cidade_df = pd.DataFrame(dados_cidade)
cidade_df.to_csv(
    'sharknado/hist/previsao_dias.csv',
    mode='a',
    index=False,
    header=False,
) """