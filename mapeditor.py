from tkinter import *
from tkinter import filedialog
from tkinter import font

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="/level", 
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
root.geometry("400x700")
root.resizable(False, False)
root['bg']='#333333'

topFrame = PanedWindow(root, background="#111111", height=200, width=400)
middleFrame = PanedWindow(root, background="#777777", height=400,width=400)
bottomFrame = PanedWindow(root, background="#333333", height=100,width=400)

topFrame.grid(row=0, column=0, sticky="ew")
middleFrame.grid(row=1, column=0, sticky="nsew")
bottomFrame.grid(row=2, column=0, sticky="nsew")


howToDoIt = Label(topFrame, text="These are the instructions to create a map: ", bg="#111111", fg="red", font=('Arial', 12))
outerwallPlacement = Label(topFrame, text="Press \"#\"  to place outside walls.", bg="#111111", fg="yellow")
insidewallPlacement = Label(topFrame, text="Press \"=\"   to place inside walls.", bg="#111111", fg="yellow")
groundPlacement = Label(topFrame, text="Press \".\"   to place empty field.", bg="#111111", fg="yellow")
playerPlacement = Label(topFrame, text="Press \"p\"   to place the player.", bg="#111111", fg="yellow")
enemyPlacement = Label(topFrame, text="Press \"1,2,3,4\" to place different enemy types.", bg="#111111", fg="yellow")

howToDoIt.place(x=50,y=10)
outerwallPlacement.place(x=50,y=40)
insidewallPlacement.place(x=50,y=60)
groundPlacement.place(x=50,y=80)
playerPlacement.place(x=50,y=100)
enemyPlacement.place(x=50,y=120)

mapFrame = Frame(middleFrame)
mapFrame.pack(pady=20)

mapText = Text(mapFrame, width=24, height=24)
mapText.pack(side=LEFT)

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