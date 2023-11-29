class User:
    def __init__(self):
        self.database_name = ""
        self.table_name = ""
        self.logged_in = False
        self.user_id = ""

    def set_database_table(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def login(self):
        # Handles input, validation, and verification to allow someone to login.
        self.logged_in = True
        self.user_id = input("Enter user ID: ")  
        print("Login successful.")
        return True

    def logout(self):
        # : Resets the userID back to blank and loggedIn back to false – returns false to be used in main.
        self.user_id = ""
        self.logged_in = False
        print("Logout successful.")
        return False

    def view_account_information(self):
        # Displays all the appropriate account information to the currently logged in user.
        if self.logged_in:
            print(f"Account Information for User ID {self.user_id}:")
        else:
            print("Please log in to view account information.")

    def create_account(self):
        # Contains all input and output related to creating an account – validation included.
        self.user_id = input("Enter user ID for the new account: ")  
        print(f"Account created successfully for User ID {self.user_id}.")

    def get_logged_in(self):
        # Traditional getter for logged_in
        return self.logged_in

    def get_user_id(self):
        #Traditional getter for user_id
        return self.user_id
