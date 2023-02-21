% Lets see how it goes
clear all, clc

patient_number=1;
filename=strcat("eeg",num2str(patient_number),".edf");

annotations=load("annotations_2017.mat");
annotations=annotations.annotat_new{1,patient_number};

% making the votation of the three annotators
annotations=1.0*(mean(annotations)>0);

[eeg, ~, ~, ~, ~, ~]=read_edf(filename);
channels=["Fp","Fp2",'F3','F4','C3','C4','P3','P4','O1','O2','F7','F8','T3','T4','T5','T6','Fz','Cz','Pz'];
fs=256;

% retrieve the data
eeg_data=[];
for i=1:length(channels)
    eeg_channel=eeg{1,i};
    eeg_channel=preprocess(eeg_channel); % preprocess each channel
    
    eeg_channel=zscore(eeg_channel);
    eeg_data=[eeg_data; eeg_channel];
end

% putting each EEG channel in one specific height
for i=1:length(channels)
    eeg_data(i,:)=eeg_data(i,:)+i;
end

clear eeg_channel
clear eeg


figure('visible','on','Position',[0 0 540 960])
starting_index=49000;
ending_index=starting_index+fs*5;
step=3;
for i=1:2850
    for j=1:length(channels)
        plot(eeg_data(j,starting_index:ending_index),"Color","white")
        hold on
    end
    hold off
    set(gca,'LooseInset',get(gca,'TightInset'));
    axis off
    set(gcf,'InvertHardCopy','off','Color','black');
    yticks(linspace(1,19,19))
    yticklabels(channels)
    ylim([0,20])
    xticks([])
    xlim([1,fs*5])
    F(i) = getframe(gcf) ;
    drawnow
    
    starting_index=starting_index+step;
    ending_index=ending_index+step;
end


% create the video writer with 1 fps
writerObj = VideoWriter('eeg_step3.mp4','MPEG-4');
writerObj.FrameRate = 10;
% set the seconds per image
% open the video writer
open(writerObj);
% write the frames to the video
for i=1:length(F)
    % convert the image to a frame
    frame = F(i) ;
    writeVideo(writerObj, frame);
end
% close the writer object
close(writerObj);
