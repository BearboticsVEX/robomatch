import tkinter as tk
import sqlite3

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
    
     
        #original listbox on double code 
        term = tk.Listbox(self)

        term.insert("end", "F16")
        term.insert("end", "S17")

        term.bind("<Double-Button-1>", self.OnDouble)
        term.pack(side="top")

        pd = tk.Listbox(self)

        pd.insert("end", "2")
        pd.insert("end", "3")
        pd.insert("end", "9")

        pd.bind("<Double-Button-1>", self.OnDouble)
        pd.pack(side="top")
  
             
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print ("widget:", widget, "selection:", selection, ": '%s'" % value)
        

        
        try:
            conn = sqlite3.connect('./RoboMatch.db')
            curs = conn.cursor()
            for row in curs.execute("SELECT * FROM matches"):
                #results.insert(END,row)
                print (row)
            conn.close()
                
        except conn:
            print("match reading exception")
            pass             
        #setup scrollbar       

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
