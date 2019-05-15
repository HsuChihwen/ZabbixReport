import snmpCom


def getS7703BaseInfo(SnmpHost,SnmpPort,SnmpCommunity):
    value={}
    descMIB=["SNMPv2-MIB","sysDescr","0"]
    upTimeMIB=["SNMPv2-MIB","sysUpTime","0"]
    sysContactMIB=["SNMPv2-MIB","sysContact","0"]
    sysNameMIB=["SNMPv2-MIB","sysName","0"]
    sysLocationMIB=["SNMPv2-MIB","sysLocation","0"]
    value['sysDescr']=snmpCom.snmpGetCmd(SnmpHost,SnmpPort,SnmpCommunity,descMIB)
    value['sysUpTime']=snmpCom.snmpGetCmd(SnmpHost,SnmpPort,SnmpCommunity,upTimeMIB)
    value['sysContact']=snmpCom.snmpGetCmd(SnmpHost,SnmpPort,SnmpCommunity,sysContactMIB)
    value['sysName']=snmpCom.snmpGetCmd(SnmpHost,SnmpPort,SnmpCommunity,sysNameMIB)
    value['sysLocation']=snmpCom.snmpGetCmd(SnmpHost,SnmpPort,SnmpCommunity,sysLocationMIB)
    return value


if __name__ == '__main__':
    S7703_SnmpHost="10.0.0.1"
    S7703_SnmpPort=161
    S7703_SnmpCommunity="zabbix"
    baseInfo=getS7703BaseInfo(S7703_SnmpHost,S7703_SnmpPort,S7703_SnmpCommunity)
    