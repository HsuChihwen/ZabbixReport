function [outputArg1] = getCpuPic(path)
%GETCPUPIC �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
outputArg1 = path;
cpudir=dir(path)
cpudata={length(cpudir)-2}
cputime={length(cpudir)-2}
label={length(cpudir)-2}

for i=3:length(cpudir)
    name=cpudir(i).name()
    label{i-2:i-2}=convertCharsToStrings(name)
    picdir=path+"/CPU.jpg"
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
    cputime{:,i-2}=time
    cpudata{:,i-2}=value
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
   if ~ strcmp("%",unit)
       yyaxis right
       ylim([0,100])
   end
   time=cputime{:,i}
   value=cpudata{:,i}
    %ax.Color=i*5
   plot(time,value,"-",'color',c(i*2,:))
   xlabel("TIME")
   grid on
   hold on
end
legend(label,'Location','southoutside','NumColumns',4)
legend('boxoff')
title("CPU-Load/Util")
hold off
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperUnits', 'points');
set(gcf, 'PaperPosition', [0 0 640 480]);
print(gcf,'-djpeg',picdir)

clear
cla
clf
end

