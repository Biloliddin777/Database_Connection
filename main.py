import psycopg2
from typing import Optional

conn = psycopg2.connect(
    database='project',
    user='postgres',
    host='localhost',
    password='123',
    port=5432
)

cursor = conn.cursor()

def create_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE
        )
    ''')
    conn.commit()

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def save(self):
        cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (self.name, self.email))
        conn.commit()

    @staticmethod
    def get_users():
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return users

    @staticmethod
    def get_user(user_id: int):
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = cursor.fetchone()
        return user

    @staticmethod
    def delete_user(user_id: int):
        cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        conn.commit()

    @staticmethod
    def update_user(user_id: int, name: str, email: str):
        cursor.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, user_id))
        conn.commit()

create_database()

# user1 = User("John Doe", "john@example.com")
# user1.save()

# user2 = User("Anna", "anna@gmail.com")
# user2.save()

users = User.get_users()
print(users)

# user = User.get_user(5)
# print(user)

User.update_user(4, "Jane Doe", "jane@example.com")

# User.delete_user(3)

conn.close()
