import pymysql

def openMysql():
    dbCon = pymysql.connect("192.168.80.80","zabbix","zabbix","zabbix" )
    return dbCon

def closeMysql(dbCon):
    dbCon.close()
