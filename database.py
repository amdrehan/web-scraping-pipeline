import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('data/news_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS headlines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            scraped_at TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(data):
    conn = sqlite3.connect('data/news_data.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for item in data:
        cursor.execute('''
            INSERT INTO headlines (title, url, scraped_at)
            VALUES (?, ?, ?)
        ''', (item['title'], item['url'], timestamp))
    
    conn.commit()
    conn.close()