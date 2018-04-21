from invoke import task


@task
def make(ctx):
    """ Build a new version of the pkgparse docker image """
    ctx.run("docker build -t pkgparse:latest .")


@task
def start(ctx):
    """ Spin up the latest version of pkgparse docker image """
    ctx.run("docker-compose up --build -d")


@task
def stop(ctx):
    """ Spin down the pkgparse docker image """
    ctx.run("docker-compose down")