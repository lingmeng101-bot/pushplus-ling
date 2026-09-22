import sqlite3
import config

SCHEMA = """
    CREATE TABLE IF NOT EXISTS LING(
    id INTEGER PRIMARY KEY,
    url TEXT NOT NULL,
    times TEXT,
    title TEXT NOT NULL,
    pushed INTEGER DEFAULT 0,
    UNIQUE(url))"""
def init_db():
    conn = sqlite3.connect(config.DB_NAME)
    c = conn.cursor()
    c.execute(SCHEMA)
    conn.commit()
    return conn

def link_exists(conn: sqlite3.Connection, url: str) -> bool:
    c = conn.cursor()
    c.execute(
        "SELECT 1 FROM LING WHERE url=? LIMIT 1",
        (url,)
    )
    exists = c.fetchone() is not None
    return exists

def save_notice(conn: sqlite3.Connection,
                url: str,
                times: str,
                title: str) -> None:
    c = conn.cursor()

    c.execute("""
        INSERT INTO LING (url, times, title) 
        VALUES (?, ?, ?)
    """, (url, times, title))

def get_unpushed(conn):

    c = conn.cursor()
    c.execute("""
        SELECT id, title, url, times FROM LING
        WHERE pushed = 0
        ORDER BY id DESC
    """)
    return c.fetchall()

def mark_pushed(conn, notice_id):

    c = conn.cursor()
    c.execute("UPDATE LING SET pushed = 1 WHERE id = ?", (notice_id,))
    conn.commit()

def commit_db(conn: sqlite3.Connection) -> None:
    conn.commit()
