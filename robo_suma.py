class Item:
    def __init__(self,category,name,date,amount):
        self.category=category
        self.name=name
        self.date=date        
        self.amount=amount

class Account:
    def __init__(self,name,owner):
        self.name=name
        self.owner=owner
        self.balances={}

Item("buy","clothes","2020-04-09",350)

accounts=[]
account_names=[x.name for x in accounts]

list_of_items=[]
import dogui.dogui_core as dg
gui1=dg.GUI("Robosuma")

combo1=dg.Combobox(gui1.window,account_names,1,1)
label1=dg.Label(gui1.window,"Aktuální stav",1,2)

entry1=dg.Entry(gui1.window,1,3)

label2=dg.Label(gui1.window,"",2,1)

gui1.build_gui()
