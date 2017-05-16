# Latent Dirichlet allocation applied to song lyrics data

Uses Python to extract and process lyrics text data from [lyricsfreak.com](http://www.lyricsfreak.com/) and [Matlab Topic Modeling Toolbox](http://psiexp.ss.uci.edu/research/programs_data/toolbox.htm) to run LDA topic model.

Information about project can be found in *'report.pdf'*.

## Python scripts (run scripts in this order)
1. **getLyricsLinksForArtists.py**: Gets links to first *numLinks* (see variable in script) song lyrics from artists listed in *'artists.csv'* and saves output in *'ArtistURLInfo.pckl'*.
2. **getLyricsFromLinks.py**: Extracts lyrics from links stored in *'ArtistURLInfo.pckl'* and saves it to *'/lyrics/{artist_name}'* dir for each artist.
3. **cleanThemLyrics.py**: Does minor post-processing and saves results to *'cleanLyricWordsPckl/{artist_name}'*.
4. **getDataForTopicModelFromLyrics.py**: Prepares data for topic model from above pickled data and saves it to *'TopicModelData.mat'*

## Matlab scripts (run scripts in this order)
1. **runTopicModel.m**: Runs lda topic model using data in *'TopicModelData.mat'* and saves results to *'TopicModelResults.mat'* and *'topics.txt'*. For inference Gibbs sampling from the [Matlab Topic Modeling Toolbox](http://psiexp.ss.uci.edu/research/programs_data/toolbox.htm) is used.
2. **plot\*.m**: Plots some useful results.
