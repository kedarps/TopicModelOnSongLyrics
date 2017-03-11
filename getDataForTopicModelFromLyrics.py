import os
import sys
import pickle
import scipy.io

cleanLyricsDir = '/'.join([sys.path[0], 'cleanLyricWordsPckl'])
dirs = os.listdir(cleanLyricsDir)

words = []
vocab = []

docIdx = []
wordIdx = []
artistIdx = []
artistList = []

iDoc = 0
iArtist = 0
for dir in dirs:
    artistList.append(dir)
    artistDir = '/'.join([cleanLyricsDir, dir])
    pckls = os.listdir(artistDir)

    iArtist += 1

    for pckl in pckls:
        f = open('/'.join([artistDir, pckl]), 'rb')
        lyricWords = pickle.load(f)
        f.close()

        iDoc += 1

        for word in lyricWords:
            words.append(word)
            docIdx.append(iDoc)
            artistIdx.append(iArtist)

uniqueVocab = set(words)
uniqueVocab = list(uniqueVocab)

for dir in dirs:
    artistDir = '/'.join([cleanLyricsDir, dir])
    pckls = os.listdir(artistDir)

    print('\n' + dir + '\n----------\n')

    for pckl in pckls:
        f = open('/'.join([artistDir, pckl]), 'rb')
        lyricWords = pickle.load(f)
        f.close()
        print(pckl)

        for word in lyricWords:
            iWord = uniqueVocab.index(word)
            wordIdx.append(iWord + 1)


saveFName = '/'.join([sys.path[0], 'TopicModelData.mat'])
scipy.io.savemat(saveFName, mdict={
                 'Vocab': uniqueVocab, 'WordIdx': wordIdx, 'DocIdx': docIdx, 'ArtistIdx': artistIdx, 'ArtistList': artistList})
