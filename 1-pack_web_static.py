#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """pack the files"""
    filename = "web_static_" + datetime.strftime(datetime.now(),
                                                 "%Y%m%d%H%M%S") + ".tgz"
    try:
        local("mkdir -p versions", capture=False)
        local("tar -cvzf " + filename + " web_static")
        return "versions/" + filename
    except:
        return None
