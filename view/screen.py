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
    __labelFrame: ttk.Labelframe
    __label: ttk.Label
    __btn: ttk.Button
    __labelFrameFromRoot: ttk.Labelframe

    def __init__(self, root):
        root.title("Routing tru frames")        
        self.__root = root
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)     
        self.__rootframe = ttk.Frame(self.__root)                  
        self.__label = ttk.Label(self.__rootframe)
        self.__labelFrame = ttk.Labelframe(self.__rootframe, text="null")
        self.__btn = ttk.Button(self.__labelFrame, text="null", width=18)
        self.__labelFrameFromRoot = ttk.Labelframe(self.__root, text="null")

    def showMain(self):        
        self.__rootframe['borderwidth'] = 2
        self.__rootframe['relief'] = 'raised'
        self.__rootframe.grid(column=0, row=0)
        self.__rootframe['width'] = 400
        self.__rootframe['height'] = 400
        self.__label.grid(column=0, row=0, sticky=W)
        self.__label['text'] = "Main Screen"
        b1 = ttk.Button(self.__rootframe, text="Show Second Screen", command=self.showSec, width=5)
        b1.grid(column=1, row=0, sticky=(E, W))

    def showMainWithLabel(self):        
        self.__rootframe.grid(column=0, row=0, padx= 20, pady=20, sticky=N)
        self.__rootframe['borderwidth'] = 15
        self.__rootframe['relief'] = 'raised'          
        
        self.__labelFrame.grid(column=1, row=1, sticky=W, padx= 10, pady=10)
        self.__labelFrame['text'] = "Main Screen"        
        
        self.__label.grid(column=0, row=0, sticky=W)
        self.__label['text'] = "Main Screen"

        self.__btn['text'] = "Show lable frame only"
        self.__btn['command'] = self.showLableFrameOnly
        self.__btn.grid(column=1, row=0, sticky=(E, W))    
        

    def showSec(self):                
        self.__rootframe['borderwidth'] = 2
        self.__rootframe['relief'] = 'sunken'
        self.__rootframe.grid(column=0, row=0, sticky=(N, W, S, E))
        self.__rootframe['width'] = 400
        self.__rootframe['height'] = 400
        self.__label.grid(column=0, row=0, sticky=W)
        self.__label['text'] = "Second Screen"
        b1 = ttk.Button(self.__rootframe, text="Show Second Screen", command=self.showMain, width=5)
        b1.grid(column=1, row=0, sticky=(E, W))
        
    def showSecWithLabel(self):               
                
        self.__labelFrame.grid(column=3, row=2, sticky=W, padx= 10, pady=10)
        self.__labelFrame['text'] = "Second Screen"        

        self.__label.grid(column=0, row=0, sticky=W)
        self.__label['text'] = "Second Screen"
        
        self.__btn['text'] = "Show main screen"
        self.__btn['command'] = self.showMainWithLabel        
        self.__btn.grid(column=1, row=0, sticky=(E, W))   

    def showLableFrameOnly(self):
        self.__labelFrameFromRoot.grid(column=0, row=0, padx=10, pady=10)
        self.__labelFrameFromRoot['text'] = "Lable Frame Only"
        
        b1 = ttk.Button(self.__labelFrameFromRoot, text="Show main Screen")
        
        b1['command'] = self.showMainWithLabel        
        b1.grid(column=1, row=0, sticky=(E, W))