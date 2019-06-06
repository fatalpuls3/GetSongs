# Getting list of all MP3's along with the entire path
# Requires python 2.7.xx

import os
import sqlite3
import sys
import time
import datetime

song_db = '.\song_db.db'
table1 = 'Songs'
filepath = 'filepath'
artist = 'artist'
title = 'title'
album = 'album'
genre = 'genre'
created_date = 'created_date'
field_type = 'NVARCHAR(1000)'
data = u"E:\\"
txt_input = "E:\\genres.txt"
folders_to_ignore = ['_ScratchLIVE_', '_ScratchLIVE_Backup', '1Audio Essentials', '1Audio Production',
                     '1Fruity Loops Packs', '1Tag Me', '$RECYCLE.BIN', 'DJ Mixes']
songdirs = os.listdir(data)


def getGenres(d):  # this version uses text file input
    print 'Gathering Genre List from Genre.txt file input'
    global genres
    genres = []
    with open(d) as genre_list:
        for line in genre_list:
            genres.append(line)
    genres = map(lambda s: s.strip(), genres)

getGenres(txt_input)

# Db functions and DB reset
conn = sqlite3.connect('song_db.db')
c = conn.cursor()
print 'Clearing Database'
c.execute("DELETE FROM Songs")
conn.text_factory = str

print 'Running song import routine'
starttime = time.ctime()
print 'Started at ' + str(starttime)
for root, dirs, files in os.walk(data):
    dirs[:] = [d for d in dirs if d not in folders_to_ignore]
    # print 'Second for loop'
    for songs in files:
        if songs.endswith(".mp3"):
            f = os.path.join(root, songs)
            fr = f.replace('E:\\','Z:\\')
            fsplit = f.split('\\')
            m = fsplit[-1]
            m = m.replace('.mp3','')
            m = m.replace('_',' ')
            g = fsplit[1]
            ar = fsplit[2]
            al = fsplit[-2]
            sg = None  # init'ing subgenre to NUL
            # print 'Artist was ' + ar
            if ar == 'Singles':
                ar = 'Various Artists'
            if ar.endswith(".mp3"):
                ar = 'Various Artists'
            if g == 'Electronic':  # if genre is Electronic setting subgenre to 3rd position and artist to be 4th position
                sg = fsplit[2]
                ar = fsplit[3]
            if ar == 'Singles' and al == 'Singles':
                ar = 'Various Artists'
            # print (f.encode('utf8'))
            created_date_full = os.path.getctime(f)
            crdo = datetime.datetime.fromtimestamp(created_date_full).date()
            # print crdo
            try:
                c.execute('''INSERT INTO Songs(artist, album, title, genre, subgenre, filepath, created_date)
                    values (?,?,?,?,?,?,?)''', (ar, al, m, g, sg, fr, crdo))
            except sqlite3.IntegrityError:
                print ('!!!')
conn.commit()
print 'Comitting data to database'
conn.close()
endtime = time.ctime()
print 'Process Complete'
print 'Completed at ' + str(endtime)
