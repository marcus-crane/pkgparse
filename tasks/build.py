from invoke import task

@task
def save_deps(ctx):
    """ Generate a new requirements.txt file """
    ctx.run("pip freeze > requirements.txt")


@task
def deps(ctx):
    """ Reinstall the requirements file """
    ctx.run("pip install -r requirements.txt")
