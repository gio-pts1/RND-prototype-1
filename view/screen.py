from tkinter import *
from tkinter import ttk

class MainScreen:

    def __init__(self, root) -> None:
        root.title("Main Screen")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Main Screen").grid(column=0, row=0, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

class SecondScreen:

    def __init__(self, root) -> None:
        root.title("Second screen")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        mainframe.grid(column=0, row=0, sticky=(N, W))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        l1 = ttk.Label(mainframe, text="Second Screen")

        l1.bind('<Enter>', lambda e: l1.configure(text='Move mouse inside'))
        l1.bind('<Leave>', lambda e: l1.configure(text='Move mouse outside'))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

class ThirdScreen:

    def __init__(self, root) -> None:
        root.option_add('*tearOff', FALSE)
        root.title("Third screen")
        win = Toplevel(root)
        menuBar = Menu(win)
        menu_file = Menu(menuBar)
        menuEdit = Menu(menuBar)
        
        mainframe = ttk.Frame(root, padding="3 3 12 12", width=800, height=500, style='Danger.TFrame')
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'raised'
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        l1 = ttk.Label(mainframe, text="Third Screen")
        s1 = ttk.Scrollbar(mainframe, orient=VERTICAL)

        l1.bind('<Enter>', lambda e: l1.configure(text='Move mouse inside'))
        l1.bind('<Leave>', lambda e: l1.configure(text='Move mouse outside'))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

class Routing:
    __root: ttk
    __rootframe: ttk.Frame
    __label: ttk.Label

    def __init__(self, root):
        root.title("Routing tru frames")        
        self.__root = root
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)     
        self.__rootframe = ttk.Frame(self.__root, width=200, height=400)  
        self.__label = ttk.Label(self.__rootframe, text="Null")

    def showMain(self):        
        self.__rootframe['borderwidth'] = 2
        self.__rootframe['relief'] = 'raised'
        self.__rootframe.grid(column=0, row=0)
        self.__label.grid(column=0, row=0, sticky=W)
        self.__label['text'] = "Main Screen"
        b1 = ttk.Button(self.__rootframe, text="Show Second Screen", command=self.showSec, width=5)
        b1.grid(column=1, row=0, sticky=(E, W))
        

    def showSec(self):                
        self.__rootframe['borderwidth'] = 2
        self.__rootframe['relief'] = 'sunken'
        self.__rootframe.grid(column=0, row=0)
        self.__label.grid(column=0, row=0, sticky=W)
        self.__label['text'] = "Second Screen"
        b1 = ttk.Button(self.__rootframe, text="Show Second Screen", command=self.showMain, width=5)
        b1.grid(column=1, row=0, sticky=(E, W))
        
    
        