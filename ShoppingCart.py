from db import create_connection

class ShoppingCart:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def set_database_table(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def view_cart(self):
        try:
            conn = create_connection(self.database_name)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {self.table_name} WHERE UserID = ?", (self.user_id,))
            print(cur.fetchall())
        except Exception as e:
            print(f"Error occurred while viewing cart: {str(e)}")
        finally:
            if conn:
                conn.close()

    def add_to_cart(self, isbn, userID, quantity):
        try:
            conn = create_connection(self.database_name)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {self.table_name} WHERE ISBN = ? AND UserID = ?", (isbn, userID))
            result = cur.fetchone()
            if result:
                existing_quantity = result[2]
                new_quantity = existing_quantity + quantity
                cur.execute(f"UPDATE {self.table_name} SET Quantity = ? WHERE ISBN = ? AND UserID = ?", (new_quantity, isbn, userID))
            else:
                cur.execute(f"INSERT INTO {self.table_name} (ISBN, UserID, Quantity) VALUES (?, ?, ?)", (isbn, userID, quantity))
            conn.commit()
            print("Item added to cart successfully.")
        except Exception as e:
            print(f"Error occurred while adding item to cart: {str(e)}")
        finally:
            if conn:
                conn.close()

    def checkout(self):
        try:
            conn = create_connection(self.database_name)
            cur = conn.cursor()
            cur.execute(f"SELECT ISBN, Quantity FROM {self.table_name}")
            cart_items = cur.fetchall()
            for item in cart_items:
                isbn = item[0]
                quantity = item[1]
                cur.execute(f"UPDATE Inventory SET Stock = Stock - ? WHERE ISBN = ?", (quantity, isbn))
            cur.execute(f"DELETE FROM {self.table_name}")
            conn.commit()
            print("Checkout completed successfully.")
        except Exception as e:
            print(f"Error occurred while checking out: {str(e)}")
        finally:
            if conn:
                conn.close()

    def remove_from_cart(self, isbn, userID):
        try:
            conn = create_connection(self.database_name)
            cur = conn.cursor()
            cur.execute(f"DELETE FROM {self.table_name} WHERE ISBN = ? AND UserID = ?", (isbn, userID))
            conn.commit()
            print("Item removed from cart successfully.")
        except Exception as e:
            print(f"Error occurred while removing item from cart: {str(e)}")
        finally:
            if conn:
                conn.close()
