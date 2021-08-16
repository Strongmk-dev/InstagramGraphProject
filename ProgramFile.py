# print("Competing in a varsity smash tournament tomorrow. Time to start a montage \uD83D\uDC27") - Note,
# emojis cannot be processed by the program. address in dissertation

from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from collections import Counter
import pandas
import json
import matplotlib.pyplot as plt
import numpy as np


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.friendly_label = Label(self, text="Enter your hashtag")
        self.friendly_label.grid(row=0, column=0)

        hashtag = ""
        data = []

    def initUI(self):
        self.master.title("Simple menu")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create file menu
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Get Json Connection", command=self.getJsonFile)
        menubar.add_cascade(label="File", menu=fileMenu)

        # create first frame for hashtag
        frame1 = Frame(self.master, width=200, height=200, highlightbackground='grey', highlightthickness=3)
        frame1.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=20)

        # create hashtag entry within frame 1


    def onExit(self):
        self.quit()

    def setHashtag(self, text):
        self.hashtag = text;
        print(self.hashtag)

    def getJsonFile(self):
        file = askopenfilename(initialdir="D:\PhyCharm\InstagramProject", filetypes=[("Json File", "*.json")],
                               title="Choose Json File")
        self.data = json.load(open(file))
        print(self.data)
        return


# def get_hashtag():
#    global Hashtag
#    #Hashtag = answer_entry.get()
#    return


# def getJsonCall():
#    file = askopenfilename(initialdir="D:\PhyCharm\InstagramProject", filetypes=[("Json File", "*.json")],
#                           title="Choose Json File")
#    global JsonData
#    JsonData = json.load(open(file))
#    return

def MakeFrame1():
    return


def MakeFrame2():
    return


def main():
    root = tk.Tk()
    root.title("OptionMenu")
    root.geometry('500x500')
    frame1 = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
