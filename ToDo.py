# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:45:40 2021

@author: arjun
"""

from tkinter import *
from PIL import Image, ImageTk

main = Tk()
main.title("To Do Planner")
#logo = Image.open("Logo.png")
#icon = ImageTk.PhotoImage(logo)
#main.iconphoto(False, icon)

class todo:
    
    logtxt = Label()
    logdisp = False
    CbxList = []
    Var = []
    
    def __init__(self):
        #main.geometry('200x200')
        #main.configure(bg = "#a9eed1")
        main.configure(bg = "#b6e1f6")
        self.titleicon()
        self.DisplayTitle()
        self.log()
        self.TxtEnt()
        self.SavedNotes()
        self.Update()
    
    def titleicon(self):
        global ph
        icon = Image.open("ToDo.png")
        ph = ImageTk.PhotoImage(icon)
        icn = Label( image = ph)
        #self.ph = ImageTk.PhotoImage(icon)
        #xyz = icon
        #icn.ima
        icn.pack()
        #load = Image.open("logo.jpg")
        #render = ImageTk.PhotoImage(load)
        #img = Label(main, image=render)
        #img.image = render
        #img.place(x=0, y=0)
        
    
    def DisplayTitle(self):
        title = Label(main, text = "To-Do List", bg = "#b6e1f6", fg = "white", font = "Courier").pack(side = TOP, pady = 5)
    
    def log(self, logstatus = ''):
        self.logtxt = Label(main, text = "Log: ", bg = "#b6e1f6", fg = "white")
        self.logtxt.pack(side = BOTTOM)
        
    
    def logstatus(self, logmsg):
            self.distroylog()
        #if(self.logdisp == False):
            self.logtxt = Label(main, text = "Log: " + logmsg, bg = "#b6e1f6", fg = "white")
            self.logtxt.pack(side = BOTTOM)
            self.logdisp = True
    
    def distroylog(self):
        self.logtxt.destroy()
    
    
    def TxtEnt(self):
        global addbn
        icon = Image.open("AddBtn3.png")
        icon = icon.resize((80, 20), Image.ANTIALIAS)
        addbn = ImageTk.PhotoImage(icon)
        
        note = StringVar()
        addtask = Entry(main, textvariable = note).pack()
        SubBtn = Button(main, text = "Add!",image = addbn, command = lambda:self.AddTask(note), bg = "#f9d6d6").pack(pady = 5)
        
    def AddChk(self, Note):
        noteindex = len(self.Var)
        self.Var.append(IntVar())
        cbx = Checkbutton(main, text = Note,selectcolor = "#f9d6d6", variable = self.Var[noteindex], onvalue = 1, offvalue = 0, bg = "#b6e1f6", activebackground = "#f9d6d6", font = "Courier")
        cbx.pack(pady = 1)
        self.CbxList.append(cbx)
        #self.distroylog()
        self.logstatus('Added!')
        
    def SaveFile(self, notefile):
        notefile.close()
    
    def AddTask(self, note):
        
        Note = note.get()
        self.AddChk(Note)
        notefile = open("tasks.txt", "a+")
        notefile.write(Note)
        notefile.write("\n")
        self.SaveFile(notefile)
        
        #tmpcbx = Checkbutton(main, text = Note, variable = self.Var[noteindex], onvalue = 1, offvalue = 0)
        #tmpcbx.pack()
        
        #tmpcbx.pack()
        #print(self.CbxList)
        #for i in self.Var:
        #    tmp = i.get()
        #    print(tmp)
        #print(self.Var[0].get())
        #xyz = self.CbxList[0]["variable"]
        #print(xyz.get())
    
    def SavedNotes(self):
        notefile = open("tasks.txt", "r")
        tasks = notefile.read().splitlines()
        self.SaveFile(notefile)
        noteindex = 0
        for task in tasks:
            self.Var.append(IntVar())
            tmpcbx = Checkbutton(main, text = task,selectcolor = "#f9d6d6", variable = self.Var[noteindex], onvalue = 1, offvalue = 0, bg = "#b6e1f6", activebackground = "#f9d6d6",font = "courier")
            self.CbxList.append(tmpcbx)
            tmpcbx.pack(pady = 1)
            noteindex += 1
        #print(self.CbxList)
    
    def Update(self):
        global cmpbn
        icon = Image.open("CmBtn2.png")
        icon = icon.resize((80, 20), Image.ANTIALIAS)
        cmpbn = ImageTk.PhotoImage(icon)
        UpdBtn = Button(main, image = cmpbn, command = self.UpdateTasks, bg = "#f9d6d6")
        UpdBtn.pack(pady = 5)
    
        
    def UpdateTasks(self):
        #print(self.CbxList[0])
        ctr = 0
        notefile = open("tasks.txt","r")
        notes = notefile.read().splitlines()
        notefile.close()
        delnotes = []
        notefile = open("tasks.txt", "w")
        for i in self.Var:
            if(i.get()==1):
                delnotes.append(self.CbxList[ctr]["text"])
                self.CbxList[ctr].destroy()
                #self.CbxList.pop(ctr)
            ctr += 1
        notes = (list(list(set(notes)-set(delnotes)) + list(set(delnotes)-set(notes))))
            
        for note in notes:
            notefile.write(note + "\n")

        
        #print(notes)
        self.SaveFile(notefile)
        
        self.logstatus("Updated!")
        
        
        

app = todo()
#app.DisplayTitle()

#title = Label(main, text = "ToDo List", bg = "cyan" ).pack(side = TOP)
main.mainloop()
