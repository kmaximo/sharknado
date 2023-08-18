# API - Tarefas

Tarefas previstas

- Previsão do tempo
  - Feature: Requisição
    - [x] Implementar busca de informações de previsão do tempo referentes à cidade desejada pelo usuário na OpenWeatherMap API : [referência](https://openweathermap.org/api)
    - [x] Usar argumento ``--u`` ou ``-u`` para usar outra unidade de medida em Fahrenheit, milhas/hora, por default está em Celsius e metros/sec
  - Feature: Processamento
    - [x] Tratamento dos resultados recebidos pelo OpenWeatherMap, transformando-os em informações mais legíveis, e gerando o gráfico, se requisitado.: [Referência oficial](https://docs.python.org/3/tutorial/errors.html#tut-userexceptions), [Referência no canal](https://youtu.be/sJpNfZqLpoI)
    - [ ] Exportar os dados do pandas para um csv para guardar histórico
  - Feature: Resposta
    - [x] Enviar a resposta final ao usuário, contendo informações sobre a previsão do tempo, gráfico (se for solicitado) e alertas, caso haja algum
- Pontos de melhorias
  - Gráfico com dados da previsão do tempo
    - [ ] Usar o rich.table [Rich](https://rich.readthedocs.io/en/latest/appendix/box.html)
  - Alertas com dados da previsão do tempo
    - [ ] Criar novos alertas com o [Rich](https://rich.readthedocs.io/)

Para tarefas não mapeadas aqui, você pode consultar as [issues do projeto](https://github.com/kmaximo/sharknado_wheater/issues)
