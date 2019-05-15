from pysnmp.hlapi import *
from pysnmp.smi import *
from pysnmp import *


def snmpGetCmd(Host, Port, Community, MIB=[]):
    value=""
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in getCmd(SnmpEngine(),
                              CommunityData(Community, mpModel=0),
                              UdpTransportTarget((Host,Port)),
                              ContextData(),
                              ObjectType(ObjectIdentity(MIB[0],MIB[1],MIB[2]).addAsn1MibSource('file:///usr/share/snmp','http://mibs.snmplabs.com/asn1/@mib@'))):
        if errorIndication or errorStatus:
            print(errorIndication or errorStatus)
            break
        else:
            for varBind in varBinds:
                temp=str(varBind).split('=')
                value=temp[1]
    return value   


def snmpbulkCmd(Host,Port,Community,MIB=[]):
    value={}
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in bulkCmd(SnmpEngine(),
                              CommunityData(Community, mpModel=0),
                              UdpTransportTarget((Host,Port)),
                              ContextData(),
                              0,20,
                              ObjectType(ObjectIdentity(MIB[0],MIB[1]).addAsn1MibSource('file:///usr/share/snmp','http://mibs.snmplabs.com/asn1/@mib@'))):
        if errorIndication or errorStatus:
            print(errorIndication or errorStatus)
            break
        else:
            for varBind in varBinds:
                temp=str(varBind).split('=')
                value[temp[0]]=temp[1]
    return value


def snmpNextCdm(Host,Port,Community,MIB=[]):
    value={}
    for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData(Community, mpModel=0),
                          UdpTransportTarget((Host, Port)),
                          ContextData(),
                          ObjectType(ObjectIdentity(MIB[0], MIB[1])),
                          lexicographicMode=False):

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                temp=str(varBind).split('=')
                value[temp[0]]=temp[1]
    return value
