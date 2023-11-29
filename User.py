from db import create_connection
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
        try:
            email = input("Enter email: ")
            password = input("Enter password: ")

            conn = create_connection(self.database_name)
            cur = conn.cursor()

            cur.execute(f"SELECT * FROM {self.table_name} WHERE Email = ? AND Password = ?", (email, password))
            
            result = cur.fetchone()
            print(result)
            if result:
                self.logged_in = True
                self.user_id = result[0]
                print("Login successful.")
                print(f"Welcome, {result[3]} {result[4]}.")
                return True
            else:
                print("Login failed.")
                return False
        except Exception as e:
            print(f"An error occurred while logging in: {str(e)}")
        return True

    def logout(self):
        # : Resets the userID back to blank and loggedIn back to false – returns false to be used in main.
        if(not self.logged_in):
            print("You are not logged in.")
            return False
        self.user_id = ""
        self.logged_in = False
        print("Logout successful.")
        return False

    def view_account_information(self):
        # Displays all the appropriate account information to the currently logged in user.
        if self.logged_in:
            print(f"Account Information for User ID {self.user_id}:")
            conn = create_connection(self.database_name)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {self.table_name} WHERE UserID = ?", (self.user_id,))
            print(cur.fetchone())
            conn.close()
        else:
            print("Please log in to view account information.")
        

    def create_account(self):
        # Contains all input and output related to creating an account – validation included.
        try:
            email = input("Enter email: ")
            password = input("Enter password: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address = input("Enter address: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            zip_code = input("Enter zip code: ")
            payment = input("Enter payment: ")

            conn = create_connection(self.database_name)
            cur = conn.cursor()

            # Get the maximum user_id from the table
            cur.execute(f"SELECT MAX(userID) FROM {self.table_name}")
            result = cur.fetchone()
            max_user_id = result[0] if result[0] else 0

            # Increment the maximum user_id by 1 for the new user
            new_user_id = max_user_id + 1
            print(self.table_name)
            cur.execute(f"INSERT INTO {self.table_name} (userID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (new_user_id, email, password, first_name, last_name, address, city, state, zip_code, payment))
            conn.commit()

            print(f"Account created successfully for User ID {new_user_id}.")
        except Exception as e:
            print(f"An error occurred while creating the account: {str(e)}")
        finally:
            conn.close()


    def get_logged_in(self):
        # Traditional getter for logged_in
        return self.logged_in

    def get_user_id(self):
        #Traditional getter for user_id
        return self.user_id
