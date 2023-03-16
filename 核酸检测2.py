import tkinter as tk

window=tk.Tk()
window.title('核酸检测记录表')
window.geometry('500x500')

l=tk.Label(window,bg='white',width=100,text='暂时无人完成核酸检测')
l.pack()

def print_selection():
    if(var1.get()==1):
        l.config(text='韦向峰完成核酸检测且为阴性')
    elif(var2.get()==1):
        l.config(text='徐冉完成核酸检测且为阴性')
    elif(var3.get()==1):
        l.config(text='宫恩溯完成核酸检测且为阴性')
    elif(var1.get()==1)&(var2.get()==1)&(var3.get()==1):
        l.config(text='419已完成核酸检测且都为阴性')
    else:
        l.config(text='暂时无人完成核酸检测')
    
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
c1 = tk.Checkbutton(window,text='韦向峰',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c2 = tk.Checkbutton(window,text='徐冉',variable=var2,onvalue=1,offvalue=0,command=print_selection)
c3 = tk.Checkbutton(window,text='宫恩溯',variable=var3,onvalue=1,offvalue=0,command=print_selection)


c1.pack()
c2.pack()
c3.pack()


window.mainloop()
