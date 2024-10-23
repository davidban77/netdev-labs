[![Open the Example in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidban77/netdev-labs?quickstart=1)
# NetDev Labs

Labs for Network Development and Observaility.

## Setup the Environment

To get started you can clone and open this in a [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) or open up the environment directly in GitHub Codespaces with the button above.

## Usage

To get started you can use the `lab` command:

```bash
lab --help
```

It comes with builtin commands to manage [containerlab](https://containerlab.dev/) and [docker compose](https://docs.docker.com/compose/) environments.

```bash
lab containerlab --help
lab docker --help
```

But to simplify the usage of the lab environments you can setup a complete environment for the scenario using the `lab create` command.

```bash
lab create netobs
```

### Labs structure

Each `lab` contains a `containerlab/` and `docker-compose.yml` directory with the lab environment configuration. These are the basic specifications for the lab environment.

To start the `containerlab` environment:

```bash
labcli containerlab start labs/netobs/containerlab/lab.clab.yml
```

To start the `docker compose` environment:

```bash
labcli docker start --compose labs/netobs/docker-compose.yml
```

> Note: You can also use the `--help` flag to get more information about the commands and their options. For example, with the `--profile` argument you can spin up a docker compose environment for a specific profile of services applied to it:
>
> ```bash
> labcli docker start --compose labs/netobs/docker-compose.yml --profile collector
> ```
>
> This will start the `docker-compose.yml` environment with the `collector` profile.
