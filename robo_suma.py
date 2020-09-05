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

list_of_items=[]
