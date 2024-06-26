class item():
    def __init__(self,data,nome,preco=int) -> None:
        self.data = [nome,preco]
    def info(self):
        print(self.data)

#objects #[1: Name, 2: Price]

# foods
rice = item([],"Rice", int(35)) 
bean = item([],"Bean",int(10))
flour = item([],"Flour",int(7))
salt = item([],"Salt",int(6))

# Eletronics 
notebook = item([],"Notebook",int(2400))
stove = item([],"Stove",int(6700))
refrigerator = item([],"Refrigerator",int(6700))
microwave = item([],"Stove",int(2500))

# Furniture
sofa = item([],"Sofa",int(8200))
lampshade = item([],"lampshade",int(1300))
table = item([],"table",int(500))
carpet = item([],"carpet",int(200))

#Categore
all_items = [rice,bean,flour,salt,notebook,stove,refrigerator,microwave,sofa,lampshade,table,carpet]
all_foods = [rice,bean,flour,salt]
all_eletronics = [notebook,stove,refrigerator,microwave]
all_furnitures = [sofa,lampshade,table,carpet]