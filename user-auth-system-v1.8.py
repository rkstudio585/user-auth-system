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

# Hashing Password using SHA-256
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Email validation using Regular Expression
def validate_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Register user and store details in SQLite3
def Register(Name: str = "", Email: str = "", Password: str = "", Confirmpass: str = "") -> str:
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
def Login(Email: str = "", Password: str = "") -> str:
    if Email:
        if validate_email(Email):
            if Password:
                if len(Password) >= 8:
                    hashed_password = hash_password(Password)
                    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (Email, hashed_password))
                    user = cursor.fetchone()
                    if user:
                        print("Login successful!")
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

# Logout function - simple for now, as no session management is implemented
def Logout(is_logout: bool, Confirmpass: str) -> str:
    if is_logout:
        if Confirmpass:
            if len(Confirmpass) >= 8:
                print("Logout successful!")
                return True or None 
            else:
                print("Confirm Password must be at least 8 characters, please try again.")
                return False
        else:
            print("Confirm Password is empty, please try again.")
            return False
    else:
        print("Logout unsuccessful. Set is_logout=True for a successful logout.")
        return False

# Validator function to print messages
def Validator(Query: list = [], QueryName: str = "") -> str:
    if Query:
        print(f'\n\t{QueryName} Successful.')
        return f"\t{QueryName} = {Query}" or None
    else:
        print(f"\t{QueryName} Unsuccessful, please try again.")
    print('')

# Execute all functions in main()
def main():
    
    # Define user data
    NAME = "John Doe"
    EMAIL = "john.doe@example.com"
    PASSWORD = "johnDoe123!"
    CONFIRM_PASS = "johnDoe123!"
    
    # Register user
    AllowRegister = Register(Name=NAME, Email=EMAIL, Password=PASSWORD, Confirmpass=CONFIRM_PASS)
    RegisterValidator = Validator(Query=AllowRegister, QueryName="Register")
    print(RegisterValidator)

    # Login user
    AllowLogin = Login(Email=EMAIL, Password=PASSWORD)
    loginValidator = Validator(Query=AllowLogin, QueryName="Login")
    print(loginValidator)

    # Logout user
    AllowLogout = Logout(is_logout=True, Confirmpass=CONFIRM_PASS)
    LogoutValidator = Validator(Query=AllowLogout, QueryName="Logout")
    print(LogoutValidator)

if __name__ == "__main__":
    main()

# Close the database connection when done
conn.close()
