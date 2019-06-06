import sqlite3

song_db = '.\song_db.db'
table1 = 'Songs'
filepath = 'filepath'
songtitle = 'title'
artist = 'artist'
album = 'album'
genre = 'genre'
subgenre = 'subgenre'
field_type = 'NVARCHAR(1000)'

conn = sqlite3.connect(song_db)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'\
  .format(tn=table1, nf=artist, ft=field_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
  .format(tn=table1, cn=album, ct=field_type))  

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
  .format(tn=table1, cn=songtitle, ct=field_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
  .format(tn=table1, cn=genre, ct=field_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
  .format(tn=table1, cn=subgenre, ct=field_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
  .format(tn=table1, cn=filepath, ct=field_type))



conn.commit()
conn.close()