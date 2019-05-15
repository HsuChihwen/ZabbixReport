function [outputArg1] = getArchivePic(path)
%GETARCHIVEPIC �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
outputArg1 = path;

archivedir=dir(path)
archivedata={length(archivedir)-2}
archivetime={length(archivedir)-2}
label={length(archivedir)-2}

for i=3:length(archivedir)
    name=archivedir(i).name()
    label{i-2:i-2}=convertCharsToStrings(name)
    picdir=path+"/ArchiveLog.jpg"
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
    archivetime{:,i-2}=time
    archivedata{:,i-2}=value
    fclose(fileID)
end
Num  = 400;
for i=1:length(label)
   c = rand(Num,3);
   y=label{:,i}
   tmp=split(y,"_")
   picname=tmp{1,:}
   
   time=archivetime{:,i}
   value=archivedata{:,i}
   plot(time,value,"-",'color',c(i*2,:))
   xlabel("TIME")
   ylabel("%")
   grid on
   hold on
end
legend(label,'Location','southoutside','NumColumns',4)
legend('boxoff')
title("ArchiveLog")
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperUnits', 'points');
set(gcf, 'PaperPosition', [0 0 640 480]);
print(gcf,'-djpeg',picdir)
hold off
clear 
cla
clf
end

