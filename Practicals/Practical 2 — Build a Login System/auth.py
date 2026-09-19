import sqlite3
import bcrypt
DATABASE = "users.db"
def connect_db():
    return sqlite3.connect(DATABASE)
def setup_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
def register():
    username = input("Enter username: ")
    password = input("Enter password: ").encode("utf-8")
    # Hash the password before storing it
    password_hash = bcrypt.hashpw(
        password,
        bcrypt.gensalt()
    )
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash.decode("utf-8"))
        )
        conn.commit()
        conn.close()
        print("Registration successful.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ").encode("utf-8")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    conn.close()
    if result is None:
        print("Invalid username or password.")
        return False
    stored_hash = result[0].encode("utf-8")
    if bcrypt.checkpw(password, stored_hash):
        print("Login successful.")
        return True
    print("Invalid username or password.")
    return False
def logout():
    print(" Logged out successfully.")
def main():
    setup_database()
    logged_in = False
    while True:
        print("\n===== Authentication Demo =====")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            if logged_in:
                print(" Already logged in.")
            else:
                logged_in = login()
        elif choice == "3":
            if logged_in:
                logout()
                logged_in = False
            else:
                print(" No user is currently logged in.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()