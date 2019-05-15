function [outputArg1] = getVfsPic(path)
%GETSWAPPIC 此处显示有关此函数的摘要
%   此处显示详细说明
outputArg1 = path;

vfsdir=dir(path)
vfsdata={length(vfsdir)-2}
vfstime={length(vfsdir)-2}
label={length(vfsdir)-2}

for i=3:length(vfsdir)
    name=vfsdir(i).name()
    label{i-2:i-2}=convertCharsToStrings(name)
    picdir=path+"/VFS.jpg"
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
    vfstime{:,i-2}=time
    vfsdata{:,i-2}=value
    fclose(fileID)
end
Num=40

for i=1:length(label)
   c = rand(Num,3); 
   y=label{:,i}
   tmp=split(y,"_")
   picname=tmp{1,:}
   tmp_unit=tmp{2,:}
   tmp_unit=split(tmp_unit,".")
   unit=tmp_unit{1:1}
   if strcmp("%",unit)
       continue
   end
   time=vfstime{:,i}
   value=vfsdata{:,i}/1000000000
   %ax.Color=i*3
   plot(time,value,"-",'color',c(i,:))
   xlabel("TIME")
   ylabel("GB")
   grid on
   hold on
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
   if ~ strcmp("%",unit)
       yyaxis right
       ylim([0,100])
   end
   time=vfstime{:,i}
   value=vfsdata{:,i}
    %ax.Color=i*5
   plot(time,value,"-",'color',c(i*2,:))
   xlabel("TIME")
   ylabel("%")
   grid on
   hold on
end
legend(label,'Location','southoutside','NumColumns',4)
legend('boxoff')
title("VFS")
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperUnits', 'points');
set(gcf, 'PaperPosition', [0 0 640 480]);
print(gcf,'-djpeg',picdir)
hold off
clear
cla
clf
end

