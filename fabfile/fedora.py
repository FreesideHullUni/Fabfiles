from invoke import task
from fabric2 import Connection

@task
def install(c, pkg):
    c.run('dnf -y install ' + pkg, pty=True)
