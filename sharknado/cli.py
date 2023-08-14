from rich.console import Console
from rich.style import Style
from typer import Argument, Context, Exit, Option, Typer, run

from sharknado.previsao import previsao_hoje

console = Console()

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


@app.command()
def consulta_previsao_hoje(
    nome_da_cidade=Argument(
        ..., help='Nome da Cidade que deseja saber o tempo'
    ),
    u: bool = Option(
        False,
        help='Para temperaturas em Fahrenheit e ventos miles/hour. Por default Temperatura Celsius e metros/sec )',
    ),
):

    dados = previsao_hoje(nome_da_cidade, u)

    pais = dados['pais']
    cidade = dados['cidade']
    temperatura = dados['temperatura']
    temperatura_min = dados['temperatura_min']
    temperatura_max = dados['temperatura_max']
    sensacao_termica = dados['temperatura_max']
    vento = dados['temperatura_max']
    tempo_id = dados['tempo_id']
    descricao_tempo = dados['descricao']
    data_temperatura = dados['data']

    console.print(f'[white reverse]{pais}[/]', end=' ')
    console.print(f'[white reverse]{cidade}[/]', end='')

    cor = select_cor_display(tempo_id)
    console.print(f'{descricao_tempo.capitalize():^20}', end=' ', style=cor)
    cor = base_style['RESET']

    console.print(f"Temperatura ({temperatura}°{'F' if u else 'C'})", end=' ')
    # console.print(f"Temp min ({temperatura_min}°{'F' if u else 'C'})", end=' ')
    # console.print(f"Temp max ({temperatura_max}°{'F' if u else 'C'})", end=' ')


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
    else:  # In case the API adds new weather codes
        estilo = base_style['RESET']
    return estilo


# if __name__ == '__main__':
#     run(consulta_previsao_hoje)
