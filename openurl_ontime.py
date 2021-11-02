import webbrowser as web
import tkinter as tk
# url = 'www.baidu.com'
# web.open(url)

def btnl_click():
    lbox1.insert(tk.END, ent1.get())

def lbox1_click(e):
    w=e.widget
    global citem
    citem=w.curselection()
    lb11.config(text=w.get(citem))

def btn2_click():
    lbox1.delete(citem)

form1=tk.Tk()
form1.title('定时打开网页')
form1.geometry('400x300+200+200')
lb11=tk.Label(form1, text='网址')
lb11.pack(anchor=tk.W)

lbox1=tk.Listbox(form1)
lbox1.pack(anchor=tk.W)
lbox1.bind('<<ListboxSelect>>', lbox1_click)

ent1=tk.Entry(form1)
ent1.pack(anchor=tk.W, side=tk.LEFT)

btn1=tk.Button(form1, text='增加', command=btnl_click)
btn1.pack(anchor=tk.W, side=tk.LEFT)

btn2=tk.Button(form1, text='删除', command=btn2_click)
btn2.pack(anchor=tk.W, side=tk.LEFT)

text = lbox1.get(1,3)
print(text)
form1.mainloop()


