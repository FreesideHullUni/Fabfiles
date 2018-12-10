from invoke import task
from fabric import Connection


@task
def install(c, pkg):
    c.sudo("dnf -y install " + pkg)
