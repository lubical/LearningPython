'''import tkinter

top = tkinter.Tk()
hello = tkinter.Label(top,text='hello world!')
hello.pack()

quit = tkinter.Button(top,text='QUIT',command=top.quit,bg='red',fg='white')
quit.pack(fill=tkinter.X,expand=1)
tkinter.mainloop()

from tkinter import *
def resize(ev=None):
    label.config(font='Helvetica -%d bold' % \
                      scale.get())

top = Tk()
top.geometry('250x150')

label = Label(top,text='hello world!',font='Helvetica -12 bold')
label.pack(fill=Y,expand=1)

scale = Scale(top,from_=10,to=50,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)

quit = Button(top,text='QUIT',command=top.quit,activeforeground='white',activebackground='red')
quit.pack()

mainloop()

import tkinter as tk

windows = tk.Tk()
windows.title('test windows!!')
windows.geometry('500x300')
label=tk.Label(windows,text='hello tkinter!',bg='green',font=('Arial',12))
label.pack()

windows.mainloop()
'''
'''
import tkinter as tk

window = tk.Tk()
window.title("this is a test window!!!")
window.geometry("500x350")
var = 'hello'
l = tk.Label(window,text=var,bg='green',fg='red',width=30,height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var = 'you hit me'
    else:
        on_hit = False
        var = ''

b = tk.Button(window,text="hit me",font=('Arial',12),width=10,height=1,command=hit_me)
b.pack()

tk.mainloop()
'''
'''
import tkinter as tk
window = tk.Tk()
window.title("this is a test window!!!")
window.geometry("1024x1024")
e1 = tk.Entry(window,show="*",font=("Arial",14))
e2 = tk.Entry(window,show=None,font=("Arial",14))
e1.pack()
e2.pack()
window.mainloop()
'''
'''
import tkinter as tk
window = tk.Tk()
window.title("this is a test window!!!")
window.geometry("500x500")

e = tk.Entry(window,show = None)
e.pack()

def insert_point():
    var = e.get()
    t.insert("insert",var)
def inset_end():
    var = e.get()
    t.insert('end',var)

b1 = tk.Button(window,text="insert point",command=insert_point)
b1.pack()

b2 = tk.Button(window,text="insert end",command=inset_end)
b2.pack()

t = tk.Text(window,height=3)
t.pack()

window.mainloop()
'''
'''
import tkinter as tk
window = tk.Tk()
window.title("this is a test window!!!")
window.geometry("500x500")

var1 = tk.StringVar()
l = tk.Label(window,bg="green",fg="yellow",font=('Arial',14),width=20,textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window,text="print selection",command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((1,2,3,4))

lb = tk.Listbox(window, listvariable=var2)

list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,"second")
lb.delete(2)
lb.pack()

window.mainloop()
'''
'''
import tkinter as tk
window = tk.Tk()
window.title("this is a test window!!!")
window.geometry("500x500")

var=tk.StringVar()
l = tk.Label(window,bg="green",width=20,text='empty')
l.pack()

def print_selection():
    l.config(text="you have selected" + var.get())

r1 = tk.Radiobutton(window,text='option A',variable=var,value='A',command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window,text='option B',variable=var,value='B',command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window,text='option C',variable=var,value='C',command=print_selection)
r3.pack()

window.mainloop()
'''
'''
import tkinter as tk
window = tk.Tk()
window.title("this is a test window!!!")
window.geometry("500x500")

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):     # 如果选中第一个选项，未选中第二个选项
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):   # 如果选中第二个选项，未选中第一个选项
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):   # 如果两个选项都未选中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')

var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)    # 传值原理类似于radiobutton部件
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

window.mainloop()
'''
'''
import tkinter as tk
window = tk.Tk()
window.title("this is a test window!!!")
window.geometry("500x500")

l = tk.Label(window,text=" ",bg="green",width=20)
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text="do " + str(counter))
    counter+=1

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="NEW",command=do_job)
filemenu.add_command(label="OPEN",command=do_job)
filemenu.add_command(label="SAVE",command=do_job)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)

editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)

editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label="Import",menu=submenu,underline=0)

submenu.add_command(label="Sunmenu_1",command=do_job)

window.config(menu=menubar)
window.mainloop()
'''

import pymysql
import tkinter as tk

db = pymysql.connect(host='localhost',      #数据库连接
                             user='root',
                             password='123456',
                             db='test',
                             port=3306,
                             charset='utf8')
cursor = db.cursor()

