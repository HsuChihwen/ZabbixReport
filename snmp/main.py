import vCenter
import zabbixCom
import veeam
import S7703
import tool
import datetime
from datetime import datetime, date, timedelta
import calendar
import time


def getHistory(hostItem,startTime,endTime,itemKey):
    for host in hostItem:
        hostname=host
        print("查询日期:"+str(startTime)+" -- "+str(endTime))
        print("查询主机"+" -- "+hostname)
        item=hostItem[host]
        for info in item:
            itemInfo=tool.getItemInfo(hostname)
            hostitem=zabbixCom.getItemBaseHostID(itemInfo)
            #print("starTime---->"+str(startTime))
            pathList=tool.getHistoryData(info,hostitem,zabbixCom.time_TimeStamp(startTime),zabbixCom.time_TimeStamp(endTime),itemKey)
            #tool.getPic(pathList)

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

def getDayofThisMonth():
    dayList=[]
    first_day, last_day = get_month_range()
    for d in date_range(datetime(first_day.year,first_day.month,first_day.day), datetime(last_day.year,last_day.month,last_day.day),
                        timedelta(hours=24)):
        dayList.append(d)

    return dayList




if __name__ == '__main__':
    engine=["UPS","TH","EM","FL","Switch"]
    host=["CPU","memory","swap","network","disk","load","tablespace","archive_log","Sessions","ratio"]
    hostItem={"机房":engine,"CRM":host,"OA":host,"B2B":host,"Warehousing":host,"ERP":host}
    itemKey=["UPS","TH","EM","PL","net","system.cpu","system.swap","vm","vfs","tablespace","session","hitratio","archive"]
    dayList=getDayofThisMonth()
    for i in range(len(dayList)):
        startTime=dayList[i]
        if i == len(dayList)-1:
            d=dayList[i]
            year=d.year
            month=d.month+1
            day=1
            hour=d.hour
            min=d.minute
            sec=d.second
            endTime=datetime(year,month,day)
        else:
            endTime=dayList[i+1]
        getHistory(hostItem,str(startTime),str(endTime),itemKey)
    





