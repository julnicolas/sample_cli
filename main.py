import typer
from enum import StrEnum

class Env(StrEnum):
    Foo = "foo"

app = typer.Typer()

@app.command()
def status(env: Env):
    """Show deployment metadata for specified environment"""
    print(f"environment: {env.value}")

@app.command()
def rollback(env: Env):
    """Rollback specified environment"""
    print(f"environment: {env.value}")

if __name__ == "__main__":
    app()
