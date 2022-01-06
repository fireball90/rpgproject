from os import waitstatus_to_exitcode
from tkinter import *
from tkinter import filedialog
from tkinter import font

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="/maps", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    mapPath.insert(END, tf)
    tf = open(tf)
    file_cont = tf.read()
    mapText.insert(END, file_cont)
    tf.close()

def saveFile():
    tf = filedialog.asksaveasfile(
        mode='w',
        title ="Save file",
        defaultextension=".txt"
        )
    tf.config(mode='w')
    mapPath.insert(END, tf)
    data = str(mapText.get(1.0, END))
    tf.write(data)
    tf.close()

root = Tk()
root.title("Map editor")
root.geometry("800x950")
root.resizable(False, False)
root['bg']='#333333'

topFrame = PanedWindow(root, background="#111111", height=50, width=800)
middleFrame = PanedWindow(root, background="#777777", height=800,width=800)
bottomFrame = PanedWindow(root, background="#333333", height=100,width=800)

topFrame.grid(row=0, column=0, sticky="ew")
middleFrame.grid(row=1, column=0, sticky="nsew")
bottomFrame.grid(row=2, column=0, sticky="nsew")

mapTextFrame = Frame(middleFrame, background="#666666",  width=400)
howToFrame = Frame(middleFrame, background="#111111",  width=400)

middleFrame.add(mapTextFrame)
middleFrame.add(howToFrame)

editorPlease=Label(topFrame, text="Map editor", bg="#111111", fg="red", font=('Arial', 30))
howToDoIt = Label(howToFrame, text="These are the instructions to create a map: ", bg="#111111", fg="red", font=('Arial', 12))
grassPlacement = Label(howToFrame, text="Press \" . \"  to place grass.", bg="#111111", fg="yellow", font=('Arial', 11))
sandPlacement = Label(howToFrame, text="Press \" : \"   to place sand.", bg="#111111", fg="yellow", font=('Arial', 11))
snowPlacement = Label(howToFrame, text="Press \" ; \"   to place snow.", bg="#111111", fg="yellow", font=('Arial', 11))
redSidePlacement = Label(howToFrame, text="Press \" ( \"   to place red sidewalls.", bg="#111111", fg="yellow", font=('Arial', 11))
woodSidePlacement = Label(howToFrame, text="Press \" { \" to place wooden sidewalls.", bg="#111111", fg="yellow", font=('Arial', 11))
stoneSidePlacement = Label(howToFrame, text="Press \" [ \"   to place stone sidewalls.", bg="#111111", fg="yellow", font=('Arial', 11))
redRoofPlacement = Label(howToFrame, text="Press \" - \"   to place red roofs.", bg="#111111", fg="yellow", font=('Arial', 11))
stoneRoofPlacement = Label(howToFrame, text="Press \" = \"   to place stone roofs.", bg="#111111", fg="yellow", font=('Arial', 11))
woodRoofPlacement = Label(howToFrame, text="Press \" _ \"   to place wooden roofs.", bg="#111111", fg="yellow", font=('Arial', 11))
normalTreePlacement = Label(howToFrame, text="Press \" ! \"   to place normal trees.", bg="#111111", fg="yellow", font=('Arial', 11))
palmTreePlacement = Label(howToFrame, text="Press \" | \"   to place palm trees.", bg="#111111", fg="yellow", font=('Arial', 11))
evergreenTreePlacement = Label(howToFrame, text="Press \" / \"   to place evergreen trees.", bg="#111111", fg="yellow", font=('Arial', 11))
howMuchPlacement = Label(howToFrame, text="The top 24 characters are for BACKGROUND ONLY! (24x24 characters)", bg="#111111", fg="red")

editorPlease.place(x=320,y=0)
howToDoIt.place(x=50,y=10)
grassPlacement.place(x=50,y=40)
sandPlacement.place(x=50,y=60)
snowPlacement.place(x=50,y=80)
redSidePlacement.place(x=50,y=100)
woodSidePlacement.place(x=50,y=120)
stoneSidePlacement.place(x=50,y=140)
redRoofPlacement.place(x=50,y=160)
woodRoofPlacement.place(x=50,y=180)
stoneRoofPlacement.place(x=50,y=200)
normalTreePlacement.place(x=50,y=220)
palmTreePlacement.place(x=50,y=240)
evergreenTreePlacement.place(x=50,y=260)
howMuchPlacement.place(x=10,y=280)

