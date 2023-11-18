import Item
class Inventory:
    def __init__(self):
        self.items = {}  # Dictionary to store items with their location as the key

    def add_item(self, item, location):
        self.items[location] = item 
        pass

    def remove_item(self, item, location):
        return self.items.pop(location)
        # Removes an item from the inventory at a location
        

    def edit_item(self, item, location):
        self.items[location] = item
        # Edits an item in the inventory at a location
        pass

    def get_item(self, location):
        return self.items[location]
        # Returns an item from a location

    def list_out_of_stock(self, item):
        out_of_stock = []
        # compare all items to item and if item is out of stock add to list
        for i in self.items:
            if i == item:
                out_of_stock.append(i)
        return out_of_stock
        # Lists items that are out of stock
        pass

    def search_items(self, item):
        found_items = []
        # Searches items based on a given item
        for location, inventory_item in self.items.items():
            if inventory_item == item:
                found_items.append((location, inventory_item))
        return found_items
