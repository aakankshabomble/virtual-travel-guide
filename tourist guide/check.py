import pyrebase

config = {
    "apiKey": "AIzaSyCTfVwQtLy9mZVYxOums4eYBkBsiddNewY",
    "authDomain": "virtual-tourist-guide-3b35c.firebaseapp.com",
    "databaseURL": "https://virtual-tourist-guide-3b35c.firebaseio.com",
    "projectId": "virtual-tourist-guide-3b35c",
    "storageBucket": "virtual-tourist-guide-3b35c.appspot.com",
}

"""firebase connection for configuration"""
firebase = pyrebase.initialize_app(config)
"""instance created"""
auth = firebase.auth()
"""instance for database is created"""
db = firebase.database()


class Authentication:

    @staticmethod
    # method created for registration of user
    def create_user_accnt(email, password):
        # method is called for registration
        auth.create_user_with_email_and_password(email, password)

    @staticmethod
    # method created for login of user
    def login_user_accnt(email, password):
        # method is called for sign in
        auth.sign_in_with_email_and_password(email, password)

    def check_for_password_length(self, password):
        if len(password) >= 8:
            return True
        else:
            return False
