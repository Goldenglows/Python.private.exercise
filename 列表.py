import tkinter as tk

window = tk.Tk()
window.title('列表部件')
window.geometry('200x200')

var1 = tk.StringVar()
l=tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

def print_selection():
   #光标选择
    value= lb.get(lb.curselection())
    var1.set(value)
    
b1 = tk.Button(window,text='print selection',width=15,height=2,command=print_selection)
b1.pack()

#定义元组构成初始的列表
var2 = tk.StringVar()
var2.set((1,2,3,4))
lb=tk.Listbox(window,listvariable=var2)
#自己写一个列表，接下来对原有的列表进行插入
list_items = [5,6,7,8]
for item in list_items:
    lb.insert('end',item)

lb.insert(0,'0')
lb.delete(2)

lb.pack()
