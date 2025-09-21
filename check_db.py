import sqlite3

# Connect to database
conn = sqlite3.connect("finaldata.db")
c = conn.cursor()

# Show all rows
c.execute("SELECT * FROM weather_report")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
