from sharknado.previsao import *
from rich.console import Console
from typer import Argument, run, Context, Exit, Option, Typer

console = Console()

def consulta_previsao_hoje(
    nome_da_cidade=Argument(
        ..., help='Nome da Cidade que deseja saber o tempo'
    ),
    u: bool = Option(False, help='Para temperaturas em Fahrenheit. Por default está False (Celsius)'),
):
    console.print(previsao_hoje(nome_da_cidade, u))

if __name__ == '__main__':
    run(consulta_previsao_hoje)
