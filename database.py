import sqlite3

db = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = db.cursor()


def create_tables():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY
    )
    """)

    db.commit()



def add_user(user_id):

    cursor.execute(
        "INSERT OR IGNORE INTO users(id) VALUES(?)",
        (user_id,)
    )

    db.commit()



def get_users():

    return cursor.execute(
        "SELECT id FROM users"
    ).fetchall()



def count_users():

    return cursor.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]