enemyOnePlacement = Label(howToFrame, text="Press \" 1 \"  to place enemy (type 1).", bg="#111111", fg="green", font=('Arial', 11))
enemyTwoPlacement = Label(howToFrame, text="Press \" 2 \"  to place enemy (type 2).", bg="#111111", fg="green", font=('Arial', 11))
enemyThreePlacement = Label(howToFrame, text="Press \" 3 \"  to place enemy (type 3).", bg="#111111", fg="green", font=('Arial', 11))
enemyFourPlacement = Label(howToFrame, text="Press \" 4 \"  to place enemy (type 4).", bg="#111111", fg="green", font=('Arial', 11))
playerPlacement = Label(howToFrame, text="Press \" p \"  to place the player.", bg="#111111", fg="green", font=('Arial', 11))
firePlacement = Label(howToFrame, text="Press \" f \"  to place fire.", bg="#111111", fg="green", font=('Arial', 11))
chestPlacement = Label(howToFrame, text="Press \" c \"  to place a chest.", bg="#111111", fg="green", font=('Arial', 11))
bandagePlacement = Label(howToFrame, text="Press \" b \"  to place a bandage.", bg="#111111", fg="green", font=('Arial', 11))
starPlacement = Label(howToFrame, text="Press \" s \"  to place star.", bg="#111111", fg="green", font=('Arial', 11))
fieldPlacement = Label(howToFrame, text="Press \" * \"  to place an empty field.", bg="#111111", fg="green", font=('Arial', 11))
howMuchTwoPlacement = Label(howToFrame, text="These characters are for FOREGROUND ONLY! (24x24 characters)", bg="#111111", fg="red")

enemyOnePlacement.place(x=50,y=320)
enemyTwoPlacement.place(x=50,y=340)
enemyThreePlacement.place(x=50,y=360)
enemyFourPlacement.place(x=50,y=380)
playerPlacement.place(x=50,y=400)
firePlacement.place(x=50,y=420)
chestPlacement.place(x=50,y=440)
bandagePlacement.place(x=50,y=460)
starPlacement.place(x=50,y=480)
fieldPlacement.place(x=50,y=500)
howMuchTwoPlacement.place(x=10,y=520)

workOrder1 = Label(howToFrame, text="You have to put 24x24 sprite in the background", bg="#111111", fg="white", font=('Arial', 12))
workOrder2 = Label(howToFrame, text="After you reach the 25th line you have to start ", bg="#111111", fg="white", font=('Arial', 12))
workOrder3 = Label(howToFrame, text="Placing the player and the enemies. ", bg="#111111", fg="white", font=('Arial', 12))
workOrder4 = Label(howToFrame, text="Be careful not to place an entity into a wall!", bg="#111111", fg="white", font=('Arial', 12))
workOrder5 = Label(howToFrame, text="You have to use \" * \" empty fields between ", bg="#111111", fg="white", font=('Arial', 12))
workOrder6 = Label(howToFrame, text="the placed entities!! Otherwise it wont work! ", bg="#111111", fg="white", font=('Arial', 12))
workOrder7 = Label(howToFrame, text="Look at the sample on the textfield!!!", bg="#111111", fg="orange", font=('Arial', 16))

workOrder1.place(x=10,y=560)
workOrder2.place(x=10,y=585)
workOrder3.place(x=10,y=610)
workOrder4.place(x=10,y=635)
workOrder5.place(x=10,y=660)
workOrder6.place(x=10,y=685)
workOrder7.place(x=10,y=720)

mapFrame = Frame(mapTextFrame, width=400)
mapFrame.pack(pady=5,padx=100)

mapText = Text(mapFrame, width=24, height=48)
mapText.pack(side=LEFT)
mapz = open("maps/first_level.txt")
file_please = mapz.read()
mapText.insert(END, file_please)


mapPath = Entry(bottomFrame)
mapPath.pack(expand=True, fill=X, padx=10,pady=5)

Button(
    bottomFrame, 
    text="Open File", 
    command=openFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    bottomFrame, 
    text="Save File", 
    command=saveFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    bottomFrame, 
    text="Exit", 
    command=lambda:root.destroy()
    ).pack(side=LEFT, expand=True, fill=X, padx=20, pady=5)

root.mainloop()