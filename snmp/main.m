%getUPSPic("F:\ReportData\东港机房\UPS")
%getTHPic("F:\ReportData\东港机房\TH")
%getEMPic("F:\ReportData\东港机房\EM")
%getCpuPic("F:\ReportData\B2B-Web\system.cpu")
%getNetPic("F:\ReportData\B2B-Web\net")
%getVMPic("F:\ReportData\B2B-Web\vm")
%getSwapPic("F:\ReportData\B2B-Web\system.swap")
%getVfsPic("F:\ReportData\B2B-Web\vfs")
path=("E:\ReportData")
maindir=dir(path)
for i=3:length(maindir)
    itemname=maindir(i).name
    itempath=path+"\"+itemname
    itemdir=dir(itempath)
    for j=3:length(itemdir)
        keyname=itemdir(j).name
        keypath=itempath+"\"+keyname
        switch keyname
            case 'UPS'
                getUPSPic(keypath)
            case 'TH'
                getTHPic(keypath)
            case 'EM'
                getEMPic(keypath)
            case 'system.cpu'
                getCpuPic(keypath)
            case 'system.swap'
                getSwapPic(keypath)
            case 'net'
                getNetPic(keypath)
            case 'vm'
                getVMPic(keypath)
            case 'vfs'
                getVfsPic(keypath)
            case 'tablespace'
                getTablespacePic(keypath)
            case 'session'
                getSessionPic(keypath)
            case 'hitratio'
                getHitratioPic(keypath)
            case 'archive'
                getArchivePic(keypath)
            clear vars keypath keyname 
        end
    end
end
