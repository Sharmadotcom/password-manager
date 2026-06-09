import os
import time
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found")

def get_db():

    start = time.time()

    conn = psycopg.connect(
        DATABASE_URL,
        sslmode="require"
    )

    print(
        "Connection took:",
        round(time.time() - start, 2),
        "seconds"
    )

    return conn