def db_add(): #增加功能
    sql = """INSERT INTO user(name)
                 VALUES ('Mac')"""
    try:

        cursor.execute(sql)

        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

def db_delete(): #删除功能
    sql = "DELETE FROM user WHERE id  = 1"
    try:
        cursor.execute(sql)

        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

def db_chaxun(): #查询功能
    sql = "SELECT * FROM user"

    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        t.delete(1.0,'end')
        for row in results:
            id = row[0]
            name = row[1]
            t.insert('end','id=%s,  name=%s\r\n' % \
                     (id,name))
            # 打印结果
            #print("id=%s,name=%s" % \
            #      (id, name))
    except:
        print("Error: unable to fecth data")

def db_close():
    db.close()

counter = 0
def do_job():
    global counter
    l.config(text=str(counter))
    counter+=1

window = tk.Tk()
window.title("this is a test window!!!")
window.geometry("800x500")#创建根窗口

l = tk.Label(window,text=' ',bg='green',width=20)
l.pack()

frame = tk.Frame(window)
frame.pack()#创建一个主frame，长在主window窗口上

#frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
#frame_l.pack(side="left",fill='x')
frame_r.pack()#第二层框架，左右形式

#tk.Label(frame_l,text="hello",font=("Arial",18)).pack()
#tk.Label(frame_r,text="123").pack()

frame_up = tk.Frame(frame_r)#第三层框架，上下形式
frame_down = tk.Frame(frame_r)
frame_up.pack(side="top")
frame_down.pack(side="bottom")

frame_ul = tk.Frame(frame_up)#第四层框架，左右形式
frame_ur = tk.Frame(frame_up)
frame_ul.pack(side="left")
frame_ur.pack(side="right")
#tk.Label(frame_ul,text="输入查询条件",font=('Arial',18)).pack()
e1 = tk.Entry(frame_ul, show=None, font=('Arial', 14))
e1.pack()
e2 = tk.Button(frame_ur, text='增加',width=10,height=1,command=db_add)
e2.pack(side="left",fill='both')
e3 = tk.Button(frame_ur,text='删除',width=10,height=1,command=db_delete)
e3.pack(side="left",fill='both')
e4 = tk.Button(frame_ur,text='查询',width=10,height=1,command=db_chaxun)
e4.pack(side="left",fill='both')

frame_dt = tk.Frame(frame_down)#第五层框架，上下形式
frame_db = tk.Frame(frame_down)
frame_dt.pack(side="top")
frame_db.pack(side="bottom")
t= tk.Text(frame_dt,height=30,width=70)
t.pack()
r1= tk.Radiobutton(frame_db, text='1',value='1')
r1.pack(side="left",fill='both')
r2= tk.Radiobutton(frame_db, text='2',value='2')
r2.pack(side="left",fill='both')
r3= tk.Radiobutton(frame_db, text='3',value="3")
r3.pack(side="left",fill='both')
r4= tk.Radiobutton(frame_db, text='4',value="4")
r4.pack(side="left",fill='both')
r5= tk.Radiobutton(frame_db, text='5',value='5')
r5.pack(side="left",fill='both')


menubar = tk.Menu(window)

filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="计划管理",menu=filemenu)

filemenu.add_command(label="生成",command=do_job)
filemenu.add_command(label="工单流程定义",command=do_job)
filemenu.add_command(label="维护",command=do_job)
filemenu.add_command(label="查询工单",command=do_job)
filemenu.add_command(label="生产进度查询",command=do_job)
filemenu.add_separator()
filemenu.add_command(label="关闭数据库",command=db_close)

editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="生产过程",menu=editmenu)

editmenu.add_command(label='工序登陆',command=do_job)
editmenu.add_command(label='工序处理',command=do_job)

shujumenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="数据维护",menu=shujumenu)

shujumenu.add_command(label="用户信息",command=do_job)
shujumenu.add_command(label="权限信息",command=do_job)
shujumenu.add_command(label="工序定义",command=do_job)
shujumenu.add_command(label="用户操作工序定义",command=do_job)

chaxunmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="查询统计报表",menu=chaxunmenu)

chaxunmenu.add_command(label="各工序完成情况统计和时间",command=do_job)
chaxunmenu.add_command(label="各操作完成情况统计和时间",command=do_job)
chaxunmenu.add_command(label="各工单完成情况统计和时间",command=do_job)



submenu = tk.Menu(filemenu)
filemenu.add_cascade(label="Import",menu=submenu,underline=0)

submenu.add_command(label="Sunmenu_1",command=do_job)

window.config(menu=menubar)

window.mainloop()