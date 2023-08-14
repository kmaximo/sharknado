from rich.console import Console
from typer import Argument, Context, Exit, Option, Typer, run

from sharknado.previsao import *

console = Console()

app = Typer()


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
    # 
    dados = previsao_hoje(nome_da_cidade, u)
    # 
    pais = dados['pais']
    cidade = dados['cidade']
    temperatura = dados['temperatura']
    temperatura_min = dados['temperatura_min']
    temperatura_max = dados['temperatura_max']
    descricao_tempo = dados['descricao']
    data_temperatura =  dados['data']

    console.print(f'{cidade}', end='')
    console.print(
        f"\t{descricao_tempo.capitalize():^20}", 
        end=" ") 
    console.print(f"({temperatura}°{'F' if u else 'C'})")


if __name__ == '__main__':
    run(consulta_previsao_hoje)
