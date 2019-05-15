import zabbixCom
import matplotlib.pyplot as plt
import numpy as np
import os
import re

#过滤windows中文件夹命名特殊字符
def clearWindowsFilestr(str):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "", str)  # 替换为下划线
    return new_title


def writeDataToFile(hisData,path,itemKey):
    dirlist=[]
    for info in hisData:
        dirname=info
        for item in hisData[info]:
            for data in item:
                tmp=item[data]
                if len(tmp)==7:
                    break
                filename=tmp[4]
                isExists=''
                dir=""
                for i in itemKey:
                    if i in filename:
                        dir=path+dirname+"/"+i
                        isExists=os.path.exists(dir)
                        if not isExists:
                            os.makedirs(dir)
                        break
                unit=tmp[6]
                value=tmp[7]         
                dir=dir+"/"+clearWindowsFilestr(filename)+"_"+unit+".dat"
                dirlist.append(dir)
                print(dir)
                date=clearList(value)
                f=open(dir,'a+')
                for v in date:
                    f.write(str(v[0]))
                    f.write(","+zabbixCom.timeStamp_Time(v[1])+"\n")
                f.close()
    return dirlist

#list中的数据去除时间重复的
def clearList(data):
    value=[]
    for d in data:
        if d not in value:
            value.append(d)
    return value

def getHistoryData(keyword,itemInfo,startTime,endTime,itemKey):
    #print("tool---getHistoryData---"+str(startTime))
    tmpInfo={}
    for item in itemInfo:
        info=itemInfo[item]
        tmp=[]
        for i in info:
            if keyword in i[3]:
                tmp.append(i)
        tmpInfo[item]=tmp
    hisData=zabbixCom.getHistoryDataBaseTime(tmpInfo,startTime,endTime)
    pathList=writeDataToFile(hisData,"E:/ReportData/",itemKey)
    return pathList

def getPic(info):
    for tmp in info:
        # EM-ActivePower_KW    name_unit
        picName=tmp.split("/")[3].split(".")[0].split("_")[0]
        unit=tmp.split("/")[3].split(".")[0].split("_")[1]
        f=open(tmp,'r')
        value=[]
        clock=[]
        for dat in f.readlines():
            a=dat.split(",")
            value.append(a[0])
            #tmp=zabbixCom.timeStamp_Time(int(a[1]))
            clock.append(a[1])
        fig = plt.figure()
        #ax = fig.add_subplot(111)
        x=np.array(clock)
        y=np.array(value)
        plt.plot(x,y,label=picName)
        plt.xlabel("Time")
        plt.ylabel(unit)
        plt.legend()
        plt.title(picName.split("_")[0])
       # plt.xlim(1,100,1)
        plt.gcf().autofmt_xdate()
        plt.show()

def getTHPic():
    print("")

def getPowerPic():
    print("")

def getItemInfo(keyword):
    hostInfo=zabbixCom.getHost()
    itemInfo={}
    for host in hostInfo:
        if keyword in host:
            itemInfo[host]=hostInfo[host]
    return itemInfo

if __name__ == '__main__':
    itemKey=["UPS","TH","EM","PL","net","system.cpu","system.swap","vm","vfs","tablespace","session","hitratio","archive_log"]
    engineRoomInfo=getItemInfo("机房")
    #crmInfo=getItemInfo("CRM")
    itemInfo=zabbixCom.getItemBaseHostID(engineRoomInfo)
    #crmItemInfo=zabbixCom.getItemBaseHostID(crmInfo)
    upsInfo=getHistoryData("UPS",itemInfo,zabbixCom.time_TimeStamp("2019-04-11 08:00:00"),zabbixCom.time_TimeStamp("2019-04-11 12:00:00"),itemKey)
    #thInfo=getHistoryData("TH",itemInfo,zabbixCom.time_TimeStamp("2019-02-02 00:00:00"),zabbixCom.time_TimeStamp("2019-02-02 23:59:59"))
    #emInfo=getHistoryData("EM",itemInfo,zabbixCom.time_TimeStamp("2019-02-02 20:58:00"),zabbixCom.time_TimeStamp("2019-02-02 23:59:59"))
    #getPic(emInfo)
    #crmCPUData=getHistoryData("CPU",crmItemInfo,zabbixCom.time_TimeStamp("2019-02-02 20:58:00"),zabbixCom.time_TimeStamp("2019-02-02 23:59:59"))
    #crmMemData=getHistoryData("disk",crmItemInfo,zabbixCom.time_TimeStamp("2019-02-02 23:50:00"),zabbixCom.time_TimeStamp("2019-02-02 23:59:59"))
    #print(crmMemData)
    #print(clearWindowsFilestr("'E:/ReportData/CRMAPP/vfs.fs.size[/,free]_B.dat'"))
    
    
   
