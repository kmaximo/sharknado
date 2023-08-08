from sharknado.previsao import requisita_tempo


def main():
    nome_cidade = input('Informe a cidade: ')
    print(requisita_tempo(nome_cidade))


if __name__ == '__main__':
    main()
