#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:34:23 2022

@author: riddhiekajain
"""

from tkinter import *
import random
root= Tk()
root.title("encapsulation")
root.geometry("500x400")
root.config(bg="azure")
label_name=Label(root, font=("Arial", 40))
label_name.place(relx=0.5, rely=0.3, anchor= CENTER)
class game:
    def __init__(self):
        self.__score=0
    def update_game(self):
        self.text=["BLACK", "RED", "GREEN", "BLUE", "VIOLET"]
        self.random_numbert=random.randint(0, 4)
        self.color=["black", "red", "green", "blue", "violet"]
        self.random_numberc=random.randint(0, 4)
        label_name["text"]=self.text[self.random_numbert]
        label_name["fg"]=self.color[self.random_numberc]
        
obj=game()
btn=Button(root, text="start", command=obj.update_game)
btn.place(relx=0.65, rely=0.65, anchor=CENTER)
root.mainloop()