## API - Tarefas a serem realizadas

Tarefas que precisam ser feitas para conclusão do projeto

- Previsão do tempo
  - Feature: Requisição
    - [x] Implementar busca de informações de previsão do tempo referentes à cidade desejada pelo usuário na OpenWeatherMap API : [referência](https://openweathermap.org/api)
    - [x] Usar argumento ``--u`` para usar a medida em Fahrenheit, por default está em Celsius
  - Feature: Processamento
    - [ ] Tratamento dos resultados recebidos pelo OpenWeatherMap, transformando-os em informações mais legíveis, e gerando o gráfico, se requisitado.: [Referência oficial](https://docs.python.org/3/tutorial/errors.html#tut-userexceptions), [Referência no canal](https://youtu.be/sJpNfZqLpoI)
    - [x] Exportar os dados do pandas para um csv para guardar histórico
  - Feature: Resposta
    - [ ] Enviar a resposta final ao usuário, contendo informações sobre a previsão do tempo, gráfico (se for solicitado) e alertas, caso haja algum
- Feature: Gráfico com dados da previsão do tempo
- Feature: Alertas com dados da previsão do tempo

Para tarefas não mapeadas aqui, você pode consultar as [issues do projeto](https://github.com/kmaximo/sharknado_wheater/issues)



<!-- cidade_df = pd.DataFrame(dados_cidade)
cidade_df.to_csv(
    'sharknado/hist/previsao_dias.csv',
    mode='a',
    index=False,
    header=False,
)  -->