clear all, clc
load('test.mat')

figure('visible','off','Position',[0 0 540 960])
for i=1:size(data,1)
    imagesc(reshape(data(i,:,:),[size(data,2, 3)]))
    i
    hold on
    colormap gray
    xticks([])
    yticks([])
    xticklabels([])
    yticklabels([])
    axis off
    set(gca,'LooseInset',get(gca,'TightInset'));
    set(gcf,'InvertHardCopy','off','Color','black');    
    F(i) = getframe(gcf) ;
    drawnow   
end

% create the video writer with 1 fps
writerObj = VideoWriter('game_of_life_1.mp4','MPEG-4');
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
