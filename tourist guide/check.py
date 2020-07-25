import pyrebase

config = {
    "apiKey": "AIzaSyCTfVwQtLy9mZVYxOums4eYBkBsiddNewY",
    "authDomain": "virtual-tourist-guide-3b35c.firebaseapp.com",
    "databaseURL": "https://virtual-tourist-guide-3b35c.firebaseio.com",
    "projectId": "virtual-tourist-guide-3b35c",
    "storageBucket": "virtual-tourist-guide-3b35c.appspot.com",
}

firebase = pyrebase.initialize_app(config)  # firebase connection for configuration
auth = firebase.auth()  # instance created
db = firebase.database()  # instance for database is created


class Authentication:

    @staticmethod
    def create_user_accnt(email, password):  # method created for registration of user
        auth.create_user_with_email_and_password(email, password)  # method is called for registration

    @staticmethod
    def login_user_accnt(email, password):  # method created for login of user
        auth.sign_in_with_email_and_password(email, password)  # method is called for sign in

    def check_for_password_length(self,password):
        if len(password) >= 8:
            return True
        else:
            return False

