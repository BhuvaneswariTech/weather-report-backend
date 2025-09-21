import sqlite3

def save_to_db(df, db_path="finaldata.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS weather_report (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            humidity REAL
        )
    ''')

    for _, row in df.iterrows():
        c.execute('''
            INSERT INTO weather_report (timestamp, temperature, humidity)
            VALUES (?, ?, ?)
        ''', (row["timestamp"], row["temperature_2m"], row["relative_humidity_2m"]))

    conn.commit()
    conn.close()
    print("✅ Data saved into finaldata.db (table: weather_report)")
