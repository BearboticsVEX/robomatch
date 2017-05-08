# python

import tkinter as tk
from tkinter import ttk
import sqlite3
import sys
from _sqlite3 import DatabaseError
from tkinter.constants import EXTENDED, BOTTOM
from tkinter.ttk import Label
from astropy.wcs.docstrings import row
from tkinter.messagebox import showinfo
            
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        #navigation frame  ------------------------------------------------------
        navbar = tk.Frame(borderwidth=3, background="white").pack(side="left")
        Label(navbar, text="Select Term").pack(side="top")
        
        TERMS = [
                ("F16"),
                ("S17"),
                ("F17"),
            ]
        
        self.term = tk.StringVar()
        self.term.set("F16")
        
        for text in TERMS:
            b = tk.Radiobutton(navbar, text=text, bg="light blue", value=text, variable = self.term, command = self.updateStatus)
            b.pack(side="top")     
        
        b.radiobutton = self.term
        
        periodW = tk.Frame(borderwidth=3).pack(side="right")
        Label(periodW, text="Select Period").pack(side="left")
        
        self.period = tk.IntVar()
        self.period.set(3)
        
        for periodVal in range(1,9):
            p = tk.Radiobutton(periodW, text=periodVal, bg="light blue", value=periodVal, variable = self.period, command = self.updateStatus)
            p.pack(side="left") 
        
        p.radiobutton = self.period
        
        
        #Games __________________________________________________________________________________________________________
        gamesW = tk.Frame()
        gamesW.pack(side="top")
        Label(gamesW, text="Select Game").pack(side="top")
        
        #listbox widget to select game
        self.game = tk.StringVar()
        self.game.set("Protobot")
        
        self.gameListBox = tk.Listbox(gamesW, height=4, selectmode="SINGLE")
        self.gameListBox.pack(side="top")
        self.gameListBox.bind("<Double-Button-1>", self.OnDouble)

        #populate list box
        try:
            conn = sqlite3.connect('./RoboMatch.db')
            curs = conn.cursor()
            
            for row in curs.execute("SELECT game FROM games ORDER BY gameid"):
                self.gameListBox.insert(tk.END,row)
            conn.close()
            
        except DatabaseError:
            print("teams reading exception")
            e = sys.exc_info()[0]
            print(">Error: %s</p>" % e )
            pass        

        #Frame for listing students -----------------------------------------------------------------------------------
        studentsW = tk.Frame() 
        studentsW.pack(side="right")
        Label(studentsW, text="Students").pack(side="top")
         
        student = tk.StringVar()
         
        self.studentsListBox = tk.Listbox(studentsW, height=4, selectmode="SINGLE")
        self.studentsListBox.pack(side="left")
        #studentsListBox.bind("<Double-Button-1>", self.OnDouble)
 
        #populate list box
        try:
            conn = sqlite3.connect('./RoboMatch.db')
            curs = conn.cursor()
             
            curs.execute('SELECT * FROM students WHERE term = ? AND period = ?', (self.term.get(), self.period.get()))
            all_rows = curs.fetchall()
            #print (all_rows)
             
            self.studentsListBox.delete(0,tk.END)    
            for row in all_rows:          
               self.studentsListBox.insert(tk.END,row)
            conn.close()
             
        except DatabaseError:
            print("students reading exception")
            e = sys.exc_info()[0]
            print(">Error: %s</p>" % e )
            pass
        
        
        #Frame for teams -------------------------------------------------------------------
        teamW = tk.Frame()
        teamW.pack()
        Label(text="Teams").pack(side="right")
        
        team = tk.StringVar()
         
        self.teamsListBox = tk.Listbox(teamW, height=12, selectmode="SINGLE")
        self.teamsListBox.pack(side="left")
        #studentsListBox.bind("<Double-Button-1>", self.OnDouble)
 
        #populate list box
        try:
            conn = sqlite3.connect('./RoboMatch.db')
            curs = conn.cursor()
            
            #print('SELECT * FROM teams WHERE term = ? AND period = ?', (self.term.get(), self.period.get()))
            
            #curs.execute('SELECT * FROM teams WHERE term = ? AND period = ?', (self.term.get(), self.period.get()))
            curs.execute('SELECT * FROM teams')
            all_rows = curs.fetchall()
            print("teams data")
            print (all_rows)
             
            self.teamsListBox.delete(0,tk.END)    
            for row in all_rows:          
               self.teamsListBox.insert(tk.END,row)
            conn.close()
             
        except DatabaseError:
            print("teams reading exception")
            e = sys.exc_info()[0]
            print(">Error: %s</p>" % e )
            pass

        #Frame for matches
        matchW = tk.Frame()
        matchW.pack()
        Label(text="Matches").pack(side="right")    
        master = tk.Frame()
        master.pack()
        
        #<create the rest of your GUI here>
        
        
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        #print ("selection:", selection, value)
        self.game.set(value)
        self.updateStatus()
                
    def updateStatus(self):
        #print("updateStatus ---->  term: ", self.term.get(), "period:", self.period.get()," game: ",self.game.get())
        
        #populate students list box with selected term and period
        try:
            conn = sqlite3.connect('./RoboMatch.db')
            curs = conn.cursor()
            
            #print('SELECT * FROM students WHERE term = ?', (self.term.get(),))
            curs.execute('SELECT * FROM students WHERE term = ? AND period = ?', (self.term.get(), self.period.get()))
            all_rows = curs.fetchall()
            #print (all_rows)
            
            self.studentsListBox.delete(0,tk.END) 
            for row in all_rows:
                self.studentsListBox.insert(tk.END,row)
            conn.close()
            
        except DatabaseError:
            print("students reading exception")
            e = sys.exc_info()[0]
            print(">Error: %s</p>" % e )
            pass

        #re-populate teams list box
        self.teamsListBox.delete(0,tk.END) 
        try:
            conn = sqlite3.connect('./RoboMatch.db')
            curs = conn.cursor()
            period = self.period.get()
                     
            curs.execute('SELECT * FROM students WHERE period = ?', (period, ))
            #curs.execute('SELECT * FROM teams WHERE term = ? AND period = ?', ('F16', ))
            all_rows = curs.fetchall()
            print (all_rows)
                
            for row in all_rows:          
               self.teamsListBox.insert(tk.END,row)
            conn.close()
             
        except DatabaseError:
            print("teams reading exception")
            e = sys.exc_info()[0]
            print(">Error: %s</p>" % e )
            pass


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
