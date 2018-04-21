from invoke import task


@task
def start(ctx):
    """ Start the pkgparse server """
    ctx.run("FLASK_APP=pkgparse/__init__.py flask run --host=0.0.0.0")
