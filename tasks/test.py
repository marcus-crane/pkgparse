from invoke import task


@task
def all(ctx):
    """ Run every test """
    ctx.run("python -m unittest discover")

@task
def unit(ctx):
    """ Run all unit tests """
    ctx.run("python -m unittest discover -s tests.unit")

@task
def integration(ctx):
    """ Run all integration tests"""
    ctx.run("python -m unittest discover -s tests.integration")