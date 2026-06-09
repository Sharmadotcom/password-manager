from db import get_db

conn = get_db()
cursor = conn.cursor()

cursor.execute("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
""")

print(cursor.fetchall())

conn.close()