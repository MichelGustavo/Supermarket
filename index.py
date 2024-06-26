import os
from shopping_cart import *

shopping_cart = shopping_cart(None)

def menu():
    os.system('cls')
    theTotal()
    print("1. Shop\n2. Shopping Cart\n3. Exit")
    choose  = int(input("> "))
    match choose:
        case 1:
            shop()
        case 2:
            shopCrt()
        case 3:
            quit()
        case _:
            menu()

#region ShopOpctions
def shop():
    os.system('cls')
    theTotal()
    print("1. All the products\n2. Food\n3. Eletronics\n4. Furniture\n5. Exit")
    choose  = int(input("> "))
    match choose:
        case 1:
            allProducts()
        case 2:
            allFoods()
        case 3:
            allEletronics()
        case 4:
            allFurnitures()
        case 5:
            menu()
        case _:
            menu()
def allProducts():
    os.system('cls')
    theTotal()
    n = 1
    for i in all_items:
        print(f"{n}. {i.data[0]} - R${i.data[1]}")
        n+=1
    else:
        print(f"{n}. Exit")
    choose  = int(input("> "))
    if choose != n:
        shopping_cart.add(all_items[choose-1])
        allProducts()
    else:
        shop()
def allFoods():
    os.system('cls')
    theTotal()
    n = 1
    for i in all_foods:
        print(f"{n}. {i.data[0]} - R${i.data[1]}")
        n+=1
    else:
        print(f"{n}. Exit")
    choose  = int(input("> "))
    if choose != n:
        shopping_cart.add(all_foods[choose-1])
        allFoods()
    else:
        shop()
def allEletronics():
    os.system('cls')
    theTotal()
    n = 1
    for i in all_eletronics:
        print(f"{n}. {i.data[0]} - R${i.data[1]}")
        n+=1
    else:
        print(f"{n}. Exit")
    choose  = int(input("> "))
    if choose != n:
        shopping_cart.add(all_eletronics[choose-1])
        allEletronics()
    else:
        shop()
def allFurnitures():
    os.system('cls')
    theTotal()
    n = 1
    for i in all_furnitures:
        print(f"{n}. {i.data[0]} - R${i.data[1]}")
        n+=1
    else:
        print(f"{n}. Exit")
    choose  = int(input("> "))
    if choose != n:
        shopping_cart.add(all_furnitures[choose-1])
        allFurnitures()
    else:
        shop()

#endregion

#region Shopping cart
def shopCrt():
    os.system('cls')
    shopping_cart.info()
    print("1. Exit")
    choose = int(input("> "))
    match choose:
        case _:
            menu()
#endregion

# the total
def  theTotal():
    print(f"*Total(shopping cart): R${shopping_cart.total()}")



menu()

