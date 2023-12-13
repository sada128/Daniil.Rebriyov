from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
window=Tk()
window.title('Панжин Владислав Николаевич')
window.geometry('800x600') #Размер окна
tb=ttk.Notebook(window)#Вкладки
t1=ttk.Frame(tb)
t2=ttk.Frame(tb) 
t3=Text(tb)
tb.add(t1, text='Первая вкладка')
tb.add(t2, text='Вторая вкладка')
tb.add(t3, text='Третья вкладка')
tb.pack(expand=1, fill='both')# expand позиция fill растяжение по гор. и верт. pack упорядочивает виджеты
lbl=Label(t1, text="КалькУлятор") 
lbl.grid(column=0, row=0)
#Чёртов калькулятор
e1=Entry(t1,width=5)#wigth - ширина 
e1.grid(column=0,row=1)
e2=Entry(t1,width=5)
e2.grid(column=0,row=3)
com=Combobox(t1,width=5)
com['values']=('+','-','*','/')
com.grid(column=0, row=2)
def b():
    a=int(e1.get())
    b=int(e2.get())
    if com.get()=='+':
        messagebox.showinfo('Ответ',a+b)
    if com.get()=='-':
        messagebox.showinfo('Ответ',a-b)
    if com.get()=='*':
        messagebox.showinfo('Ответ',a*b)
    if com.get()=='/':
        messagebox.showinfo('Ответ',a/b)
bt=Button(t1,text='Результат',command=b)
bt.place(relx=0.5,rely=0.5,anchor='center')# rel смещение от 0.0 до 1.0 на долю высоты и ширины
#Чекбоксы на 2 вкладке
chk= IntVar() 
chk1=Radiobutton(t2, text='Первый',value=1, variable=chk) 
chk1.grid(column=0, row=0)
chk2= IntVar() 
chk2=Radiobutton(t2, text='Второй',value=2, variable=chk) 
chk2.grid(column=1, row=0)
chk3= IntVar() 
chk3=Radiobutton(t2, text='Третий',value=3, variable=chk) 
chk3.grid(column=2, row=0)
#кнопка и дальше окно
def f():
    if chk.get()==1:
        messagebox.showinfo('Красава','Выбран 1 вариант')
    if chk.get()==2:
        messagebox.showinfo('Красава','Выбран 2 вариант')
    if chk.get()==3:
        messagebox.showinfo('Красава','Выбран 3 вариант')
bt1=Button(t2,text='Выбрать', command=f)
bt1.grid(column=1,row=2)
#Работа с текстом
def ch(): # читка с файла
    a = filedialog.askopenfilename(initialdir="1.txt", title="Откройте текстовый файл")
#initialdir - каталог, filetypes - указываем тип файла
    b=open(a,encoding="utf-8")
    s=b.read()
    t3.insert(1.0,s)
    b.close()
def ch1():
    a = filedialog.askopenfilename( filetypes=(("TXT files", "*.txt"),("All files", "*.*")))
    b=open(a,'w')
    s=t3.get(1.0,END)
    b.write(s)
    b.close()
bt2=Button(t3,text='Можно считать с файла',command=ch)
bt2.grid( row=0,sticky=E)
bt3=Button(t3,text='Записать файл',command=ch1)
bt3.grid(column=1, row=0)