# imported check module
import check
"""instance of class Authentication"""
auth = check.Authentication()


class Tourist:
    email = ""
    password = ""

    """"method created for taking users choice"""
    def ask_user(self):
        print('Welcome')
        user_choice = input('Do you want to register or login?\n 0 == register , 1 == login')
        if int(user_choice) == 1:
            value = self.check_password()
            if value:
                self.user_login()
                print("****************")
                print("\nCongratutaltions! \nLogin sucessfully\n")
                print("****************")

        elif int(user_choice) == 0:
            value = self.check_password()
            if value:
                self.register_user()
        else:
            print("password id too weak")
            self.ask_user()

    """"taking inputs from users """
    def user_input(self):
        self.email = input('Enter your email: ')
        self.password = input('Enter your password: ')

    def register_user(self):
        auth.create_user_accnt(self.email, self.password)

    def user_login(self):
        auth.login_user_accnt(self.email, self.password)

    """"checking password"""
    def check_password(self):
        self.user_input()
        if auth.check_for_password_length(self.password):
            return True
        else:
            print("password should be greater than 8")
            self.check_password()


""""making instance for tourist"""
tourist = Tourist()
tourist.ask_user()
