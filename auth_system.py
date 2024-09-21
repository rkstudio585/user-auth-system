import re
import hashlib
import sqlite3

# Initialize SQLite Database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a users table if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL)''')
conn.commit()

# Global variable to keep track of the logged-in user
logged_in_user = None

# Hashing Password using SHA-256
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Email validation using Regular Expression
def validate_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Register user and store details in SQLite3
def Register():
    global logged_in_user
    
    print("\n--- Register a New Account ---")
    Name = input("Enter your name: ")
    Email = input("Enter your email: ")
    Password = input("Enter your password (min 8 characters): ")
    Confirmpass = input("Confirm your password: ")
    
    if Name:
        if len(Name) >= 3:
            if Email:
                if validate_email(Email):
                    if Password:
                        if len(Password) >= 8:
                            if Confirmpass:
                                if Password == Confirmpass:
                                    hashed_password = hash_password(Password)
                                    try:
                                        cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', 
                                                       (Name, Email, hashed_password))
                                        conn.commit()
                                        print("Account created successfully!")
                                        logged_in_user = Email
                                        HomePage()
                                        return [Name, Email] or None
                                    except sqlite3.IntegrityError:
                                        print("An account with this email already exists.")
                                        return False
                                else:
                                    print("Passwords do not match, please try again.")
                                    return False
                            else:
                                print("Confirm Password is empty, please try again.")
                                return False
                        else:
                            print("Password must be at least 8 characters, please try again.")
                            return False
                    else:
                        print("Password is empty, please try again.")
                        return False
                else:
                    print("Invalid email format, please try again.")
                    return False
            else:
                print("Email is empty, please try again.")
                return False
        else:
            print("Name must be at least 3 characters, please try again.")
            return False
    else:
        print("Name is empty, please try again.")
        return False

# Login user by checking credentials from SQLite3
def Login():
    global logged_in_user
    
    print("\n--- Login to Your Account ---")
    Email = input("Enter your email: ")
    Password = input("Enter your password: ")

    if Email:
        if validate_email(Email):
            if Password:
                if len(Password) >= 8:
                    hashed_password = hash_password(Password)
                    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (Email, hashed_password))
                    user = cursor.fetchone()
                    if user:
                        print("Login successful!")
                        logged_in_user = Email
                        HomePage()
                        return [Email] or None
                    else:
                        print("Invalid email or password.")
                        return False
                else:
                    print("Password must be at least 8 characters, please try again.")
                    return False
            else:
                print("Password is empty, please try again.")
                return False
        else:
            print("Invalid email format, please try again.")
            return False
    else:
        print("Email is empty, please try again.")
        return False

# Logout function - Logs out the current user
def Logout():
    global logged_in_user
    
    if logged_in_user:
        print("\n--- Logout from Your Account ---")
        Confirmpass = input("Confirm your password for logout: ")
        
        if Confirmpass:
            if len(Confirmpass) >= 8:
                print(f"Logout successful for {logged_in_user}!")
                logged_in_user = None
                return True or None 
            else:
                print("Confirm Password must be at least 8 characters, please try again.")
                return False
        else:
            print("Confirm Password is empty, please try again.")
            return False
    else:
        print("You are not logged in.")
        return False

# Home Page where the user can only logout if logged in
def HomePage():
    global logged_in_user
    
    if logged_in_user:
        print(f"\n--- Welcome to your Home Page, {logged_in_user} ---")
        while True:
            action = input("\nType 'logout' to log out, or 'exit' to leave the home page: ").strip().lower()
            if action == "logout":
                Logout()
                break
            elif action == "exit":
                print("Leaving the home page.")
                break
            else:
                print("Invalid command. Please type 'logout' or 'exit'.")
    else:
        print("You must log in to access the home page.")

# Help function to show how to use the program
def show_help():
    print("""
    --- Help Menu ---
    Welcome to the User Management System!

    You can perform the following actions:
    
    1. Register - Create a new account.
    2. Login - Log into your existing account.
    3. Logout - Log out from your account (only available after logging in).

    To use these actions, type one of the following commands:
    - 'register' to create a new account.
    - 'login' to log into your account.
    - 'logout' (only available after login).
    - 'help' to show this help message.
    - 'exit' to quit the program.
    """)

# Main function to handle user input and execute corresponding actions
def main():
    show_help()
    while True:
        action = input("\nEnter a command (register/login/logout/help/exit): ").strip().lower()
        
        if action == "register":
            Register()
        
        elif action == "login":
            Login()
        
        elif action == "logout":
            if logged_in_user:
                Logout()
            else:
                print("You need to log in first.")
        
        elif action == "help":
            show_help()
        
        elif action == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid command. Type 'help' to see available options.")
    
if __name__ == "__main__":
    main()

# Close the database connection when done
conn.close()
