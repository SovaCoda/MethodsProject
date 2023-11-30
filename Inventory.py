from db import create_connection
class Inventory:
    def __init__(self):
        self.database_name = ""
        self.table_name = ""

    def set_database_table(self, database_name, table_name):
        # Set up the database and table names
        self.database_name = database_name
        self.table_name = table_name

    def view_inventory(self, userID):
        try:
            connection = create_connection(self.database_name)
            cursor = connection.cursor()
            
            cursor.execute(f"SELECT Title, ISBN, Stock FROM {self.table_name}")
            rows = cursor.fetchall()

            print("Inventory:")
            for i, row in enumerate(rows):
                print(f"{i+1}. Title: {row[0]}")
                print(f"   ISBN: {row[1]}")
                print(f"   Stock: {row[2]}")
                print("----------")

            selected_item = input("Enter the number of the item to add to your cart (or 'q' to quit): ")
            if selected_item.isdigit():
                selected_item = int(selected_item)
                if 1 <= selected_item <= len(rows):

                    cart_item = rows[selected_item-1]
                    print(f"Adding '{cart_item[0]}' to your cart.")
                    conn = create_connection(self.database_name)
                    cur = conn.cursor()

                    cur.execute("SELECT Quantity FROM Cart WHERE UserID = ? AND ISBN = ?", (userID, cart_item[1]))
                    existing_quantity = cur.fetchone()

                    if existing_quantity:
                        quantity = int(input("Enter the quantity to add: "))
                        new_quantity = existing_quantity[0] + quantity
                        cur.execute("UPDATE Cart SET Quantity = ? WHERE UserID = ? AND ISBN = ?", (new_quantity, userID, cart_item[1]))
                    else:
                        quantity = int(input("Enter the quantity to add: "))
                        cur.execute("INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (?, ?, ?)", (userID, cart_item[1], quantity))

                    conn.commit()
                    conn.close()
                else:
                    print("Invalid item number.")
            elif selected_item.lower() == 'q':
                print("Quitting...")
            else:
                print("Invalid input.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        finally:
            if connection:
                connection.close()

    def search_inventory(self):
        # Asks for a title, checks the database, and displays the results.
        title = input("Enter title: ")
        connection = create_connection(self.database_name)
        cursor = connection.cursor()
        cursor.execute(f"SELECT Title, ISBN, Stock FROM {self.table_name} WHERE Title = ?", (title,))
        rows = cursor.fetchall()
        for row in rows:
            print(f"Title: {row[0]}")
            print(f"ISBN: {row[1]}")
            print(f"Stock: {row[2]}")
            print("----------")

    def decrease_stock(self, isbn):
        # Decreases the stock number in the appropriate database for the given ISBN."""
        conn = create_connection(self.database_name)
        cur = conn.cursor()
        cur.execute(f"UPDATE {self.table_name} SET Stock = Stock - 1 WHERE ISBN = ?", (isbn,))
        conn.commit()
        conn.close()

    def get_database_name(self):
        #Traditional getter for database_name.
        return self.database_name

    def get_table_name(self):
        #Traditional getter for table_name."""
        return self.table_name
