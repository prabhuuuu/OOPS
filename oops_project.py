# a social media type application 

class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()
    
    def menu(self):
        user_input = input("""
                    Upwelcome to chatbook
                    1. Press 1 to signup
                    2. Press 2 to signin
                    3. Press 3 to write a post
                    4. Press 4 to text a friend
                    5. Press any other key to exit.\n """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_posts()
        elif user_input=="4":
            self.message()
        else:
            exit()

    def signup(self):
        email = input("enter your email here:")
        password = input("enter your password here:")
        self.username = email
        self.password = password
        print("you have successfully signed up\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("you need to signup first\n")
            self.menu()
        else:
            uname= input("enter your username/email here:")
            input_password= input("enter your password here:")
            if self.username==uname and self.password==input_password:
                self.loggedin=True
                print("you have successfully logged in\n")
            else:
                print("invalid credentials\n")
        self.menu()
    
    def my_posts(self):
        if self.loggedin==True:
            txt=input("enter your post here:")
            print(f"your post:{txt} has been posted")
        else:
            print("you need to login first to post something")
        self.menu()

    def message(self):
        if self.loggedin==True:
            txt=input("enter your message here:")
            frnd = input("enter your friend's name here:")
            print(f"your message:{txt} has been sent to {frnd}")
        else:
            print("you need to login first to send a message")
        self.menu()

obj = chatbook()