import psycopg2

# Connect to an chinook database
conn = psycopg2.connect(database="chinook")

# Open a cursor to perform database operations
cursor  = conn.cursor()

# Query 1 - Select all records from the Artist table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the Name column from the Artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only 'Queen' from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by 'ArtistId' #51 from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with 'ArtistId' #51 on the Album table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is 'Queen' from the Track table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - Select all tracks where the composer is 'Miles Davis' from the Track table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Miles Davis"])

# Query 8 - Select all tracks where the composer is 'test' from the Track table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the results (single)
# results  = cursor.fetchone()

# Close communication with the database
conn.close()

# Print results
for result in results:
    print(result)
