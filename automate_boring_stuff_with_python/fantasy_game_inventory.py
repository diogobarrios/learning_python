# Fantasy Game Inventory

# inventory of player 1:
stuff = {'rope': 1, 'torch': 6,
                    'gold coin': 42, 'dagger': 1,
                    'arrow': 12}


# Function to display what player 1 has and the total
def display_inventory(inventory):
    # Title for pretty printing
    print('Inventory:')
    # variable empty to sum all int of items in the inventory
    item_total = 0
    # For loop to show all the item in the inventory
    # .items() method to show keys and values
    for k, v in inventory.items():
        # coerce int to str and show keys
        print(str(v) + ' ' + k)
        # sum all the items
        item_total += v
        # print the value added on item_total
    print('Total number of items: ' + str(item_total))


display_inventory(stuff)

# Function to add the loot to the inventory


def add_to_inventory(inventory, added_items):
    for item in added_items:
        # This method .setdefault() will attach value of zero to item that
        # doesn't have in the inventory
        inventory.setdefault(item, 0)
        # Increases that value by one, each time that item appears
        # in the loot list
        inventory[item] += 1
    return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff_update = add_to_inventory(stuff, dragonLoot)
display_inventory(stuff_update)
