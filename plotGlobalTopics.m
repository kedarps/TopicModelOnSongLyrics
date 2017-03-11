txt = 'TopicProportions.txt';
fid = fopen(txt);

topics = [];
topicNames = [];
topicProps = [];

while ~feof(fid)
    tline = fscanf(fid,'%s;%s;%s');
    
    if ~isempty(tline)
        tlineSplit = strsplit(tline,';');
        
        topics = cat(1, topics, tlineSplit(1));
        topicProps = cat(1, topicProps, str2double(tlineSplit{2}));
        topicNames = cat(1, topicNames, tlineSplit(3));
    end
end

fclose(fid);

bar(1:20, topicProps);
xlim([0 21]);
set(gca,'XTick', 1:20, 'XTickLabel',topicNames,'XTickLabelRotation',60,'FontSize',14);
xlabel('Topics');
ylabel('Probability');
title('Corpus wide topic proportions');

