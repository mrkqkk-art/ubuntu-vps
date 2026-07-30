import sqlite3


db = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = db.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS settings(
    key TEXT PRIMARY KEY,
    value TEXT
)
""")

db.commit()



def set_setting(key, value):

    cursor.execute(
        """
        INSERT OR REPLACE INTO settings(key,value)
        VALUES(?,?)
        """,
        (key, value)
    )

    db.commit()



def get_setting(key, default=None):

    result = cursor.execute(
        "SELECT value FROM settings WHERE key=?",
        (key,)
    ).fetchone()


    if result:
        return result[0]

    return default
