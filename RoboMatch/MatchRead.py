#!/usr/bin/env python

import tkinter
import sqlite3
from tkinter import *

def main():

    #create a window
    window = tkinter.Tk()
    f = Frame(window) #create a frame to hold some buttons

    #create a label widget
    lbl = tkinter.Label(window, text="RoboMatch")

    #pack(add) the widget to the window
    lbl.pack()
       
    #Define buttons for frame
    btnG = tkinter.Button(f, text = "Games", command = read_Games)
    btnS = tkinter.Button(f, text = "Students", command = read_Students)
    btnM = tkinter.Button(f, text="Matches", command = read_Matches)
    btnT = tkinter.Button(f, text = "Teams", command = read_Teams)
    btnQ = tkinter.Button(f, text = "Quit", command = quit)
    
    #pack it  (you can use pack or grid, but not both
    btnG.pack(side='left')
    btnS.pack(side='left')
    btnM.pack(side='left')
    btnT.pack(side='left')
    btnQ.pack(side='left')
    f.pack()

    #listbox widget to hold teams
    teamsW = tkinter.Listbox(window, height=10)
    teamsW.pack(side='left')

    #populate list box
    try:
        conn = sqlite3.connect('./RoboMatch.db')
        curs = conn.cursor()
        for row in curs.execute("SELECT * FROM teams, students where teams.student_id = students.student_id;"):
            print (row)
            teamsW.insert(END,row)
        conn.close()
    
    except EXCEPTION:
        print("teams reading exception")
          
    #Create a widget to display results
    results = tkinter.Listbox(window, height = 12, width = 30)
    S = Scrollbar(window)

    S.pack(side='right', fill=Y)
    results.pack(side='right',fill=Y)
    
    S.config(command=results.yview)
    results.config(yscrollcommand=S.set)
    
    try:
        conn = sqlite3.connect('./RoboMatch.db')
        curs = conn.cursor()
        for row in curs.execute("SELECT * FROM matches"):
            results.insert(END,row)
            print (row)
        conn.close()
            
    except EXCEPTION:
        print("match reading exception")
        pass             
    #setup scrollbar
    
    #draw the window and start application
    window.mainloop()
                     

def mainloop():
    read_Students()
    read_Teams()
    read_Matches()

def read_Games():
    print("reading games...")
    try:
        conn = sqlite3.connect("./RoboMatch.db")
        curs = conn.cursor()
        for row in curs.execute("SELECT * FROM games"):
            print(row)
        conn.close
    except EXCEPTION:
        print("exception")
        pass
             
def read_Students():
    print("read students...")
    try:
        conn = sqlite3.connect("./RoboMatch.db")
        curs = conn.cursor()
        for row in curs.execute("SELECT * FROM students"):
            print(row)
        conn.close
    except EXCEPTION:
        print("exception")
        pass
   
def read_Matches():
    print("read_Matches...")
    try:
        conn = sqlite3.connect('./RoboMatch.db')
        curs = conn.cursor()
        for row in curs.execute("SELECT * FROM matches"):
            print (row)
        conn.close()
            
    except EXCEPTION:
        print("exception")
        pass
            
def read_Teams():
    print("read_Teams...")
    try:
        conn = sqlite3.connect('./RoboMatch.db')
        curs = conn.cursor()
        for row in curs.execute("SELECT * FROM teams"):
            print (row)
        conn.close()
         
    except EXCEPTION:
        print("exception")
        pass
    
    
#     with open('teams.csv') as csvfile:
#         teams = csv.reader(csvfile)
#         for row in teams:
#             if teams.line_num >1:
#                 print (row)
                      

if __name__ == '__main__':
    
    #print(os.listdir(os.getcwd()))
    main()
    
