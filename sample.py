from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('300x200-800+380')
root.attributes("-alpha", 0.8)
root.winfo_screen()

menuBar = Menu(root)
menu_file = Menu(menuBar)
menu_edit = Menu(menuBar)
menuBar.add_cascade(menu=menu_file, label='File')
menuBar.add_cascade(menu=menu_edit, label='Edit')


menu_file.add_command(label='New')
menu_file.add_command(label='Open...')
menu_file.add_command(label='Close')


root['menu'] = menuBar

ttk.Button(root, text="testing").grid()
root.mainloop()

