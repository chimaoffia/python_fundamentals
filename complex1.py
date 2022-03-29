#list

shopping_items = ["iphone", "macbook","iwatch"]
shopping_items[2] = "airpod"
print(shopping_items)

shopping_items[0] = "redmi"
print(shopping_items)


#adding items to the list

shopping_items.append("iphone") #add items ti the last index of a list 
print(shopping_items)

shopping_items.insert(1,"tomatoes")  # add item to a specific index in a list.
print(shopping_items)

shopping_items.extend(["bread","water"]) # add multiple item to the last index.
print(shopping_items)

#removing items iside the list

shopping_items.pop(0) # remove item from a specific index.
print(shopping_items)

shopping_items.remove("tomatoes") # it revoes a specific item by it name not index.
print(shopping_items)

# shopping_items.clear() #  it clears everything
# print(shopping_items)

#slicing a list 

print(shopping_items[0:2])
print(shopping_items) #note the original items are still complete. slicing only make a copy of an aray


print(shopping_items[:])  # : means copy everything




# testing my ming (logic)
another_items = shopping_items[:]


another_items[0] = "airpod"
print(another_items)
print(shopping_items)


another_items = shopping_items
another_items[0] = "cow"
print(another_items)
print(shopping_items)