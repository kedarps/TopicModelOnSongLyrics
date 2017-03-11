import os
import sys
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle


punc = set(string.punctuation)
stop_words = set(stopwords.words('english'))

lyricsDir = '/'.join([sys.path[0], 'lyrics'])
cleanLyricsDir = '/'.join([sys.path[0], 'cleanLyricWordsPckl'])

dirs = os.listdir(lyricsDir)

for dir in dirs:
    artistDir = '/'.join([lyricsDir, dir])
    outDir = '/'.join([cleanLyricsDir, dir])

    print(artistDir + "\n------------\n")

    if not os.path.exists(outDir):
        os.makedirs(outDir)

    lyricsTxt = os.listdir(artistDir)
    for txt in lyricsTxt:
        # outText = '/'.join([outDir, txt])
        outText = '/'.join([outDir, '.'.join([txt.split('.')[0], 'pckl'])])

        if not os.path.isfile(outText):
            print("Processing " + txt)
            fPath = '/'.join([artistDir, txt])
            f = open(fPath, 'r')
            lines = f.read().split(',')
            f.close()

            cleanLyricWords = []
            for line in lines:
                # remove weird preceding unicodes
                match = re.search(r"(u\')|(u\")", line)
                if match is not None:
                    lineAscii = line[match.end():]
                else:
                    lineAscii = line

                # remove punctuations
                lineWoPunc = ''.join(
                    ch for ch in lineAscii if ch not in punc).lower()

                # remove stopwords
                words = word_tokenize(lineWoPunc)
                wordsWoStops = [w for w in words if not w in stop_words]

                for wrd in wordsWoStops:
                    if wrd is not '':
                        cleanLyricWords.append(wrd)

            f = open(outText, 'wb')
            pickle.dump(cleanLyricWords, f)
            f.close()
            # with open(outText, 'w') as outTextFile:
            #     outTextFile.write("%s\n" % cleanLyricWords)
        else:
            print(outText + " already exists!")
