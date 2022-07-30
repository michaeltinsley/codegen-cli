from typer.testing import CliRunner

from codegen import codegen_app

runner = CliRunner()


def test_language():
    result = runner.invoke(codegen_app, ["", "--language", "python"])
    assert result.exit_code == 0


def test_unsupported_language():
    result = runner.invoke(codegen_app, ["", "--language", "java"])
    assert result.exit_code == 2
    assert "Invalid value" in result.output
