import time

import pandas as pd
import plotly.express as px
from rich.console import Console
from rich.progress import Progress, track
from rich.style import Style
from rich.table import Table
from typer import Argument, Context, Exit, Option, Typer, run

from sharknado import __version__
from sharknado.previsao import *

console = Console()
table = Table()
app = Typer()

# Codigo das condições do tempo
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)

base_style = {
    'THUNDERSTORM': Style.parse('red'),
    'DRIZZLE': Style.parse('cyan'),
    'RAIN': Style.parse('blue'),
    'SNOW': Style.parse('bright_white'),
    'ATMOSPHERE': Style.parse('blue'),
    'CLEAR': Style.parse('yellow'),
    'CLOUDY': Style.parse('dim'),
    'RESET': Style.parse('white'),
}


def version_func(flag):
    if flag:
        print(__version__)
        raise Exit(code=0)


@app.callback(invoke_without_command=True)
def main(
    ctx: Context,
    version: bool = Option(False, callback=version_func, is_flag=True),
):
    message = """Forma de uso: [b]sharknado [SUBCOMANDO] [ARGUMENTOS][/]

    Existe 1 subcomando disponível para essa aplicação

    - [b]previsao[/]: Gera previsão do tempo da cidade escolhida.

    [b]Exemplos de uso:[/]
    sharknado previsao 'recife'

    sharknado previsao 'sao paulo' -u

    sharknado previsao 'Londres' -u -g

    [b]Para mais informações rápidas: [red]sharknado --help[/]

    [b]Para informações detalhadas: [blue][link=http://sharknado_weather.readthedocs.io]acesse a documentação![/]
    """
    if ctx.invoked_subcommand:
        return
    console.print(message)


@app.command()
def previsao(
    nome_da_cidade=Argument(
        ...,
        help="Informar entre aspas, o 'Nome da Cidade' que deseja saber o tempo",
    ),
    u: bool = Option(
        False,
        '-u',
        '--u',
        help='Para temperaturas em Fahrenheit e ventos miles/hour. Por default Temperatura Celsius e metros/sec',
    ),
    g: bool = Option(
        False,
        '-g',
        '--g',
        help='Para gráficos com as informações do tempo',
    ),
):

    if g:

        dados = previsao_dias(nome_da_cidade, u, g)
        cidade = dados[0]['cidade']
        datas = []
        df = pd.DataFrame(dados)

        # for x in df['data']:
        #     dt = x.split(' ')
        #     dt = dt[0]
        #     datas.append(dt)
        # df['dt'] = datas

        # df.plot.bar(
        #     x='dt',
        #     y=['temperatura', 'temperatura_min', 'temperatura_max'],
        #     rot=0,
        #     figsize=(16, 9),
        #     title=f'Previsão de 5 dias de temperaturas da cidade de {cidade}',
        #     xlabel='Dias',
        #     ylabel=f"Temperatura em °{'F' if u else 'C'}",
        # )
        # plt.show()

        fig = px.bar(
            df,
            x='data',
            y='temperatura',
            title=f'Previsão de 5 dias de temperaturas da cidade de {cidade}',
            labels={  # replaces default labels by column name
                'data': 'Dias',
                'temperatura': f"Temperatura em °{'F' if u else 'C'}",
            },
        )
        fig.show()

        # print(df)

    else:
        for i in track(range(20), description='Processando...'):
            time.sleep(0.5)  # Simulate work being done
        dados = previsao_hoje(nome_da_cidade, u, g)

        pais = dados[0]['pais']
        cidade = dados[0]['cidade']
        temperatura = dados[0]['temperatura']
        temperatura_min = dados[0]['temperatura_min']
        temperatura_max = dados[0]['temperatura_max']
        sensacao_termica = dados[0]['temperatura_max']
        vento = dados[0]['temperatura_max']
        tempo_id = dados[0]['tempo_id']
        descricao_tempo = dados[0]['descricao']
        data_temperatura = dados[0]['data']

        console.print(f'[white reverse]{pais}[/]', end=' ')
        console.print(f'[white reverse]{cidade}[/]', end='')

        cor = select_cor_display(tempo_id)
        console.print(
            f'{descricao_tempo.capitalize():^20}', end=' ', style=cor
        )
        cor = base_style['RESET']

        console.print(
            f"Temperatura ({temperatura}°{'F' if u else 'C'})", end=' '
        )
        console.print(
            f"Temp min ({temperatura_min}°{'F' if u else 'C'})", end=' '
        )
        console.print(
            f"Temp max ({temperatura_max}°{'F' if u else 'C'})", end=' '
        )
        console.print(
            f"Sensação Térmica ({sensacao_termica}°{'F' if u else 'C'})",
            end=' ',
        )
        console.print(f"Vento ({vento} {'m/h' if u else 'm/s'})", end=' ')


def select_cor_display(tempo_id):
    if tempo_id in THUNDERSTORM:
        estilo = base_style['THUNDERSTORM']
    elif tempo_id in DRIZZLE:
        estilo = base_style['DRIZZLE']
    elif tempo_id in RAIN:
        estilo = base_style['RAIN']
    elif tempo_id in SNOW:
        estilo = base_style['SNOW']
    elif tempo_id in ATMOSPHERE:
        estilo = base_style['ATMOSPHERE']
    elif tempo_id in CLEAR:
        estilo = base_style['CLEAR']
    elif tempo_id in CLOUDY:
        estilo = base_style['CLOUDY']
    else:  # no caso de surgir novos codígos
        estilo = base_style['RESET']
    return estilo


# cidade_df = pd.DataFrame(dados_cidade)
# cidade_df.to_csv(
#     'sharknado/hist/previsao_dias.csv',
#     mode='a',
#     index=False,
#     header=False,
# )
