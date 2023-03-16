import tkinter as tk

window = tk.Tk()
window.title('可输入窗口')
window.geometry('200x200')
window.config(bg='blue')

# 可输入界面  依附于window  show指输入显示，=None 则是显示你本来输入的 ='* '则显示*
e=tk.Entry(window, show=None)
#放到窗口中
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    t.insert('end',var)
def insert_front():
    var=e.get()
    t.insert(0.0,var)

#设置按钮，command指按钮满足xxx函数
b1=tk.Button(window,text='插入到光标处',width=15,height=2,command=insert_point)
b1.pack()

b2=tk.Button(window,text='插入到首行',width=15,height=2,command=insert_front)
b2.pack()

b3=tk.Button(window,text='插入到尾部',width=15,height=2,command=insert_end)
b3.pack()

#文本框
t=tk.Text(window,height=10)
t.pack()

window.mainloop()
