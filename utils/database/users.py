import psycopg2


def connect_db():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='group3',
        user='postgres',
        password='1'
    )
    conn.autocommit = True
    return conn


def close_db(conn):
    if conn:
        conn.close()


def create_user(chat_id, username):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"INSERT INTO users (chat_id, username) VALUES ('{chat_id}', '{username}');",
        )
    close_db(conn)

def update_user(phone, chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"update users set phone='{phone}' where chat_id='{chat_id}';",
        )
    close_db(conn)

def update_fio(fio, chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"update users set fio='{fio}' where chat_id='{chat_id}';",
        )
    close_db(conn)

def update_phone(phone, chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"update users set phone='{phone}' where chat_id='{chat_id}';",
        )
    close_db(conn)
def update_about(about, chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"update users set about='{about}' where chat_id='{chat_id}';",
        )
    close_db(conn)


def delete_user(chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"delete from users where chat_id='{chat_id}';",
        )
    close_db(conn)


def get_user_by_id(chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"select * from users where chat_id='{chat_id}';",
        )
        result = cursor.fetchone()
    close_db(conn)

    return result


def get_users():
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            "select * from users",
        )
        result = cursor.fetchall()
    close_db(conn)

    return result
