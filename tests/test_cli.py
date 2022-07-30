from typer.testing import CliRunner

from codegen import CodegenApp as app

runner = CliRunner()


def test_language():
    result = runner.invoke(app, ["", "--language", "python"])
    assert result.exit_code == 0


def test_unsupported_language():
    result = runner.invoke(app, ["", "--language", "java"])
    assert result.exit_code == 2
    assert "Invalid value" in result.output


def test_prompt():
    result = runner.invoke(app, ["# Print Hello World!"])
    assert result.exit_code == 0
    assert "Print Hello World!" in result.output
