import csv
from urllib import urlopen
from bs4 import BeautifulSoup
import re
import pickle


baseURL = 'http://www.lyricsfreak.com'
allArtistInfo = []
with open('artists.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        artist = row[0]

        URL = '/'.join([baseURL, artist[0], artist, ''])
        print(URL)
        html = urlopen(URL).read()
        soup = BeautifulSoup(html, 'html.parser')

        searchStr = '/'.join(['', artist[0], artist.split('+')[0]])
        print(searchStr)
        allLyricLinks = []
        allLinks = soup.find_all(href=re.compile(searchStr))

        for link in allLinks[:60]:
            allLyricLinks.append(link.get('href'))

        thisArtistInfo = {"artist": artist, "links": allLyricLinks}

        allArtistInfo.append(thisArtistInfo)

    print("Saving to pickle...")
    f = open('ArtistURLInfo.pckl', 'wb')
    pickle.dump(allArtistInfo, f)
    f.close()
    print("Done\n")
