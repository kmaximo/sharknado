
# Sharknado

Sharknado é um CLI de previsao do tempo busca informações sobre tempo em uma determinada cidade através da API [OpenWeather](https://openweathermap.org/api) .

Toda a aplicação é baseada em um comando chamado `sharknado`.

## Como usar?

### Previsão do tempo neste momento

Você pode saber a previsão do tempo atual via linha de comando. Por exemplo:

```bash
poetry run skarknado 'nome da cidade'
```

Retornando informações do tempo da cidade escolhida:

```bash
NG Sokoto   Algumas nuvens    Temperatura (37°C) Temp min (37°C) Temp max (37°C) Sensação Térmica (37°C) Vento (37 m/s)
```

### Previsão do tempo agora em outra unidade de medida: Fahrenheit e miles/h

Você pode saber a previsão do tempo atual via linha de comando. Por exemplo:

```bash
poetry run skarknado 'nome da cidade' -u
```

Retornando informações do tempo da cidade escolhida:

```bash
NG Sokoto  Nuvens dispersas   Temperatura (98°F) Temp min (98°F) Temp max (98°F) Sensação Térmica (98°F) Vento (98 m/h) 
```

## Gráfico

## Como usar gráfico?

### Previsão do tempo neste momento com gráfico

Você pode saber a previsão do tempo atual via linha de comando. Por exemplo:

```bash
poetry run skarknado 'nome da cidade' -g
```

Retornando informações em uma janela do tempo da cidade escolhida

### Previsão do tempo agora em outra unidade de medida: Fahrenheit e miles/h com gráfico

Você pode saber a previsão do tempo atual via linha de comando. Por exemplo:

```bash
poetry run skarknado 'nome da cidade' -u -g
```

Retornando informações em uma janela do tempo da cidade escolhida

## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag `--help`:

```bash
poetry run skarknado --help
                                                                       
 Usage: sharknado [OPTIONS] 'NOME_DA_CIDADE'

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    nome_da_cidade      TEXT  Informar entre aspas, o 'Nome da Cidade' que deseja saber o tempo [default: None]           │
│                                [required]                                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --u                   -u                                       Para temperaturas em Fahrenheit e ventos miles/hour. Por    │
│                                                                default Temperatura Celsius e metros/sec                    │
│ --g                   -g                                       Para gráficos com as informações do tempo                   │
│ --install-completion          [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None] │
│ --show-completion             [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or      │
│                                                                customize the installation.                                 │
│                                                                [default: None]                                             │
│ --help                                                         Show this message and exit.                                 │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
