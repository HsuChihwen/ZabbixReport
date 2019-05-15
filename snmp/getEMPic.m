function [outputArg1] = getEMPic(path)
%GETEMPIC 此处显示有关此函数的摘要
%   此处显示详细说明
outputArg1 = path;
emdir=dir(path)
emdata={length(emdir)-2}
emtime={length(emdir)-2}
label={length(emdir)-2}
for i=3:length(emdir)
    name=emdir(i).name()
    label{i-2:i-2}=convertCharsToStrings(name)
    picdir=path+"/EM.jpg"
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
    emtime{:,i-2}=time
    emdata{:,i-2}=value
    fclose(fileID)
end
Num  = 400;
for i=1:length(label)
   c = rand(Num,3);
   y=label{:,i}
   tmp=split(y,"_")
   picname=tmp{1,:}
   tmp_unit=tmp{2,:}
   tmp_unit=split(tmp_unit,".")
   unit=tmp_unit{1:1}
   if ~ strcmp("KW",unit)
       yyaxis right
       ylim([0,inf])
   end
   time=emtime{:,i}
   value=emdata{:,i}
    %ax.Color=i*5
   plot(time,value,"-",'color',c(i*2,:))
   xlabel("TIME")
   grid on
   hold on
end
legend(label,'Location','southoutside','NumColumns',length(label)/2)
legend('boxoff')
title("EM")
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperUnits', 'points');
set(gcf, 'PaperPosition', [0 0 640 480]);
print(gcf,'-djpeg',picdir)
hold off
clear
cla
clf
end

