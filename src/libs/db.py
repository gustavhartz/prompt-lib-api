# db.py
import os
import psycopg2
from contextlib import contextmanager

# Database connection parameters
DB_PARAMS = {
    "database": os.environ["DB_DATABASE"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "host": os.environ["DB_HOST"],
    "port": os.environ["DB_PORT"],
}


@contextmanager
def get_db_connection():
    conn = psycopg2.connect(**DB_PARAMS)
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def get_db_cursor(commit=False):
    with get_db_connection() as connection:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            yield cursor
            if commit:
                connection.commit()
        finally:
            cursor.close()


def create_user(username, email):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id;",
            (username, email),
        )
        return cursor.fetchone()[0]


def create_prompt(title, description, prompt, user_id):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO prompts (title, description, prompt, user_id) VALUES (%s, %s, %s, %s) RETURNING id;",
            (title, description, prompt, user_id),
        )
        return cursor.fetchone()[0]


def list_prompts(query=None):
    with get_db_cursor() as cursor:
        if query:
            cursor.execute(
                "SELECT * FROM prompts WHERE title ILIKE %s OR description ILIKE %s;",
                (f"%{query}%", f"%{query}%"),
            )
        else:
            cursor.execute("SELECT * FROM prompts;")
        return cursor.fetchall()


def get_user_ranking():
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT user_id, COUNT(*) as like_count FROM likes GROUP BY user_id ORDER BY like_count DESC;"
        )
        return cursor.fetchall()


def vote_on_prompt(user_id, prompt_id, vote_type):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO votes (user_id, prompt_id, vote_type) VALUES (%s, %s, %s) ON CONFLICT (user_id, prompt_id) DO UPDATE SET vote_type = EXCLUDED.vote_type;",
            (user_id, prompt_id, vote_type),
        )


def like_unlike_prompt(user_id, prompt_id, like=True):
    with get_db_cursor(commit=True) as cursor:
        if like:
            cursor.execute(
                "INSERT INTO likes (user_id, prompt_id) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                (user_id, prompt_id),
            )
        else:
            cursor.execute(
                "DELETE FROM likes WHERE user_id = %s AND prompt_id = %s;",
                (user_id, prompt_id),
            )
