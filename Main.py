
from Menu import main_menu
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

database = r".\commercedatabase.db"

sql_create_inventory_table = """ CREATE TABLE Inventory (
                                    ISBN VARCHAR(20) PRIMARY KEY,
                                    Title VARCHAR(255),
                                    Author VARCHAR(100),
                                    Genre VARCHAR(50),
                                    Pages INT,
                                    ReleaseDate DATE,
                                    Stock INT
                                    );
                            """
sql_create_user_table = """ CREATE TABLE User (
                            UserID INT PRIMARY KEY,
                            Email VARCHAR(255),
                            Password VARCHAR(255),
                            FirstName VARCHAR(50),
                            LastName VARCHAR(50),
                            Address VARCHAR(255),
                            City VARCHAR(100),
                            State VARCHAR(50),
                            Zip VARCHAR(10),
                            Payment VARCHAR(255)
                            );
                        """
sql_create_cart_table = """ CREATE TABLE Cart (
                            UserID INT,
                            ISBN VARCHAR(20),
                            Quantity INT,
                            PRIMARY KEY (UserID, ISBN),
                            FOREIGN KEY (UserID) REFERENCES User(UserID),
                            FOREIGN KEY (ISBN) REFERENCES Inventory(ISBN)
                            );
                        """
if __name__ == '__main__':
    conn = create_connection(database)
    create_table(conn, sql_create_inventory_table)
    create_table(conn, sql_create_user_table)
    create_table(conn, sql_create_cart_table)
    main_menu()
