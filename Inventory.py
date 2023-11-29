class Inventory:
    def __init__(self):
        self.database_name = ""
        self.table_name = ""

    def set_database_table(self, database_name, table_name):
        # Set up the database and table names
        self.database_name = database_name
        self.table_name = table_name

    def view_inventory(self):
        # Displays all items in the inventory.
        print(f"Inventory for {self.table_name} in {self.database_name}:")

    def search_inventory(self):
        # Asks for a title, checks the database, and displays the results.
        title = input("Enter the title to search: ")
        print(f"Search results for '{title}':")

    def decrease_stock(self, isbn):
        # Decreases the stock number in the appropriate database for the given ISBN."""
        print(f"Stock decreased for ISBN {isbn} in {self.table_name}.")

    def get_database_name(self):
        #Traditional getter for database_name.
        return self.database_name

    def get_table_name(self):
        #Traditional getter for table_name."""
        return self.table_name
