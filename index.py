from tkinter import *
from view.screen import *

route = 4

root = Tk()
if(route == 1):
    MainScreen(root)
elif(route == 2):
    SecondScreen(root)
elif(route == 3):
    ThirdScreen(root)
elif(route == 4):
    r = Routing(root)
    r.showMain()
    

root.mainloop()