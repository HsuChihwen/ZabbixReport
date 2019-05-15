import pymysql

def openMysql():
    dbCon = pymysql.connect("IPAddress","username","Password","database" )
    return dbCon

def closeMysql(dbCon):
    dbCon.close()
