import typer

app = typer.Typer()

@app.command()
def hello():
    typer.echo("Hello world!")


if __name__ == "__main__":
    app()


# Add a 'status' command that will check the server
# Add a 'backup' command that will back up the world
# Add a 'restart' command that will restart the server
# Consider an admin list
# Consider a ban list