from invoke import task
from fabric2 import Connection

@task
def update(c):
    c.sudo('dnf -y update')

@task
def fed_vers(c):
    version = c.run('cat /etc/fedora-release', hide=True).stdout.strip()
    print('{}: {}'.format(c.host, version))
