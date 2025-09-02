import mysql.connector
from datetime import datetime
import time
import os

# MySQL database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='Aetheria'
)
cursor = conn.cursor()

def clear_screen():
    # Clear terminal screen (works on Unix-like systems and Windows)
    os.system('cls' if os.name == 'nt' else 'clear')

def display_messages(chat_id):
    # Retrieve the last 10 messages for a specific chat
    cursor.execute('''
        SELECT SenderID, Content, Timestamp
        FROM Message
        WHERE ChatID = %s
        ORDER BY Timestamp DESC
        LIMIT 10
    ''', (chat_id,))
    messages = cursor.fetchall()

    # Clear the screen before printing new messages
    clear_screen()

    for message in reversed(messages):  # Reverse to display the latest message last
        print(f"{message[0]}: {message[1]} ({message[2]})")

def send_message(content, sender_id, chat_id):
    # Insert the message into the database
    cursor.execute('''
        INSERT INTO Message (Content, SenderID, Timestamp, ChatID)
        VALUES (%s, %s, %s, %s)
    ''', (content, sender_id, datetime.now(), chat_id))
    conn.commit()

if __name__ == '__main__':
    # Ask for user ID and chat ID
    user_id = input("Enter your user ID: ")
    chat_id = input("Enter the chat ID: ")

    while True:
        display_messages(chat_id)
        user_input = input("Type your message (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        send_message(user_input, user_id, chat_id)

        # Introduce a delay before the next update
        time.sleep(1)

# Close the connection when done
conn.close()
