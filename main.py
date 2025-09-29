import typer
from enum import StrEnum

class Env(StrEnum):
    Foo = "foo"

app = typer.Typer()

@app.command()
def status(env: Env):
    print(f"environment: {env.value}")

@app.command()
def deploy(env: Env):
    print(f"environment: {env.value}")

if __name__ == "__main__":
    app()
