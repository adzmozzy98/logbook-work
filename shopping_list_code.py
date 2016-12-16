print("shopping list = 0") 
shoppinglist = " "
items = []

while shoppinglist != "":
    shoppinglist = input("enter a item: ")
    if shoppinglist != "":
        items.append(shoppinglist)
print("shoppinglist: ", items)
print(len(items))
