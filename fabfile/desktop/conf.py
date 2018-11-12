from invoke import task, Exit, Collection, Responder
from fabric2 import Connection
from fabric2.transfer import Transfer
from patchwork.files import append


@task
def selinux(c):
    c.sudo("setsebool -P use_nfs_home_dirs 1")


@task
def dconf(c):
    append(c, "/etc/dconf/profile/user", "service-db:keyfile/user")
    c.append(
        "/etc/dconf/profile/gdm",
        "user-db:user\n"
        "system-db:gdm\n"
        "file-db:/usr/share/gdm/greeter-dconf-defaults",
        use_sudo=True,
    )
    c.sudo("mkdir /etc/dconf/db/gdm.d")
    c.append(
        "/etc/dconf/db/gdm.d/00-login-screen",
        "[org/gnome/login-screen]\n" "disable-user-list=true",
        use_sudo=True,
    )
    c.sudo("dconf update")


@task
def deploy_ff_policy(c):
    with c.cd("/usr/lib64/firefox/"):
        c.put(
            "distFiles/firefox/distribution.ini",
            "distribution/",
            use_sudo=True
        )


@task
def wol_setup(c):
    c.append(
        "/etc/sysconfig/network-scripts/ifcfg-eno1",
        'ETHTOOL_OPTIONS="wol g"'
    )
