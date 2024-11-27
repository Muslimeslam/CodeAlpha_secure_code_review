import sqlite3
import os
import hashlib
import base64


def setup_database():
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    cursor.execute('''INSERT INTO users (username, password) VALUES ('admin', 'password123')''')
    conn.commit()
    conn.close()
def login():
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    print("Enter your username:")
    username = input()  
    print("Enter your password:")
    password = input()  
    
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")
    cursor.execute(query)  
    
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed!")
    conn.close()
def store_password():
    print("Enter a new password to store:")
    password = input()
    
 
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    print(f"Weakly hashed password: {hashed_password}")


def read_file():
    print("Enter the name of the file to read:")
    filename = input()  
    
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print(f.read())
    else:
        print("File does not exist.")


def encode_message():
    print("Enter a message to encode:")
    message = input()
    
    
    key = "defaultkey"  
    combined_message = key + message
    
    
    encoded_message = base64.b64encode(combined_message.encode())
    print(f"Encoded message: {encoded_message}")
    print(f"Hardcoded key (vulnerability): {key}")


if __name__ == "__main__":
    setup_database()
    
    print("\n1. Login")
    print("2. Store Password")
    print("3. Read File")
    print("4. Encode Message")
    
    print("Choose an option:")
    choice = input()
    
    if choice == '1':
        login()
    elif choice == '2':
        store_password()
    elif choice == '3':
        read_file()
    elif choice == '4':
        encode_message()
    else:
        print("Invalid choice.")
