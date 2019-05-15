import requests
import xml
import json
from requests.auth import HTTPBasicAuth
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
        
            
def getCookies():
    url='url'
    r=requests.post(url,auth=('username','password'))
    cookies=requests.utils.dict_from_cookiejar(r.cookies)
    return cookies

def getLastSevenDaysJobsInfo(url,cookies):
    r=requests.get(url,cookies=cookies,auth=('username','password'))
    tree=ET.fromstring(r.content)
    lastSevenDaysJobsInfo=[]
    for child in tree:
        lastSevenDaysJobsInfo.append(child.attrib)
    return lastSevenDaysJobsInfo
    

def getDiskCapInfo(url,cookies):
    r=requests.get(url,cookies=cookies,auth=('username','password')))
    root = ET.fromstring(r.content)
    diskCapInfo={}
    name=root[0][0].tag
    diskCapInfo[name.split('}')[1]]=root[0][0].text # name
    capacity=root[0][1].tag
    diskCapInfo[capacity.split('}')[1]]=root[0][1].text # Capacity
    freeSpace=root[0][2].tag
    diskCapInfo[freeSpace.split('}')[1]]=root[0][2].text # FreeSpace
    backupSize=root[0][3].tag
    diskCapInfo[backupSize.split('}')[1]]=root[0][3].text # BackupSize
    return diskCapInfo

def getVMSOverview(url,cookies):
    r=requests.get(url,cookies=cookies,auth=('username','password')))
    root = ET.fromstring(r.content)
    vmsOverview={}
    for child in root:
        tag=child.tag
        text=child.text
        vmsOverview[tag.split('}')[1]]=text
    return vmsOverview
    
    
    
    
