
shoppingListsarray = []
list_count = 1
item_count = 1

class ShoppingList:
    def __init__(self, store):
        self.store = store
        self.items = []
        self.id = str(list_count)
    def __repr__(self):
        return '%s\'s list id = %s : %s' % (self.store, self.id, self.items)

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.id = item_count
    def __repr__(self):
        return'%s : %s' % (self.name, self.quantity)


while True:
    grocery_input = str(input("--Options-- \n 1: Create New list \n 2: Add Items to existing list \n 3: View current lists \n 4: 'q' to quit \n"))
    if grocery_input == '1':
        name_of_new_store = input("Enter the name of the new list: ")
        new_list = ShoppingList(name_of_new_store)
        list_count += 1
        shoppingListsarray.append(new_list)
    elif grocery_input == '2':
        for i in shoppingListsarray:
            print(i)
        list_id = str(input("Enter the id of the list you want to add items to: "))
        for j in shoppingListsarray:
            if j.id == list_id:
                item_name = input("Enter the name of the item: ")
                item_quant = input("Enter the quantity: ")
                new_item = Item(item_name, item_quant)
                item_count += 1
                j.items.append(new_item)
    elif grocery_input == '3':
        for i in shoppingListsarray:
            print(i)
    elif grocery_input == '4' or grocery_input == 'q':
        break
