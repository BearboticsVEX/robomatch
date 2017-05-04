#!/usr/bin/env python
import tkinter as tk

#MODIFY STRUCTURE
# class Navbar(tk.Frame): ...
# class Toolbar(tk.Frame): ...
# class Statusbar(tk.Frame): ...
# class Main(tk.Frame): ...
# 
# class MainApplication(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self.statusbar = Statusbar(self, ...)
#         self.toolbar = Toolbar(self, ...)
#         self.navbar = Navbar(self, ...)
#         self.main = Main(self, ...)
# 
#         self.statusbar.pack(side="bottom", fill="x")
#         self.toolbar.pack(side="top", fill="x")
#         self.navbar.pack(side="left", fill="y")
#         self.main.pack(side="right", fill="both", expand=True)
#         


# class structure Tk template from http://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.parent = parent
        self.value = None  #for listbox index

        
        
        
        
        termList = tk.Listbox(self, selectmode="SINGLE")

        termList.insert(0, "F15")
        termList.insert(1, "S16")
        termList.insert(2, "F16")
        termList.insert(3, "S17")
        termList.insert(4, "F17")
        termList.insert(5, "S18")
        
        termList.pack(side="left")
            
        
        self.periodList = tk.Listbox(self, selectmode="BROWSE")
        self.periodList.bind("<Return>", self.readMatches)
        
        for periodVal in range(1,9):
            self.periodList.insert(periodVal, periodVal)
        
        #p = tk.Radiobutton(root, text=periodLabel, value=2, variable=self.py, command=MatchW.ShowChoice(self))
        self.periodList.pack()

        readMatchesB = tk.Button(self, text="SELECT matches from db", command=self.readMatches)
        readMatchesB.pack()
        
        q = tk.Button(root, text="QUIT", fg="red", command=self.master.destroy)
        q.pack()
        
    def readMatches(self, event=None):
            try:
                firstIndex = self.periodList.curselection()[0]
                print("firstIndex :", firstIndex)
                self.value = self.periodList[int(firstIndex)]  #something is wrong with this conversion
                
            except IndexError:
                print ("readMatches index error")
                self.value = None
            #self.periodList.destroy()  #why are we destroying this list?
            
            #print ("read matches %d %s", index, value)
        
        
        #def ShowChoice(self):
         
        #print ("your CHOICE is", MatchW.py.get() )
        #print("button:", method)
        
# Robot match score recorder GUI app
#
# base object is a robot match, where two to four teams 
# student, each student is assigned to a team with one or two
#   students who participates in matches against other teams from the same class.
#   During a semester, students will change teams
#

#instance variables ___________________________________________________________________
class Student(object):
    def __init__(self, name, term, period):
        self.name = name 
        self.term = term         #ex: F16, S17
        self.period = period     #i.e. integer - class period 1-9

#approx ten teams per class of ~20 students
#each team has 1-3 student members
class Team(object):    
    def __init__(self, student, game, period, teamNum):
        self.game = game     # String-each student will be on different teams for each game
        self.period = period # integers 1-9   
        self.teamNum = teamNum #integers 1-30
        self.student = student #there are two to three students on each team

# all teams will particiapte in several different games each semester        
class Match(object):
    def __init__(self, game, gameType, date, team1, team2, team1score, team2score):
        self.game = game
        self.gameType = gameType #boolean 0-practice, 1-tournament
        self.date = date
        self.team1 = team1
        self.team2 = team2
        self.team1score = team1score
        self.team2score = team2score
  

        
    
        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    root.destroy
