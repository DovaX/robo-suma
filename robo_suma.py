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

class MoneySupply:
    def __init__(self,name):
        self.name=name
    
class Lender:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

M1=MoneySupply("M1")
M2=MoneySupply("M2")
M3=MoneySupply("M3")

lender=Lender("Friend1",200)
Item("buy","clothes","2020-04-09",350)

FIO_Main=Account("FIO_Main","Dominik")
FIO_V=Account("FIO_V","Dominik")
FIO_OSVC=Account("FIO_OSVC","Dominik")
FIO_Replicator=Account("FIO_Replicator","Replicator")

FIO_Vault13=Account("FIO_Main","Dominik a Dan")
KB=Account("KB","Dominik")
RB=Account("RB","Dominik")
Cash=Account("Cash","Dominik")
#

accounts=[FIO_Main,FIO_V,FIO_OSVC,KB,RB,Cash]
account_names=[x.name for x in accounts]

list_of_items=[]
import dogui.dogui_core as dg
import datetime
import pandas as pd

def add_category():
    pass

def insert_or_update_balance(df,account_name,date,amount):
    balances_df=balances_table.select_to_df()
    existing_balance_df=balances_df[(balances_df['account_name']==account_name) & (balances_df['date']==date)]
    if len(existing_balance_df)==0:
        balances_table.insert_from_df(df)
    #TODO
    #elif existing_balance_df['account_name']==:
    #     balances_table.update("amount="+str(amount),"")
        
def gui_add_balance():
    account_name=combo1.cb.get()
    amount=float(entry1.text.get())
    index=account_names.index(account_name)
    date=entry3.text.get()
    account=accounts[index]
    account.balances[date]=amount
    df=pd.DataFrame([[account_name,date,amount]])

    insert_or_update_balance(df,account_name,date,amount)

    
    refresh_balances()

    
def refresh_balances():    
    balances=balances_table.select_to_df()
    balances_text=balances['account_name']+":"+balances['amount'].astype(str)
    
    #balances_text="\n".join([x.name+":"+str(x.balances) for x in accounts])
    print(balances_text)
    
    label2.text.set(balances)  

def gui_add_expense():
    
    category=combo4.cb.get()
    name=entry5.text.get()
    date=entry6.text.get()
    amount=float(entry7.text.get().replace(",","."))
   
    new_expenses_df=pd.DataFrame([[category,name,date,amount]],columns=["category","name","date","amount"])
    expenses_table.insert_from_df(new_expenses_df)
    
    entry5.text.set("")
    entry6.text.set("")
    entry7.text.set("")
    
    
    
def gui_add_income():
    
    category=combo4.cb.get()
    name=entry5.text.get()
    date=entry6.text.get()
    amount=float(entry7.text.get().replace(",","."))
   
    new_incomes_df=pd.DataFrame([[category,name,date,amount]],columns=["category","name","date","amount"])
    incomes_table.insert_from_df(new_incomes_df)
    
    entry5.text.set("")
    entry6.text.set("")
    entry7.text.set("")
    
    
def gui_add_account():
    pass

import dbhydra.dbhydra.dbhydra_core as dh

db1=dh.XlsxDB("RobosumaDB")
db1.create_database()

balances_table=dh.XlsxTable(db1,"balances",["id","account_name","date","amount"])
expenses_table=dh.XlsxTable(db1,"expenses",["id","category","name","date","amount"])
incomes_table=dh.XlsxTable(db1,"incomes",["id","category","name","date","amount"])

gui1=dg.GUI("Robosuma")
today=datetime.datetime.now().strftime("%Y-%m-%d")    
label3=dg.Label(gui1.window,"Datum",1,2)
entry3=dg.Entry(gui1.window,1,3,today)
combo1=dg.Combobox(gui1.window,account_names,2,1)
label1=dg.Label(gui1.window,"Aktuální stav",2,2)
entry1=dg.Entry(gui1.window,2,3)
btn1=dg.Button(gui1.window,"Submit",gui_add_balance,2,4)
label2=dg.Label(gui1.window,"",3,1)
label3=dg.Label(gui1.window,"Income and expenses:",3,2)
label4=dg.Label(gui1.window,"Category:",4,2)
categories=['falk','fryb','rest','fast','vbuy','vpos','buy','obl','call','ubyt','food','cest','benz','rekr','mam','lost','int','eroz','drnk','hair','pokr','kb','douc','heal','games','sport','kolo','osvc','repl']
combo4=dg.Combobox(gui1.window,categories,4,3)
label5=dg.Label(gui1.window,"Name:",5,2)
entry5=dg.Entry(gui1.window,5,3)
label6=dg.Label(gui1.window,"Date:",6,2)
entry6=dg.Entry(gui1.window,6,3)
label7=dg.Label(gui1.window,"Amount:",7,2)
entry7=dg.Entry(gui1.window,7,3)
btn7=dg.Button(gui1.window,"Add expense",gui_add_expense,7,4)
btn8=dg.Button(gui1.window,"Add income",gui_add_income,8,4)
btn8=dg.Button(gui1.window,"Add account",gui_add_account,9,4)


gui1.build_gui()
