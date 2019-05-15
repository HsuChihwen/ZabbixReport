function [outputArg1] = getNetPic(path)
%GETNETPIC 此处显示有关此函数的摘要
%   此处显示详细说明
outputArg1 = path;
netdir=dir(path)
netdata={length(netdir)-2}
nettime={length(netdir)-2}
label={length(netdir)-2}


for i=3:length(netdir)
    name=netdir(i).name()
    label{i-2:i-2}=convertCharsToStrings(name)
    picdir=path+"/Net.jpg"
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
    nettime{:,i-2}=time
    netdata{:,i-2}=value
    fclose(fileID)
end
Num  = 400;
for i=1:length(label)
   c = rand(Num,3);
   y=label{:,i}
   tmp=split(y,"_")
   picname=tmp{1,:}
   unit="Mbps"
   time=nettime{:,i}
   value=netdata{:,i}/1000000
    %ax.Color=i*5
   plot(time,value,"-",'color',c(i*2,:))
   xlabel("TIME")
   ylabel(unit)
   grid on
   hold on
end
legend(label,'Location','southoutside','NumColumns',length(label))
legend('boxoff')
title("Net-In/Out")
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperUnits', 'points');
set(gcf, 'PaperPosition', [0 0 640 480]);
print(gcf,'-djpeg',picdir)
hold off
clear
cla
clf
end

