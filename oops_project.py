# a social media type application 

class chatbook:
    def __init__(self):
        self.username=" "
        self.password=" "
        self.logedin=False
        self.menu()
    
    def menu(self):
        user_input = input("""
                    Upwelcome to chatbook
                    1. Press 1 to signup
                    2. Press 2 to signin
                    3. Press 3 to write a post
                    4. Press 4 to view posts
                    5. Press any other key to exit.\n """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your email here:")
        password = input("enter your password here:")
        self.username = email
        self.password = password
        print("you have successfully signed up\n")

    def signin(self):
        if self.username=="" and self.password=="":
            print("you need to signup first\n")
            self.menu()
        else:
            uname= input("enter your username/email here:")
            input_password= input("enter your password here:")
            if self.username==uname and self.password==input_password:
                self.logedin=True
                print("you have successfully logged in\n")
            else:
                print("invalid credentials\n")
        self.menu()
obj = chatbook()