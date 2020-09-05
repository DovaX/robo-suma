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
import datetime

def gui_add_balance():
    global balances
    account_name=combo1.cb.get()
    amount=float(entry1.text.get())
    index=account_names.index(account_name)
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    account=accounts[index]
    account.balances[date]=amount
    print(account.balances)
    refresh_balances()
    
    
def refresh_balances():    
    balances_text="\n".join([x.name+":"+str(x.balances) for x in accounts])
    print(balances_text)
    label2.text.set(balances_text)    

gui1=dg.GUI("Robosuma")

combo1=dg.Combobox(gui1.window,account_names,1,1)
label1=dg.Label(gui1.window,"Aktuální stav",1,2)

entry1=dg.Entry(gui1.window,1,3)
btn1=dg.Button(gui1.window,"Submit",gui_add_balance,1,4)

label2=dg.Label(gui1.window,"",2,1)

gui1.build_gui()
