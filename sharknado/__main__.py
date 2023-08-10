from rich.console import Console
from sharknado.previsao import *
import datetime
from time import sleep

console = Console()

def startup():
    console.rule("Inicializando Sharknado")
    sleep(2)
    console.rule("Verificando conexão com a internet")
    sleep(2)
    console.rule("Aguarde um momento")
    sleep(2)
    console.rule("Sharknado está online")
    sleep(2)
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        console.rule("[green]Bom dia")
    elif hour>12 and hour<18:
        console.rule("[yellow]Boa Tarde")
    else:
        console.rule("[red]Boa Noite")

def main():

    sim_escolha = ['sim', 's']
    nao_escolha = ['nao', 'n']

    previsao_escolha_hj = console.input('[green]Você deseja saber a previsão do tempo de hoje? (sim/nao): ')

    if previsao_escolha_hj.lower() in sim_escolha:
        nome_cidade = console.input('Informe a cidade que você deseja saber a previsão do tempo: ')
        #print(previsao_hoje(nome_cidade))
    else:
        print('Até a próxima!!')
        sys.exit()
        

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

if __name__ == '__main__':
    startup()
    main()
