from typing import Optional

from .main import app


@app.command()
def init(force: Optional[bool] = False) -> None:
    """
    Initialise the Huggingface project.
    """
    print("Initializing a new project...")
    if force:
        print("Force initialisation...")
