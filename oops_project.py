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
            pass
        elif user_input=="2":
            pass
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

obj = chatbook()