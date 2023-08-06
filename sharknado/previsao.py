import requests

# link do open_weather: https://openweathermap.org/

API_KEY = '3338dae4b22d12a55b696ce212d8587a'
nome_da_cidade = 'recife'

link = f'https://api.openweathermap.org/data/2.5/weather?q={nome_da_cidade}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(link)

if requisicao.status_code != 200:
    print('Não foi possível obter a localização.')

else:
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    print(requisicao_dic)
    print(descricao, f'{temperatura}ºC')
