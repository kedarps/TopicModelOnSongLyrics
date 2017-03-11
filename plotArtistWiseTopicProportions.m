txt = 'TopicProportions.txt';
fid = fopen(txt);

topicNames = [];

while ~feof(fid)
    tline = fscanf(fid,'%s;%s;%s');
    
    if ~isempty(tline)
        tlineSplit = strsplit(tline,';');
        topicNames = cat(1, topicNames, tlineSplit(3));
    end
end

fclose(fid);

results = importdata('TopicModelResults.mat');

allTopicAssignments = results.Z;
artistIdx = results.ArtistIdx;
for iArtist = 1:length(results.ArtistList)
    thisArtist = strjoin(results.ArtistList{iArtist});
    thisArtistIdx = (artistIdx == iArtist);
    thisArtistZ = allTopicAssignments(thisArtistIdx);
    
    h = histcounts(thisArtistZ,20);
    h = h./sum(h);
    
    subplot(1,15,iArtist);
    barh(h);
    
    if iArtist == 1
        set(gca,'YTick', 1:20, 'YTickLabel',topicNames,'YTickLabelRotation',00,'FontSize',12);
    else
        set(gca,'YTick', 1:20, 'YTickLabel',[]);
    end
    
    axis tight;
    title(sprintf('%s',thisArtist),'FontSize', 11);
end