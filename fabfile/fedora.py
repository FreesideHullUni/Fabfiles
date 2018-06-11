from invoke import task
from fabric2 import Connection


@task
def install(c, pkg):
    c.sudo("dnf -y install " + pkg)
