#!/usr/bin/env python

import subprocess
import threading
import os

def ping(host):
    result = subprocess.call(
        '/usr/bin/rbd create -p pool-232fad5a7a5e4a62aebdf61292be3c1c  %s --size 102400 && /usr/bin/rbd rm  -p pool-232fad5a7a5e4a62aebdf61292be3c1c %s > /dev/null 2>&1' %(host,host), shell=True
#        '/usr/bin/rbd rm  -p pool-232fad5a7a5e4a62aebdf61292be3c1c %s &> /dev/null' % host , shell=True
    )
    if result == 0:
        print "%s:up" % host
    else:
        print "%s:down" % host

if __name__ == '__main__':
    ips = ['ruigang-%s' % i for i in range(0, 149)]
    for ip in ips:
        t = threading.Thread(target=ping, args=[ip])
        t.start()
os._exit(0)
