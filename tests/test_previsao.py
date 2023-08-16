from sharknado.previsao import previsao_hoje


def test_previsao_true():

    print(previsao_hoje('recife'))

def test_previsao_erro():

    print(previsao_hoje('sa paulo'))
