# `Login(Email, Password)` for allowed user Login,
# if user successful register or user have an account.
def Login(Email: str = "", Password: str = "") -> str:
    if Email:
        if '@' in Email:
            if Password:
                if Password.count("") > 8:
                    card: list = [Email, Password]
                    return card or None
                # Password.count("") > 8
                else:
                    print("Password Atlist 8 Character, Please try again.")
                    return False
            # Password 
            else:
                print("\tPassword Are Empty, Please try again.")
                return False 
        # @ in Email 
        else:
            print("\tEmail Invalid, Please try again.")
            return False
    # Email 
    else:
        print("\tEmail Are Empty, Please try again.")
        return False


# `Register(Name, Email, Password, Confirmpass)` for,
# allowed the user to Create an Account using Name, Email, 
# Password and Confirmpass.
def Register(Name: str = "", Email: str = "", Password: str = "", Confirmpass: str  = "") -> str:
    if Name:
        if Name.count("") >= 4:
            if Email:
                if '@' in Email:
                    if Password:
                        if Password.count("") > 8:
                            if Confirmpass:
                                if Confirmpass.count("") > 8:
                                    if Password == Confirmpass:
                                        card: list = [Name, Email, Password, Confirmpass]
                                        return card or None
                                    # Password == Confirmpass
                                    else:
                                        print("\tConfirm Password or Password Not Matching, Please try again.")
                                        return False
                                #Confirmpass.count("") > 8
                                else:
                                    print("Confirm Password Atlist 8 Character, Please try again.")
                                    return False
                            #Confirmpass
                            else:
                                print("Confirm Password Are Empty, Atlist 8 Character to mach, Please try again.")
                                return False
                        # Password.count("") > 8
                        else:
                            print("Password Atlist 8 Character, Please try again.")
                            return False
                    # Password
                    else:
                        print("\tPassword Are Empty, Atlist 8 Chraracter, Please try again.")
                        return False    
                # @ in Email
                else:
                    print("\tEmail Invalid, Please try again.")
                    return False
            # Email
            else:
                print("\tEmail Are Empty, Please try again.")
                return False
        # Name.count("") >= 4
        else:
            print("\tName Mast Be 3 Character's, Please try again.")
            return False
    #Name
    else:
        print("\tName Are Empty, Please try again.")
        return False
    
    
# `Logout(is_logout, Confirmpass)` for,
# if the user has login or register then allowed access to,
# logout using is_logout=True and Confirm password.
def Logout(is_logout: bool, Confirmpass: int) -> str:
    if is_logout:
        if Confirmpass:
            if Confirmpass.count("") > 8:
                return True or None 
            # Confirmpass.count("") > 8
            else:
                print("Confirm Password Atlist 8 Character, Please try again.")
                return False
        # Confirmpass
        else:
            print("\tConfirm Password Are Empty, Atlist 8 Chraracter, Please try again.")
            return False
    # is_allowed
    else:
        print("\tLogout Unuccessful `False` us `True` for Logout Successful.")
        return False


# `Validator(Query, QueryName)` for,
# Valid Every Function according `True` or `False`,
# and display the success or error massage.
def Validator(Query: list = [], QueryName: str = "") -> str:
    if Query:
        print(f'\n\t{QueryName} Successful..')
        return f"\t{QueryName} = {Query}" or None
    # Query
    else:
        print(f"\t{QueryName} Unuccessful, Please try again.")
    print('')


# execute all program in here `main()`.
def main():
    
    # Define user data to register, login and logout.
    NAME = "MD Riad Khan"
    EMAIL = "riadkhan@rkstudio.com"
    PASSWORD = "riad1234@#"
    CONFIRM_PASS = "riad1234@#"
    
    # Allowed user to register using Name, Email, Password and Confirmpass and create an account sucessfully.
    AllowRegister = Register(Name=NAME, Email=EMAIL, Password=PASSWORD, Confirmpass=CONFIRM_PASS)
    RegisterValidator = Validator(Query=AllowRegister, QueryName="Register")
    print(RegisterValidator)
    
#    if register:
#        print(f"\t{register = }.")
#        print('\tRegister Successful..')
#    else:
#        print("\t Register Unuccessful, Please try again.")
#    
#    print('')

    # allowed use to login using Email and Password.
    AllowLogin = Login(Email=EMAIL, Password=PASSWORD)
    loginValidator = Validator(Query=AllowLogin, QueryName="Logging")
    print(loginValidator)
    
#    if login:
#        print(f"\t{login = }.")
#        print("\tlogging Successful..")
#    else: 
#        print("\tLogging Unsuccessful, Please try again.")
#    
#    print('')

    # `is_logout=False` for not logout.
    # `is_logout=True` for logout. 
    # allowed the user to logout using `is_logout=True` or Confirmpass for successful logout if the user login or register.
    AllowLogout = Logout(is_logout=True, Confirmpass=CONFIRM_PASS)
    LogoutValidator = Validator(Query=AllowLogout, QueryName="Logout")
    print(LogoutValidator)
    

if __name__ == "__main__":
    main()
