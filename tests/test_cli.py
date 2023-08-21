from pytest import mark
from typer.testing import CliRunner

from sharknado.cli import app

runner = CliRunner()


def test_aplicacao_previsao_do_tempo_hoje_recife():
    result = runner.invoke(app, ['previsao', 'recife'])
    assert result.exit_code == 0
    assert 'Recife' in result.stdout


def test_aplicacao_previsao_do_tempo_hoje_galway_fahrenheit():
    result = runner.invoke(app, ['previsao', 'galway', '-u'])
    assert result.exit_code == 0
    assert 'Galway' in result.stdout


def test_aplicacao_previsao_do_tempo_hoje_Sokoto_fahrenheit():
    result = runner.invoke(app, ['previsao', 'sokoto', '-u'])
    assert result.exit_code == 0
    assert 'Sokoto' in result.stdout
