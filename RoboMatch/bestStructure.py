# python

import tkinter as tk
from tkinter import ttk

class Navbar(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        navbar = tk.Frame()
        navbar.pack()
        
        TERMS = [
                ("F16"),
                ("S17"),
                ("F17"),
            ]
        
        
        self.term = tk.StringVar()
        self.term.set("S17")
        
        for text in TERMS:
            b = tk.Radiobutton(navbar, text=text, value=text, variable = self.term, command = self.updateStatus)
            b.pack(side="left")     
        
        b.radiobutton = self.term
        
        self.period = tk.IntVar()
        self.period.set = 2
        
        for periodVal in range(1,9):
            p = tk.Radiobutton(root, text=periodVal, value=periodVal, variable = self.period, command = self.updateStatus)
            p.pack() 
        
        p.radiobutton = self.period
        
        

    def updateStatus(self):
            print("term: ", self.term.get(), "period:", self.period.get())
    
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.navbar = Navbar(self)
        self.navbar.pack(side="left", fill="y")

        master = tk.Frame()
        master.pack()
        
        #<create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
