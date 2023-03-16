import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window,bg='blue',height=100,width=200)

'''
如果想要插入图片
image_file = tk.PhotoImage(file='xxxxx.gif')
anchor 指锚定的原点  nw指西北角  center中心
image = canvas.create_image(0,0,anchor='  ',image=image_file)

'''

#创建一个坐标
x0,y0,x1,y1 = 50,50,80,80
#绘制一条线段
line = canvas.create_line(x0,y0,x1,y1)
#绘制一个圆
oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
#绘制一个扇形  start   extent  指扇形张开的角度
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180)
#绘制一个矩形
rect = canvas.create_rectangle(100,30,100+20,30+20)
canvas.pack() 

#设置移动的函数，指可以将矩形移动  图，右，下
def moveit():
    canvas.move(rect,1,2)

b = tk.Button(window,text='move',command=moveit).pack()

window.mainloop()
