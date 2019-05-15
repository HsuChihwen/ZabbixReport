import atexit
from pyVmomi import vim,vmodl
from pyVim.connect import SmartConnectNoSSL,Disconnect
from pyVim.connect import SmartConnect
import operator
import time
from datetime import timedelta

def vCenterLogin(host,user,pwd,port):
    try:
        si = SmartConnectNoSSL(host=host, user=user, pwd=pwd, port=port)
        #si = SmartConnect(host=host, user=user, pwd=pwd, port=port)
        atexit.register(Disconnect, si)
        content = si.RetrieveContent()
        time=si.CurrentTime()
    except vmodl.MethodFault as error:
        print ("Caught vmodl fault : " + error.msg)
        return False, error.msg
    return content


def getDatastores(content):
    Datastores={}
    for datacenter in content.rootFolder.childEntity:
        datastores = datacenter.datastore
        datastore_Info={}
        for ds in datastores:
            datastore_Info={}
            name=ds.summary.name
            if name.find("datastore1",0,len(name))!=0:
                datastore_Info["name"]=ds.summary.name
                datastore_Info["datastore"]=ds.summary.datastore
                datastore_Info["url"]=ds.summary.url
                datastore_Info["capacity"]=ds.summary.capacity
                datastore_Info["freeSpace"]=ds.summary.freeSpace
                datastore_Info["uncommitted"]=ds.summary.uncommitted
                datastore_Info["type"]=ds.summary.type
                datastore_Info["mantenanceMode"]=ds.summary.maintenanceMode
                Datastores[ds.summary.name]=datastore_Info
    return Datastores

            

def getHosts(content):
    hostsInfo={}
    for datacenter in content.rootFolder.childEntity:
        if hasattr(datacenter.hostFolder, 'childEntity'):
            hostFolder = datacenter.hostFolder
            computeResourceList = []
            computeResourceList = getComputeResource(hostFolder,computeResourceList)
            for computeResource in computeResourceList:
               hostlist=computeResource.host
               for host in hostlist:
                   info={}
                   info['biosVersion']=host.hardware.biosInfo.biosVersion
                   info['quickStats']=host.summary.quickStats
                   info['uptime']=host.summary.quickStats.uptime
                   info['name']=host.name
                   info['network']=host.network
                   info['vm']=host.vm
                   info['memory']=host.hardware.memorySize
                   info['cpu']=host.hardware.cpuPkg[0].description
                   info['cpu_hz']=host.hardware.cpuPkg[0].hz
                   info['cpu_cores']=host.hardware.cpuInfo.numCpuCores
                   info['cpu_packages']=host.hardware.cpuInfo.numCpuPackages
                   info['cpu_threads']=host.hardware.cpuInfo.numCpuThreads
                   info['model']=host.hardware.systemInfo.model
                   info['vendor']=host.hardware.systemInfo.model
                   hostsInfo[host.name]=info
    return hostsInfo
               

def getPerfManager(content,interval,startTime,endTime):
    perf_dict = {}
    perfList = content.perfManager.perfCounter
    for counter in perfList:
        counter_full = "{}.{}.{}".format(counter.groupInfo.key, counter.nameInfo.key, counter.rollupType)
        perf_dict[counter_full] = counter.key
    print(BuildQuery(content, time.time(), (perf_id(perf_dict, 'net.transmitted.average')), "", "10.10.10.205", 60))

def BuildQuery(content, startTime,endTime,entity,intervalId):
    result={}
    perfManager = content.perfManager
    metricId = vim.PerformanceManager.MetricId(counterId=counterId, instance=instance)
    startTime = vchtime 
    endTime = vchtime 
    obj=content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    for vm in obj.view:
        query = vim.PerformanceManager.QuerySpec(entity=vm)
        perfResults = perfManager.QueryPerf(querySpec=[query])
        result[vm.name]=perfResults
    return result


def perf_id(perf_dict, counter_name):
    counter_key = perf_dict[counter_name]
    return counter_key

def getVM(content):
    obj = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vmInfo={}
    for vm in obj.view:
        vm_name=vm.name
        list=[]
        for datastore in vm.datastore:
            list.append(datastore.name)
        vmInfo[vm_name]=list
    return vmInfo
            
        
             

def getComputeResource(Folder,computeResourceList):
    if hasattr(Folder, 'childEntity'):
        for computeResource in Folder.childEntity:
            getComputeResource(computeResource,computeResourceList)
    else:
        computeResourceList.append(Folder)
    return computeResourceList

if __name__ == "__main__":
    host = "vcenter.xingyun361.com"
    user = "administrator@vsphere.local"
    pwd = "Zhd@esxi.com2016"
    port = "443"
    content=vCenterLogin(host,user,pwd,port)
    datastoresInfo=getDatastores(content)
    getHosts=getHosts(content)
    #getPerfManager(content,60,"20190221","20190221")
    vmInfo=getVM(content)
    print(getHosts)
