
# Sharknado Previsao do Tempo

Sharknado Previsao do Tempo é uma API para buscar informações sobre tempo em uma determinada cidade.

Toda a aplicação é baseada em um comando chamado `sharknado`. Esse comando tem um subcomando relacionado a cada ação que a aplicação pode realizar. Como `previsao`, `grafico` e `alertas`
{% include "templates/cards.html" %}


{% include "templates/instalacao.md" %}

## Como usar?

### Previsão de hoje

Você pode saber a previsão do tempo via linha de comando. Por exemplo:


```bash
{{ commands.run }} previsao_hoje 'nome da cidade'
```

Retornando informações do tempo da cidade escolhida:

```
BR Recife  Nuvens dispersas   Temperatura (28°C)
```

## Grafico

Uso básico

```bash
{{ commands.run }} acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

Até o momento você usar acordes maiores, menores, dimunito e aumentados


## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag `--help`:

```bash
{{ commands.run }} --help
                                                                       
 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...

╭─ Commands ──────────────────────────────────────────────────────────╮
│ acorde                                                              │
│ campo-harmonico                                                     │
│ escala                                                              │
╰─────────────────────────────────────────────────────────────────────╯
```

### Mais informações sobre os subcomandos

As informações sobre os subcomandos podem ser acessadas usando a flag `--help` após o nome do parâmetro. Um exemplo do uso do `help` nos campos harmônicos:

```bash
{{ commands.run }} campo-harmonico --help
                                                                       
 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE] 
                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica do campo harmônico           │
│                                 [default: c]                        │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmônico       │
│                                 [default: maior]                    │
╰─────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                         │
╰─────────────────────────────────────────────────────────────────────╯
```