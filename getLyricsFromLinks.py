import pickle
from urllib import urlopen
from bs4 import BeautifulSoup
import os
import sys
import time

writeSuccess = 0
writeFails = 0

baseURL = 'http://www.lyricsfreak.com'

f = open('ArtistURLInfo.pckl', 'rb')
artistInfo = pickle.load(f)
f.close()

for artist in artistInfo:
    artistName = artist['artist']
    dirPath = '/'.join([sys.path[0], 'lyrics', artistName])
    print(artistName + "\n------\n")

    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    urls = artist['links']
    for url in urls:
        url = url.encode('ascii')

        if 'html' in url:
            songName = url.split('/')
            songName = songName[len(songName) - 1].split('.')[0]

            fName = '/'.join([dirPath, '.'.join([songName, 'txt'])])

            if not os.path.isfile(fName):
                print("Processing " + artistName + " " + songName)
                seekURL = baseURL + url
                html = urlopen(seekURL).read()
                soup = BeautifulSoup(html, 'html.parser')
                div = soup.find('div', {'id': 'content_h'})

                if len(div) != 0:
                    time.sleep(10)
                    thisSongLyrics = [div.contents[0]]
                    restStrings = div.contents[1].strings

                    for string in restStrings:
                        thisSongLyrics.append(string)

                    with open(fName, 'w') as txtFile:
                        try:
                            txtFile.write("%s" % thisSongLyrics)
                            writeSuccess += 1
                        except:
                            print("Failed to write")
                            writeFails += 1
                            pass
                else:
                    print("No div content found\n")
                    writeFails += 1
            else:
                print(artistName + " " + songName + " already processed!")

    print(artistName + "\n------\n")

print("Successfully wrote: " + str(writeSuccess) + " files\n")
print("Failed to write: " + str(writeFails) + " files\n")
