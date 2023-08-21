from sharknado.previsao import previsao_hoje


def test_previsao_true():

    result = previsao_hoje('recife', False, False)
    assert 'Recife' in result[0]['cidade']


def test_previsao_erro():
    # result = previsao_hoje('sa paulo', False, False)
    # assert 'Sao Paulo' in result[0]['cidade']
    ...
