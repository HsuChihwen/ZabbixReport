import time
import json
import urllib.request as urllib2


def zabbixLogin(user,passwd):
    '''use zabbixAPI login

    param url:str
    param user:str
    param passwd:str

    return:AuthID
    '''
    data = json.dumps({"jsonrpc":"2.0","method":"user.login","id":1,"params":{"user":"admin","password":"zabbix"}}).encode(encoding='utf_8', errors='strict')
    res_json = get_Request(data)
    return res_json['result']

def get_Request(jsondata):
    '''send requset to zabbix and get response
    param jsondata: json string
      example :{"jsonrpc":"2.0","method":"host.get","id":2,"auth":authID,"params":{"output":"extend"}}
    '''
    url="http://zabbix.xingyun361.com/zabbix/api_jsonrpc.php"
    header = {"Content-Type": "application/json-rpc"}
    request = urllib2.Request(url,jsondata)
    for key in header:
        request.add_header(key,header[key])
    res = urllib2.urlopen(request,timeout=50)
    res_str = res.read().decode('utf-8')
    res_json = json.loads(res_str)
    return res_json



def get_Host(authID):
    '''get all host expect status=1
    0 - (默认) 已监控的主机;
    1 - 未监控的主机
    param authID:str
    return: HostInfo:list[dict]
    example:[{'host': '10.0.0.1', 'hostid': '10107', 'name': 'CoreSwitch-S7703'}, 
    {'host': 'admin.xingyun361.com', 'hostid': '10108', 'name': 'B2B-Admin'}]
    '''
    data=json.dumps({"jsonrpc":"2.0","method":"host.get","id":2,"auth":authID,"params":{"output":"extend","filter":{"status":"0"}}}).encode(encoding='utf_8', errors='strict')
    res_json = get_Request(data)
    HostInfo=[]
    for value in res_json['result']:
        info={}
        info['host']=value['host']
        info['hostid']=value['hostid']
        info['name']=value['name']
        HostInfo.append(info)
    return HostInfo

def get_Itemprototype(authID):
    '''get item value
    param authID:str
    return ItemInfo:list[dict]
    example:[{'itemid': '28675', 'hostid': '10156', 'name': 'Incoming network traffic on $1', 'key_': 'net.if.in[{#IFNAME}]'}]
    '''
    data=json.dumps({"jsonrpc":"2.0","method":"itemprototype.get","id":2,"auth":authID,"params":{"output":"extend"}}).encode(encoding='utf_8', errors='strict')
    res_json = get_Request(data)
    ItemInfo=[]
    for value in res_json['result']:
        info={}
        info['itemid']=value['itemid']
        info['hostid']=value['hostid']
        info['name']=value['name']
        info['key']=value['key_']
        ItemInfo.append(info)
    return ItemInfo

def get_HistoryData(authID,startTime,endTime,itemid,hostid):
    data=json.dumps({"jsonrpc":"2.0","method":"history.get","id":1,"auth":authID,"time_from":startTime,"time_till":endTime,"itemids":itemid,"hostids":hostid,"params":{"output":"extend","history": 0,"limit":990000}}).encode(encoding='utf_8', errors='strict')
    res_json = get_Request(data)
    print(res_json)

def getHostIDFromName(authID,name):
    '''getHostID based hostname
    param authID:str
    param name:str zabbix中的主机名称
    return:获取关于这个主机的所有数据
    '''
    data=json.dumps({"jsonrpc":"2.0","method": "host.get","params": {"output":"extend","filter": { "host":[name]}},"auth": authID,"id":1}).encode(encoding='utf_8', errors='strict')
    res_json = get_Request(data)
    return res_json['result']

def getItemIDFromHostID(authID,HostID):
    data=json.dumps({"jsonrpc": "2.0","method": "item.get","params": {"output": "extend","hostids": HostID},"auth":authID,"id":1}).encode(encoding='utf_8', errors='strict')
    res_json = get_Request(data)
    return res_json['result']
    

def getAllHostInfoBaseHostAndItem(hostInfo,itemInfo):
    result={}
    for host in hostInfo:
        hostid=host['hostid']
        value=[]
        for item in itemInfo:
            if hostid==item['hostid']:
                value.append(item)
        result[host['name']]=value
    return result




def time_TimeStamp(dt):
    '''时间戳转换
    time to timestamp
    param dt:time 2018-09-01 08:00:00
    '''
    time.strptime(dt,"%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(time.strptime(dt,"%Y-%m-%d %H:%M:%S"))
    return int(timestamp)

def getAllData():
    url=""
    user="admin"
    passwd="zabbix"
    authID = zabbixLogin(user,passwd)
    HostInfo=[]
    temp=get_Host(authID)
    for value in temp:
        info={}
        info['host']=value['host']
        info['hostid']=value['hostid']
        info['name']=value['name']
        HostInfo.append(info)
    return HostInfo
   
