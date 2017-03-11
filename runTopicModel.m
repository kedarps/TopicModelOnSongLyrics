close all;

data = importdata('TopicModelData.mat');

WO = [];

for i = 1:size(data.Vocab,1)
    WO = cat(1, WO, cellstr(data.Vocab(i,:)));
end
WO = strrep(WO, 'u2019', '''');
WO = strrep(WO, 'u2018', '''');

artistList = [];

for i = 1:size(data.ArtistList,1)
    artistList = cat(1, artistList, cellstr(data.ArtistList(i,:)));
end
artistList = cellfun(@(x) strsplit(x,'+'), artistList, 'UniformOutput', false);


artistIdx = double(data.ArtistIdx);
WS = double(data.WordIdx);
DS = double(data.DocIdx);


%%
% Set the number of topics
T = 20; 

%%
% Set the hyperparameters
BETA = 0.01;
ALPHA = 50/T;

%%
% The number of iterations
N = 1000; 

%%
% The random seed
SEED = 3;

%%
% What output to show (0=no output; 1=iterations; 2=all output)
OUTPUT = 2;

%%
% This function might need a few minutes to finish
[ WP,DP,Z ] = GibbsSamplerLDA( WS , DS , T , N , ALPHA , BETA , SEED , OUTPUT );

topicsToPlot = T;
nWordsToPlot = 20;

WP = full(WP);
topicPlots = fullfile(pwd, 'TopicPlots');

if ~isdir(topicPlots)
    mkdir(topicPlots)
end

TopicModelResults = struct('WP', WP, 'DP', DP, 'Z', Z, 'ArtistList', {artistList}, 'ArtistIdx', artistIdx);
save('TopicModelResults.mat', 'TopicModelResults');

figure('Position',[1930 15 1900 975]);
iPlot = 1;
for iTopic = 1:10
    topicHere = WP(:,iTopic);
    [sortedTopicHere, sortIdxs] = sort(topicHere,'descend');
    
    subplot(2,5,iPlot);
    iPlot = iPlot + 1;
    barh(flipud(sortedTopicHere(1:nWordsToPlot)));
    set(gca,'YTick',1:nWordsToPlot,'YTickLabel',flipud(WO(sortIdxs(1:nWordsToPlot))),'YTickLabelRotation',-30,'YLim',[0 nWordsToPlot+1],'FontSize',10,'FontWeight','normal');
    title(sprintf('Topic %d',iTopic),'FontSize',18);
end
subplot(2,5,1);
xlabel('Number of occurences','FontSize',14,'FontWeight','bold');
ylabel('Words','FontSize',14,'Rotation',270,'FontWeight','bold');
saveas(gcf,fullfile(topicPlots,['AllTopics_1','.png']));
%%
% Put the most 7 likely words per topic in cell structure S
% [S] = WriteTopics( WP , BETA , WO , 7 , 0.7 );

% fprintf( '\n\nMost likely words in the first ten topics:\n' );

%%
% Show the most likely words in the first ten topics
% S( 1:10 )  

%%
WriteTopics( WP , BETA , WO , 20 , 0.7 , 4 , fullfile(pwd, 'topics.txt') );


