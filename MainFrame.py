import json
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename


class ProgramFrame(tkinter.Frame):
    def __init__(self, the_window):
        super().__init__()

        Frame.__init__(self, the_window)
        self.hashtag = ""
        self.data = []
        self.graphChoiceVar = ""
        self.datatypevardis = ""
        self.datatypevarcon = ""
        self.switch = StringVar()

        # Defining and setting hashtag set up
        self.friendly_label1 = Label(self, text="Enter hashtag")
        self.name_entry = Entry(self)
        self.button = Button(self, text="Click Me", command=self.setHashtag)
        # self.name_label1 = Label(self, text=self.hashtag)
        self.friendly_label1.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry.grid(row=1, column=0, padx=10, pady=10)
        self.button.grid(row=2, column=0, padx=10, pady=10)
        # self.name_label1.grid(row=3, column=0, padx=10, pady=10)

        # Defining what type of graph you want (Continuous or Discreate)
        self.friendly_label2 = Label(self, text="Enter Graph Type")
        Options = [
            "Discrete",
            "Continuous"
        ]
        self.variable = StringVar(self)
        self.variable.set(Options[0])
        self.graphChoice = OptionMenu(self, self.variable, *Options)
        self.variable.set('Discrete')
        self.button2 = Button(self, text="Set Graph Type", command=self.setGraphType)
        # self.name_label2 = Label(self, text=self.graphChoiceVar)
        self.friendly_label2.grid(row=0, column=3, padx=10, pady=10)
        self.graphChoice.grid(row=1, column=3, padx=10, pady=10)
        self.button2.grid(row=2, column=3, padx=10, pady=10)
        # self.name_label2.grid(row=3, column=3, padx=10, pady=10)

        # Defining the different data comparisons the graph would include
        self.friendly_label3 = Label(self, text="Enter Graphical Data - Discrete")
        OptionsGrphDiscrete = [
            "Likes per hashtag",
            "Word Length per hashtag",
            "Hashtagged Images vs Videos",
        ]
        self.vargraph = StringVar(self)
        self.vargraph.set(OptionsGrphDiscrete[0])
        self.datachoicedis = OptionMenu(self, self.vargraph, *OptionsGrphDiscrete)
        self.vargraph.set('Likes per hashtag')
        self.button3 = Button(self, text="Set Discrete Data Type", command=self.setDatatype)
        # self.name_label3 = Label(self, text=self.datatypevardis)
        self.friendly_label3.grid(row=0, column=5, padx=10, pady=10)
        self.datachoicedis.grid(row=1, column=5, padx=10, pady=10)
        self.button3.grid(row=2, column=5, padx=10, pady=10)
        # self.name_label3.grid(row=3, column=5, padx=10, pady=10)

        self.friendly_label4 = Label(self, text="Enter Graphical Data - Continuous")
        OptionsGrphContin = [
            "Hashtag longevity"
        ]
        self.vargraphCon = StringVar(self)
        self.vargraphCon.set(OptionsGrphContin[0])
        self.datachoiceCon = OptionMenu(self, self.vargraphCon, *OptionsGrphContin)
        self.vargraphCon.set('Likes per hashtag')
        self.button4 = Button(self, text="Set Continuous Data Type", command=self.setDatatypeCon)
        # self.name_label4 = Label(self, text=self.datatypevarcon)
        self.friendly_label4.grid(row=0, column=7, padx=10, pady=10)
        self.datachoiceCon.grid(row=1, column=7, padx=10, pady=10)
        self.button4.grid(row=2, column=7, padx=10, pady=10)
        # self.name_label4.grid(row=3, column=7, padx=10, pady=10)

        self.initUI()

        # self.name_label5 = Label(self, text=self.datacheckvar)
        # self.name_label5.grid(row=5, column=5, padx=10, pady=10)

        self.buttonMain = Button(self, text="Clear Data Fields", command=self.ClearVariables)
        self.buttonMain.grid(row=6, column=5, padx=10, pady=10)
        self.buttonMain = Button(self, text="Create Graph", command=self.createGraph)
        self.buttonMain.grid(row=7, column=5, padx=10, pady=10)

        # Defining

    def initUI(self):
        self.master.title("Social Media Graphical Interface: Options Menu")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create file menu
        JsonMenu = Menu(menubar, tearoff=False)
        JsonMenu.add_command(label="Get Json Connection", command=self.getJsonFile)
        menubar.add_cascade(label="JsonConnection", menu=JsonMenu)

    def setHashtag(self):
        self.hashtag = self.name_entry.get()
        print(self.hashtag)

    def getJsonFile(self):
        file = askopenfilename(initialdir="D:\PhyCharm\InstagramProject", filetypes=[("Json File", "*.json")],
                               title="Choose Json File")
        self.data = json.load(open(file))
        print(self.data)
        # self.datacheck()
        return

    def setGraphType(self):
        self.graphChoiceVar = self.variable.get()
        print(self.graphChoiceVar)

    def setDatatype(self):
        self.datatypevardis = self.vargraph.get()
        print(self.datatypevardis)

    def setDatatypeCon(self):
        self.datatypevarcon = self.vargraphCon.get()
        print(self.datatypevarcon)

    def ClearVariables(self):
        self.hashtag = ""
        self.graphChoiceVar = ""
        self.datatypevarcon = ""
        self.datatypevardis = ""
        self.data.clear()

    def LikesPerHashTag(self):
        #captions = self.data['Posts']['Posts caption']['Likes']
        print(self.data['Posts'][2]['Post caption'][2]['Likes'])

    def WordLengthPerHashTag(self):
        print("hit1")

    def ImagesVSVideos(self):
        print("hit2")

    def HashtagLongevity(self):
        print("hit3")

    def invalidEntry(self):
        print("hit4")


    def createGraph(self):
        print("Button works")
        self.switch = (self.graphChoiceVar + self.datatypevardis + self.datatypevarcon)

        #switchcase = {
        #    "DiscreteLikes per hashtag""DiscreteLikes per hashtag": print("1"), #self.LikesPerHashTag,
        #    "DiscreteWord Length per hashtag": print("2"), #self.WordLengthPerHashTag,
        #    "DiscreateHashtagged Images vs Videos": print("3"), #self.ImagesVSVideos,
        #    "ContinuousHashtag longevity": print("4") #self.HashtagLongevity
        #}

        if self.switch == "DiscreteLikes per hashtag":
            self.LikesPerHashTag()
        elif self.switch == "DiscreteWord Length per hashtag":
            self.WordLengthPerHashTag()
        elif self.switch == "DiscreteHashtagged Images vs Videos":
            self.ImagesVSVideos()
        elif self.switch == "ContinuousHashtag longevity":
            self.HashtagLongevity()
        else:
            self.invalidEntry()

    # def datacheck(self):
    #    if self.data is not None:
    #        self.datacheckvar.set("Connection made")
    #        self.update_idletasks()

    #    else:
    #        self.datacheckvar.set("Connection not made")
    #        self.update_idletasks()




def main():
    my_window = Tk()
    frameA = ProgramFrame(my_window)
    frameA.grid(row=0, column=0)
    my_window.mainloop()


if __name__ == '__main__':
    main()
