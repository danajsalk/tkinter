"""
First it creates a frame, selected color top navigation bar you saw on the
Window. It takes some arguments, only the first one  is mandatory. That is the
self.master. The first one is mandatory because the Frame() class needs to know
in which part of the Window it should be placed. Other arguments are self
explanatory. the bg is the background color variable and usesa hex value. You
can use a color picker to get the hex value of any color.
(COLOR PICKER ~Chrome Extension)

Why a class?
Classes are the pillar of Object Oriented Programming. OOP is highly concerned
with code organization, re-usability, and encapsulation.
"""

from tkinter import *

from datetime import datetime, timedelta
import json
import pandas as pd
import requests
import time
import urllib

__author__ = "Dana Koczur"
__version__ = "1.0"
__date__ = "01/30/2019"

# Variables
###############################################################################
bcolor = "#00D4FF"#"#58C13E"#0EF17C"

#############################################################################
# Inside a class functions are called methods
class Window(object):

    def __init__(self, master):
        self.master = master
        # sets the title
        self.master.title("Run Script GUI")
        # sets the dimentions and position of window
        self.master.geometry('400x400+650+300')
        self.master.config(bg="#fff")

        # set the resizable option to false
        self.master.resizable(0, 0)

        # call the widget function to create widgets
        self.AddWidgets()


    def AddWidgets(self):
        # Grid Manager to Position
        self.TopFrame = Frame(self.master, bg=bcolor, width=400, height=75)
        self.TopFrame.grid(column=0, row=1, ipadx=10, ipady=10)

        self.TextLabel = Label(self.master, text="Welcome!", font="Laksaman",
                               fg="#333", bg="#fff")
        self.TextLabel.grid(column=0, row=2, padx=10, pady=0)

        self.SayHello = Button(self.master, text="Hello Run",
                               width=10, height=2, bd=0, bg=bcolor,
                               activebackground="#fff",
                               activeforeground=bcolor,
                               fg="#fff", command=self.ShowHelloBox)
        self.SayHello.grid(column=0, row=4, padx=10, pady=10)

        self.RunScript = Button(self.master, text="Run Script", width=10,
                                height=2, bd=0, bg=bcolor,
                                activebackground="#fff",
                               activeforeground=bcolor,
                               fg="#fff", command=self.run_script)
        self.RunScript.grid(column=0, row=5, padx=10, pady=10)

        self.SayExit = Button(self.master, text="Exit", width=10, height=2,
                              bd=0, bg=bcolor, activebackground="#fff",
                              activeforeground=bcolor,
                               fg="#fff", command=self._quit)
        self.SayExit.grid(column=0, row=6, padx=10, pady=10)

        # Grid Manager to Position
        self.BottomFrame = Frame(self.master, bg=bcolor, width=400, height=90)
        self.BottomFrame.grid(column=0, row=8, ipadx=10, ipady=10)

    def ShowHelloBox(self):
        self.TextLabel.config(text="Hello!")

    # Creating a Menu Bar
    # Exit GUI cleanly
    def _quit(self):
        self.master.quit()
        self.master.destroy()

    def run_script(self):
        def main():

            print("YEAH!!!")

        self.TextLabel.config(text="Run Completed!")

        if __name__ == '__main__':
            main()

        # Defined functions for transformations and data


app = Tk()
Window = Window(app)

app.mainloop()


