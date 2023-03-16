import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window,text='',bg='yellow')
l.pack()
counter = 0

#设置一个按了就会加一的
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter+=1

#菜单
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=0)
#将刚刚设置过的filemenu加到按钮里面
menubar.add_cascade(label='File',menu=filemenu)
#file下属的各种命令按钮
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
#在文件中加一条线sparator
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

editmenu = tk.Menu(menubar,tearoff=0)
#将刚刚设置过的editmenu加到按钮里面
menubar.add_cascade(label='Edit',menu=editmenu)
#edit下属的各种命令按钮
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)
editmenu.add_separator()
editmenu.add_command(label='Exit',command=window.quit)

#设立分支
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label="Submenu1",command=do_job)

#将所有按钮放在window上面
window.config(menu=menubar)

window.mainloop()

