#Latent Dirichlet allocation applied to song lyrics data

Uses Python to extract and process lyrics text data from [lyricsfreak.com](http://www.lyricsfreak.com/) and [Matlab Topic Modeling Toolbox](http://psiexp.ss.uci.edu/research/programs_data/toolbox.htm) to run LDA topic model.



## Python scripts (run scripts in this order)
1. **getLyricsLinksForArtists.py**: Gets links to first *numLinks* song lyrics from artists listed in *'artists.csv'*. Output is saved in *'ArtistURLInfo.pckl'*
2. **getLyricsFromLinks.py**: Extracts lyrics from links stored in *'ArtistURLInfo.pckl'* and saves it to *'/lyrics/{artist_name}'* dir for each artist.
3. **cleanThemLyrics.py**: Does minor post-processing and saves results to *'cleanLyricWordsPckl/{artist_name}'*.
4. **getDataForTopicModelFromLyrics.py**: Prepares data for topic model from above pickled data and saves it to *'TopicModelData.mat'*

## Matlab scripts (run scripts in this order)
1. **runTopicModel.m**: Runs lda topic model using Gibbs Sampling from [Matlab Topic Modeling Toolbox](http://psiexp.ss.uci.edu/research/programs_data/toolbox.htm) and saves results to *'TopicModelResults.mat'* and *'topics.txt'*.
2. **plot*.m**: Plots some useful results.
