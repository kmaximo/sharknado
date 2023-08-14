from typer.testing import CliRunner

from sharknado.cli import app

runner = CliRunner()


def test_previsao_do_tempo_hoje():
    result = runner.invoke(app)
    assert result.exit_code == 0
