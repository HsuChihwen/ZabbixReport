
import matlab
import matlab.engine
import os
import time
import numpy as np
import zabbixCom
 


#eng=matlab.engine.start_matlab()
#mat=eng.fspecial('gaussian',matlab.double([100,100]),3.0)
#eng.mesh(mat)
#time.sleep(3)

path="E:\\ReportData\\"

def timestampTotime(clock):
    value=[]
    for time in clock:
        value.append(zabbixCom.timeStamp_Time(int(time)))
    return value

def getPic(x,y,picitem):
    picname=picitem.split(".")[0]
    unit=picitem.split(".")[1]
    print("picName---->"+picname)
    print ("Initializing Matlab Engine")
    eng=matlab.engine.start_matlab()
    print ("Initializing Complete!")
    x1=np.array(x)
    y1=np.array(y)
    print(type(x1.tolist()))
    eng.workspace['a']=x1
    eng.workspace['b']=y1
    eng.workspace['unit']=unit
    #a=eng.linspace(x)
    #b=eng.linspace(y)
    
    eng.plot(x1.tolist(),y1.tolist())
    #eng.eval("plot(a,b)",nargout=0)
    
    #eng.hold('on',nargout=0)
    #eng.figure(nargout=0)
    #eng.hold('on',nargout=0)
    eng.quit()


def getDataFromFile(path):

    files=os.listdir(path)
    for file in files:
        for item in os.listdir(path+file):
            value=[]
            c=[]
            dir=path+file+"\\"+item
            f=open(dir,'r')
            iter_f = iter(f); #创建迭代器
            for line in iter_f: #遍历文件，一行行遍历，读取文本
                value.append(line.split(' ')[0])
                c.append(line.split(' ')[1])
            clock=timestampTotime(c)
            print("len(value)---->"+str(len(value)))
            print("len(clock)---->"+str(len(clock)))
            print("file---->"+file)
            print("item---->"+item)
            print("value---->"+str(value))
            
            getPic(clock,value,item)



       




if __name__ == '__main__':
    path="E:\\ReportData\\"
    getDataFromFile(path)
