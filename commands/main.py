from pathlib import Path
import typer
from labcli.cli import app
from labcli.utils.containerlab_utils import containerlab_deploy, containerlab_destroy, containerlab_inspect
from labcli.utils.docker_utils import docker_ps, docker_destroy, docker_start

# lab_app = typer.Typer(help="Lab related commands", rich_markup_mode="rich")

# app.add_typer(lab_app, name="lab")

app._add_completion = False


@app.command()
def create(lab: str = typer.Argument(..., help="Name of the lab")):
    """Create a lab

    Example:

    $ lab create netobs
    """
    # Deploy containerlab topology
    clab_cmd = containerlab_deploy(sudo=True, topology=Path(f"./labs/{lab}/containerlab/lab.clab.yml"))
    if clab_cmd is not None and clab_cmd.returncode != 0:
        typer.echo(clab_cmd.stderr)
        raise typer.Abort()
    # Start docker containers
    docker_cmd = docker_start(compose_file=Path(f"./labs/{lab}/docker-compose.yml"))
    if docker_cmd is not None and docker_cmd.returncode != 0:
        typer.echo(docker_cmd.stderr)
        raise typer.Abort()
