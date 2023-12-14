import requests
import json
from tkinter import *
import tkinter as tk
from pprint import pprint
window=Tk()
window.title('Json')
window.geometry('800x600')
e=Entry(window,width=15)
l=Label(window,text='Введите имя пользователя')
l.pack()
e.pack()#anchor виджет в опр. части
def f():
    a=e.get()
    username=a#имя пользователя
    url = f"https://api.github.com/users/{username}"#получение ссылки
    user_data = requests.get(url).json()#чтение с сылки
    pprint(user_data)#глянуть что считалось
    data={}
    k=['company','created_at','email','id','name','url']#ключи в словаре 
    for i in k:# проход по ключам
        data[i]=user_data[i]#добавление в словарь нужных значений
    with open("data_file.json","w") as r:
        json.dump(data,r,indent=4)#indent кол-во отступов при сериализации
bt=Button(window,text="Let's go",command=f,width=45)
bt.pack()
window.mainloop()