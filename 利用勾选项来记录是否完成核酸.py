import tkinter as tk

window=tk.Tk()
window.title('核酸检测记录表')
window.geometry('500x500')

l=tk.Label(window,bg='yellow',width=100,text='暂时无人完成核酸检测')
l.pack()

def print_selection():
    if(var1.get()==1)&(var2.get()==0):
        l.config(text='隋浩睿核酸检测为阴性，曲成义未完成核酸检测')
    elif(var1.get()==0)&(var2.get()==1):
        l.config(text='曲成义核酸检测为阴性，隋浩睿未完成核酸检测')
    elif(var1.get()==0)&(var2.get()==0):
        l.config(text='暂时无人完成核酸检测')
    else:
        l.config(text='两人均完成核酸检测且都为阴性')
    
var1=tk.IntVar()
var2=tk.IntVar()
c1 = tk.Checkbutton(window,text='隋浩睿',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c2 = tk.Checkbutton(window,text='曲成义',variable=var2,onvalue=1,offvalue=0,command=print_selection)

c1.pack()
c2.pack()
