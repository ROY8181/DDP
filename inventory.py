inventory = {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    elif item not in inventory:
        inventory[item] =quantity
    else:
        pass

add_item("pear",7)
print(inventory)

def update_item(item, quantity):
    if item in inventory:
        inventory[item]= quantity
    else:
        print("The inventory name is not found")
