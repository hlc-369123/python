#!/bin/env python

"""
SNMPv1 TRAP with defaults
+++++++++++++++++++++++++

Send SNMPv1 TRAP through unified SNMPv3 message processing framework
using the following options:

* SNMPv1
* with community name 'public'
* over IPv4/UDP
* send TRAP notification
* with Generic Trap #1 (warmStart) and Specific Trap 0
* with default Uptime
* with default Agent Address
* with Enterprise OID 1.3.6.1.4.1.20408.4.1.1.2
* include managed object information '1.3.6.1.2.1.1.1.0' = 'my system'

Functionally similar to:
$ snmptrap -v1 -c public demo.snmplabs.com 1.3.6.1.4.1.20408.4.1.1.2 0.0.0.0 1 0 0 1.3.6.1.2.1.1.1.0 s "my system"
"""#
from pysnmp.hlapi import *
import os
import re

def alarm_pools_width(alarm_meassage):
	errorIndication, errorStatus, errorIndex, varBinds = next(
    		sendNotification(
        		SnmpEngine(),
        		CommunityData('public', mpModel=0),
        		UdpTransportTarget(('172.16.153.42', 162)),
        		ContextData(),
        		'trap',
        		NotificationType(
            			ObjectIdentity('1.3.6.1.6.3.1.1.5.1')
        			).addVarBinds(
            				('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.1'),
            				('1.3.6.1.2.1.1.1.0', OctetString(alarm_meassage))
        				)
	    		)
		)
	if errorIndication:
    		print(errorIndication)


def alarm_buckets_width(alarm_meassage):
        errorIndication, errorStatus, errorIndex, varBinds = next(
        sendNotification(
                SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('172.16.153.42', 162)),
                ContextData(),
                'trap',
                NotificationType(
                ObjectIdentity('1.3.6.1.6.3.1.1.5.1')
                ).addVarBinds(
                        ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2'),
                        ('1.3.6.1.2.1.1.1.0', OctetString(alarm_meassage))
                )
        )
        )

        if errorIndication:
                print(errorIndication)


def alarm_nfs_gateway(alarm_meassage):
        errorIndication, errorStatus, errorIndex, varBinds = next(
        sendNotification(
                SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('172.16.153.42', 162)),
                ContextData(),
                'trap',
                NotificationType(
                ObjectIdentity('1.3.6.1.6.3.1.1.5.1')
                ).addVarBinds(
                        ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.3'),
                        ('1.3.6.1.2.1.1.1.0', OctetString(alarm_meassage))
                )
        )
        )

        if errorIndication:
                print(errorIndication)





alarm_meassage = os.popen('/root/alarm_gen.sh').read()

alarm_type = re.search("([\w']+)", alarm_meassage).group(1)


switch_alarm = {
		'pool' : alarm_pools_width,
		'bucket' : alarm_buckets_width,
		'NFS' : alarm_nfs_gateway
}

try:
	switch_alarm[alarm_type](alarm_meassage)
except KeyError as e:
	print "Here is noting to send Notification!"
	pass 

