from invoke import task
from tasks.lint import flake8


@task(post=[flake8])
def all(ctx):
    """ Run all tests and check linting """
    ctx.run("python -m unittest discover")


@task
def unit(ctx):
    """ Run all unit tests """
    ctx.run("python -m unittest discover -s tests.unit")


@task
def integration(ctx):
    """ Run all integration tests"""
    ctx.run("python -m unittest discover -s tests.integration")