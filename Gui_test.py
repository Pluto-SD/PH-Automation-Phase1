from tkinter import *

def save_data():
	filed = open('inputdata.txt', 'a')
	filed.write('Depot:\n')
	filed.write('%s\n' % depot.get())
	filed.write('Description:\n')
	filed.write('%s\n' % description.get())
	filed.write('Address:\n')
	filed.write('%s\n' % address.get('1.0', END)) #從第一行 第0列開始get
	depot.set(None)
	#depot.delete(0, END)
	description.delete(0, END)
	address.delete(1.0, END)

app = Tk()
app.title('Head-Ex_GUI')
Label(app, text = 'Depot:').pack()
depot = StringVar()
depot.set(None)
Radiobutton(app, variable = depot, text = 'Cam, MA', value = 'Cam, MA').pack()
Radiobutton(app, variable = depot, text = 'Cam, UK', value = 'Cam, UK').pack()
Radiobutton(app, variable = depot, text = 'Seattle, WA', value = 'Seattle, WA').pack()
Label(app, text = 'Description:').pack()
description = Entry(app) #輸入單一行文字
description.pack()
Label(app, text = 'Address:').pack()
address = Text(app) #可輸入較多文字也可以多行
address.pack()
Button(app, text = 'Save', command = save_data).pack()
app.mainloop()
