from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

#Creating variable for the Tkinter window
window = tkinter.Tk()
infoGame = "How to play this game:\n\nTo control your player, use W,A,S,D\n\nMove your player towards the key in order to open the door\nOnce you have unlocked the door, move your player into the red square\nThis is how you get into the next level\n\nHOWEVER, there will be an enemy lurking around the game, tracking you down\nGuide yourself around the map and don't get caught!"

#Defining function for when you press the button
def StartGame():
  window.destroy()
  
  subprocess.run(['python', 'main.py'])

def ShowLeaderboard():
  scriptLB = 'displayLeaderboard.py'
  subprocess.run(['python', scriptLB])

def Help():
  tkinter.messagebox.showinfo("Help!", infoGame)

def ExitGame():
  quit()

window.title("Haunted Asylum Game")
window.geometry("600x400")

#Creating variables for window
original_image = Image.open("bg_dark.png")
resized_image = original_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(resized_image)

background_label = tkinter.Label(window, image=background_image, borderwidth=0, highlightthickness=0)
label1=tkinter.Label(window, text = "Haunted Asylum", fg="white", bg = "black", font=("Cooper Black", 110))
buttonStart = tkinter.Button(window, text = "Start Game", font = 12, width = 60, height = 5, command = StartGame)
buttonLB = tkinter.Button(window, text = "Leaderboard", font = 12, width = 60, height = 5, command = ShowLeaderboard)
buttonHelp=tkinter.Button(window, text = "Help", font = 12, width = 60, height = 5, command = Help)
buttonEG=tkinter.Button(window, text = "Exit Game", font = 12, width = 60, height = 5, command = ExitGame)

#Packing the objects
label1.place(x = 870, y = 10)
buttonStart.place(x = 1202, y = 300)
buttonLB.place(x = 1202, y =500)
buttonHelp.place(x = 1202, y = 700)
buttonEG.place(x = 1202, y = 900)
background_label.place(x=0, y=0)

window.attributes('-fullscreen',True)
window.mainloop()