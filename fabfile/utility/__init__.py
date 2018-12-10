from invoke import task
from fabric import Connection


@task
def update(c):
    c.sudo("dnf -y update")


@task
def fed_vers(c):
    result = c.run("cat /etc/fedora-release", hide=True).stdout.strip()
    hostname = c.run("hostname", hide=True).stdout.strip()
    print("{}/{}: {}".format(c.host, hostname, result))
