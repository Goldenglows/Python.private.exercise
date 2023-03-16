import tkinter as tk

window=tk.Tk()
window.title('window')
window.geometry('200x200')

l=tk.Label(window,bg='blue',width=40,text='I do not love either')
l.pack()

def print_selection():
    if(var1.get()==1)&(var2.get()==0):
        l.config(text='I love only Python')
    elif(var1.get()==0)&(var2.get()==1):
        l.config(text='I love only Java')
    elif(var1.get()==0)&(var2.get()==0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')
    

'''

text      显示内容
variable：
onvalue   如果选择了  显示是1，不显示是0
offvalue  如果没选择  显示是1，不显示是0

'''
var1=tk.IntVar()
var2=tk.IntVar()
c1 = tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c2 = tk.Checkbutton(window,text='Java',variable=var2,onvalue=1,offvalue=0,command=print_selection)

c1.pack()
c2.pack()
