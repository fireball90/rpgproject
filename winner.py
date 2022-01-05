import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label):

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('images/winneranimated.gif')

goplayBTN=tk.PhotoImage(file="images/buttonbg.gif")

playAgain = tk.Button(root,image=goplayBTN ,bg="black", border=0, command=root.destroy)
playAgain.place(x=100,y=460)

exitBTN = tk.Button(root,image=goplayBTN,  bg="black", border=0,command=root.destroy)
exitBTN.place(x=350,y=460)

exitTxt= tk.Label(root, text="Exit", bg="gold", fg="black", font=("Arial",12))
exitTxt.place(x=395,y=465)

tryAgainTxt= tk.Label(root, text="Play again", bg="gold", fg="black", font=("Arial",12))
tryAgainTxt.place(x=115,y=465)

thanksLabel=tk.Label(root,text="Thank you for playing our game!", bg="green", fg="yellow",font=("Arial",12))
thanksLabel.place(x=180,y=520)

copyrightLabel=tk.Label(root,text="Credits: Jancsurák Bence, Mészáros Balázs és Lekner Norbert", bg="green", fg="yellow",font=("Arial",12))
copyrightLabel.place(x=80,y=550)

root.mainloop()
import base_v2