import mysqlConn
import pymysql
import sys
import time


#select FROM_UNIXTIME(history_uint.clock),history_uint.`value` from history_uint where history_uint.itemid=39399
def getHost():
    dbCon = mysqlConn.openMysql()
    cursor = dbCon.cursor()
    sql = "select `hosts`.hostid,`hosts`.host,`hosts`.name  from hosts where `hosts`.status=0 and `hosts`.flags=0 GROUP BY `hosts`.hostid"
    hostInfo={}
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
           info=[]
           info.append(row)
           hostInfo[row[2]]=info
       dbCon.close()
    except:
        dbCon.close()
        print ("Error: unable to fetch data")
    return hostInfo

def getItemBaseHostID(hostInfo):
    dbCon = mysqlConn.openMysql()
    cursor = dbCon.cursor()
    itemInfo={}
    for hostname in hostInfo:
        host=hostInfo[hostname]
        for value in host:
            sql="select items.itemid,items.snmp_oid,items.hostid,items.`name`,key_,value_type,units from items where items.hostid="+str(value[0])+" and items.flags!=2"
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                info=[]
                for row in results:
                    info.append(row)
                    itemInfo[value[2]]=info
            except IndexError as e:
               print( e)
    return itemInfo
               
def getHistoryDataBaseTime(itemInfo,startTime,endTime):
    
    hisData={}
    for name in itemInfo:
        hostmap=[]
        hostname=name
        for item in itemInfo[name]:
            dbCon = mysqlConn.openMysql()
            cursor = dbCon.cursor()
            #过滤没有单位的type和status类型的数值
            if 'Type' in item[3] or "Status" in item[3] :
                continue
            itemmap={}
            tmp=[]
            #只查询数值类型的数据
            if item[5]==0 :
                table="history"
            elif item[5]==3:
                table="history_uint"
            else:
                continue
            #print("zabbixCom---getHistoryDataBaseTime---"+str(startTime))
            sql="select "+ table+".value, "+table+".clock from "+ table+",items where ("+table+".clock between "+str(startTime)+" and "+str(endTime)+" ) and "+table+".itemid="+str(item[0])+" and items.hostid="+str(item[2])
            #print(sql)
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                value=[]
                clock=[]
                tmp.append(item[0])
                tmp.append(item[1])
                tmp.append(item[2])
                tmp.append(item[3])
                tmp.append(item[4])
                tmp.append(item[5])
                tmp.append(item[6])
                for row in results:
                    if row[0] =='':
                        break
                    else:
                        tmp.append(results)
                        break
                    #value.append(row[0])
                    #clock.append(row[1])
                #tmp.append(value)
                #tmp.append(clock)
            except IndexError as e:
               print( e)
            mysqlConn.closeMysql(dbCon)
            itemmap[item[0]]=tmp
            hostmap.append(itemmap)
        hisData[name]=hostmap
    return hisData


def time_TimeStamp(dt):
    '''时间戳转换
    time to timestamp
    param dt:time 2018-09-01 08:00:00
    '''
    time.strptime(dt,"%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(time.strptime(dt,"%Y-%m-%d %H:%M:%S"))
    return int(timestamp)

def timeStamp_Time(timestamp):
    time_local = time.localtime(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

if __name__ == '__main__':
    HostInfo=getHost()
    ItemInfo=getItemBaseHostID(HostInfo)
    print(getHistoryDataBaseTime(ItemInfo,time_TimeStamp("2018-12-01 00:00:00"),time_TimeStamp("2018-12-30 08:00:00")))


    