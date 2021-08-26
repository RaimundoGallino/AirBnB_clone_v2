#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """pack the files"""
    local("mkdir -p versions", capture=False)
    filename = "web_static_" + datetime.strftime(datetime.now(),
                                                 "%Y%m%d%H%M%S") + ".tgz"
    try:
        ret = local("tar -cvzf " + filename + " web_static", capture=True)
        return ret
    except:
        return None
