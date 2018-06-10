from invoke import task, Exit, Collection, Responder
from fabric2 import Connection
from fabric2.transfer import Transfer
from patchwork.files import append

import os

from . import desktop
from . import utility



ns = Collection()

d = Collection('desktop')
d.add_collection(desktop)
d.add_collection(desktop.install)
d.add_collection(desktop.conf)

ns.add_collection(d)
ns.add_collection(utility)

#env.roledefs = {
#    'desktops': ['fs-desktop-01', 'fs-desktop-02', 'fs-desktop-03'],
#    'servers': ['ipa', 'docker', 'fs-web-02']
#}


