import typer
from rich.console import Console
from rich.syntax import Syntax

from .languages import Language
from .model import Model

app = typer.Typer(name="Codegen CLI: Generate Python code from Huggingface models")


@app.command()
def generate(
    prompt: str,
    language: Language = typer.Option(Language.python, case_sensitive=True),
) -> None:
    """
    Generate code from a Huggingface model.

    :param prompt: The input string
    :param language: The language to generate code for
    """
    print(
        f"Generating code for the prompt '{prompt}', in {language.value.capitalize()}..."
    )

    codegen_model = Model()
    generated_code = codegen_model(prompt, language.value)

    syntax = Syntax(generated_code, language.value, theme="monokai", line_numbers=True)
    console = Console()
    console.print(syntax)


if __name__ == "__main__":
    app()
