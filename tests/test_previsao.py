from sharknado.previsao import requisita_tempo


def test_previsao_true():
    print(requisita_tempo('recife'))


def test_previsao_false():
    print(requisita_tempo('sa paulo'))
