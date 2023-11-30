from User import User 
from Inventory import Inventory
from ShoppingCart import ShoppingCart
cur_inventory = Inventory()
cur_inventory.set_database_table(r".\commercedatabase.db", "Inventory")
cur_cart = ShoppingCart()
cur_cart.set_database_table(r".\commercedatabase.db", "Cart")
cur_user = User()
cur_user.set_database_table(r".\commercedatabase.db", "User")
def options():
    print("Choose an option: ")
    print("1. Login ")
    print("2. Create Account ")
    print("3. Log out ")
    print(" ")
    l = [" "]

    
    g = int(input())
    if g == 1:
        cur_user.login()
        main_menu()
        

    if g == 2:
        cur_user.create_account()
        main_menu()

    if g ==3:
        cur_user.logout()
        main_menu()
    else:
         print("That is an invalid option. Select again.")
         print(" ")
         main_menu()

def menu():
    print("Main menu ")
    print ("1. Log out")
    print ("2. View Account Information")
    print ("3. Inventory Information")
    print ("4. Cart Information")
    print (" ")
    
    x = int(input())
    while x!= 1 and x!= 2 and x!= 3 and x!= 4:
        print("That is an invalid option ")
        x = int(input())
        print(" ")
    if x==1:
        cur_user.logout()
        main_menu()
    elif x ==2:
        cur_user.view_account_information()
        print(" ")
        main_menu()
    elif x == 3:
            print("Select an option ")
            print("1. Go back ")
            print("2. View Inventory ")
            print("3. Search Inventory")
            print(" ")
            i = int(input())
            while i!= 1 and i!= 2 and i!= 3:
                print("That is an incorrect option. Please select again ")
                print(" ")
                i = int(input())
            if i==1:
                main_menu()
            elif i==2:
                #viewInventory()
                cur_inventory.view_inventory(cur_user.get_user_id())
                print(" ")
                main_menu()
            elif i==3:
                #searchInventory()    
                print(" ")
                cur_inventory.search_inventory()
                main_menu()
            
        
    elif x == 4:
        print("1. Go Back")
        print("2. View Cart")
        print("3. Remove an Item from Cart")
        print("4. Check Out")
        print(" ")
            
        z = int(input())
        while z!= 1 and z!= 2 and z!= 3 and z!= 4:
            print("That is an invalid option. Select again.")
            print(" ")
            z = int(input())
        if z ==1:
            main_menu()
            print(" ")
        elif z==2:
            #viewCart()
            cur_cart.view_cart(cur_user.get_user_id())
            print(" ")
            main_menu()
        elif z == 3:
            #removeFromCart()
            cur_cart.remove_from_cart(input("Enter Title: "), cur_user.get_user_id())
            print(" ")
            main_menu()
        elif z == 4:
            #checkout(User ID)        
            cur_cart.checkout(cur_user.get_user_id())
            main_menu()
            print(" ")
        
def main_menu():
    if(cur_user.logged_in):
        menu()
    else:
        options()
