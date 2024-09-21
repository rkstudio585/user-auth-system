# User Login, Registration, and Logout System

# `Login(Email, Password)` for allowing user login, if the user has successfully registered.
def Login(Email: str = "", Password: str = "") -> str:
    if Email:
        if '@' in Email and '.' in Email.split('@')[-1]:
            if Password:
                if len(Password) >= 8:
                    card: list = [Email, Password]
                    return card or None
                else:
                    print("Password must be at least 8 characters, please try again.")
                    return False
            else:
                print("\tPassword is empty, please try again.")
                return False
        else:
            print("\tInvalid email format, please try again.")
            return False
    else:
        print("\tEmail is empty, please try again.")
        return False


# `Register(Name, Email, Password, Confirmpass)` for allowing users to create an account using Name, Email, Password, and Confirmpass.
def Register(Name: str = "", Email: str = "", Password: str = "", Confirmpass: str = "") -> str:
    if Name:
        if len(Name) >= 3:
            if Email:
                if '@' in Email and '.' in Email.split('@')[-1]:
                    if Password:
                        if len(Password) >= 8:
                            if Confirmpass:
                                if len(Confirmpass) >= 8:
                                    if Password == Confirmpass:
                                        card: list = [Name, Email, Password]
                                        return card or None
                                    else:
                                        print("\tPassword and Confirm Password do not match, please try again.")
                                        return False
                                else:
                                    print("Confirm Password must be at least 8 characters, please try again.")
                                    return False
                            else:
                                print("Confirm Password is empty, please try again.")
                                return False
                        else:
                            print("Password must be at least 8 characters, please try again.")
                            return False
                    else:
                        print("\tPassword is empty, please try again.")
                        return False    
                else:
                    print("\tInvalid email format, please try again.")
                    return False
            else:
                print("\tEmail is empty, please try again.")
                return False
        else:
            print("\tName must be at least 3 characters, please try again.")
            return False
    else:
        print("\tName is empty, please try again.")
        return False


# `Logout(is_logout, Confirmpass)` for logging out a user if they are logged in, using is_logout=True and Confirm Password.
def Logout(is_logout: bool, Confirmpass: str) -> str:
    if is_logout:
        if Confirmpass:
            if len(Confirmpass) >= 8:
                return True or None 
            else:
                print("Confirm Password must be at least 8 characters, please try again.")
                return False
        else:
            print("\tConfirm Password is empty, please try again.")
            return False
    else:
        print("\tLogout unsuccessful. Set is_logout=True for a successful logout.")
        return False


# `Validator(Query, QueryName)` for validating the success or failure of operations and displaying messages.
def Validator(Query: list = [], QueryName: str = "") -> str:
    if Query:
        print(f'\n\t{QueryName} Successful.')
        return f"\t{QueryName} = {Query}" or None
    else:
        print(f"\t{QueryName} Unsuccessful, please try again.")
    print('')


# Execute the program in `main()`.
def main():
    
    # Define user data to register, login, and logout.
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
