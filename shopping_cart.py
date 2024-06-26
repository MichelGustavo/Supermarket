from item import *

class shopping_cart():
    #Set the list of shopping cart
    def __init__(self,items) -> None:
        self.all = []
    #Add itens to shopping cart
    def add(self,item):
        self.all.append(item)
    #Return the total of all itens values
    def total(self):
        totalValue : int = 0
        for i in self.all:
            totalValue = totalValue + i.data[1]
        else:
            return totalValue
    #Print info of the list
    def info(self):
        for i in self.all:
            print(f"<>| {i.data[0]}. - price: R${i.data[1]} |")
        totalValue : int = 0
        for i in self.all:
            totalValue = totalValue + i.data[1]
        print(f'<>| Total: R${totalValue} |')
    def order_list(self):
        shopping_cart.all.sort(key= all_items.index)
    
            


