import sqlite3

def init_database():
    connection = sqlite3.connect("storage.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clean_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            data_hash TEXT UNIQUE
        )
    """)
    connection.commit()
    connection.close()

def check_duplicate(fingerprint):
    connection = sqlite3.connect("storage.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM clean_data WHERE data_hash = ?", (fingerprint,))
    exists = cursor.fetchone()
    connection.close()
    return exists is not None

def save_data(content, fingerprint):
    connection = sqlite3.connect("storage.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO clean_data (content, data_hash) VALUES (?, ?)", (content, fingerprint))
    connection.commit()
    connection.close()