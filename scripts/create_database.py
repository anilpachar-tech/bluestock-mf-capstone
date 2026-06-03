from pathlib import Path
import sqlite3

# Paths

DATABASE_PATH = Path("data/db/bluestock_mf.db")
SCHEMA_PATH = Path("sql/schema.sql")

# Create Database

conn = sqlite3.connect(DATABASE_PATH)

print("Database Connected")

# Execute Schema

with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
    schema_sql = file.read()

conn.executescript(schema_sql)

print("Schema Executed Successfully")

# Verify Tables

cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

tables = cursor.fetchall()

print("\nTables Created:")

for table in tables:
    print(table[0])

conn.commit()
conn.close()

print("\nDatabase Created Successfully")