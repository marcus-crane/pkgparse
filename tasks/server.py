from invoke import task


@task
def start(ctx):
    """ Start the pkgparse server """
    ctx.run("gunicorn -w 4 -b 0.0.0.0:8000 pkgparse:app")
