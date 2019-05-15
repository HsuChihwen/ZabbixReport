function [outputArg1] = getVMPic(path)
%GETVMPIC �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
outputArg1 = path;
vmdir=dir(path)
vmdata={length(vmdir)-2}
vmtime={length(vmdir)-2}
label={length(vmdir)-2}

for i=3:length(vmdir)
    name=vmdir(i).name()
    label{i-2:i-2}=convertCharsToStrings(name)
    picdir=path+"/VM.jpg"
    delimiter=',';
    formatSpec = '%q%q%[^\n\r]';
    filedir=path+"/"+name
    
    fileID = fopen(filedir,'r');
    dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter, 'TextType', 'string',  'ReturnOnError', false);
    dates{2} = datetime(dataArray{2}, 'Format', 'yyyy-MM-dd HH:mm:ss', 'InputFormat', 'yyyy-MM-dd HH:mm:ss');
    dates = dates(:,2);
    time = dates{:, 1};
    value=str2double(dataArray{:,1})
    %tmp={time,value}
    vmtime{:,i-2}=time
    vmdata{:,i-2}=value
    fclose(fileID)
end
Num  = 400;
for i=1:length(label)
   c = rand(Num,3);
   y=label{:,i}
   tmp=split(y,"_")
   picname=tmp{1,:}
   unit="M"
   time=vmtime{:,i}
   value=vmdata{:,i}/1000000
    %ax.Color=i*5
   plot(time,value,"-",'color',c(i*2,:))
   xlabel("TIME")
   ylabel(unit)
   grid on
   hold on
end
legend(label,'Location','southoutside','NumColumns',length(label))
legend('boxoff')
title("VM")
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperUnits', 'points');
set(gcf, 'PaperPosition', [0 0 640 480]);
print(gcf,'-djpeg',picdir)
hold off
clear
cla
clf
end

