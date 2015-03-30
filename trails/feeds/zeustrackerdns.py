#!/usr/bin/env python

"""
Copyright (c) 2014-2015 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

from core.common import retrieve_content

__url__ = "https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist"
__check__ = "ZeuS"
__info__ = "zeus (malware)"
__reference__ = "zeustracker.abuse.ch"

def fetch():
    retval = {}
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            retval[line] = (__info__, __reference__)

    return retval
