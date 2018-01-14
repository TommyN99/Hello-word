shoppinglist = []

print("Hello welcome to the item tracker for your shopping list")

x = input(("please add an item"))

shoppinglist.append(x)

print("you now have", shoppinglist, "in your shopping list")

y = input(("do you wish to add more?"))

if y ==(""):
    print("your item in the shopping list are",shoppinglist)
else:
    shoppinglist.append(y)
    print("your shopping list has been updated", shoppinglist)


