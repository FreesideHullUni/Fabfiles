from invoke import task, Exit, Collection, Responder
from fabric import Connection
from fabric.transfer import Transfer
from patchwork.files import append

import os

from . import desktop
from . import utility


ns = Collection()

d = Collection("desktop")
d.add_collection(desktop)
d.add_collection(desktop.install)
d.add_collection(desktop.conf)

ns.add_collection(d)
ns.add_collection(utility)
