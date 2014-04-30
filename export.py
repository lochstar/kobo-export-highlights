import sqlite3
import csv

# Open database
conn = sqlite3.connect('KoboReader.sqlite')
c = conn.cursor()

# Execute SQL
highlights = c.execute('SELECT VolumeID, Text, DateCreated FROM Bookmark').fetchall()

# Close database
c.close()

# Encode data
encoded = [[s.encode('utf8') for s in t] for t in highlights]

print (('Exporting %s Higlights...') % (len(highlights)))

# Write CSV
writer = csv.writer(open('highlights.csv', 'wb'))
with open('highlights.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(encoded)
