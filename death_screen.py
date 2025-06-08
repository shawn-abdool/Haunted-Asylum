#Importing tkinter and importing modules of it
from main import *
from main import runningGame
#from main import timeTaken
from tkinter import *
import tkinter
from tkinter.simpledialog import askstring
from csv import DictWriter
from PIL import Image, ImageTk
import subprocess

with open('levels_survived.txt', 'r') as f:
  levels_survived = f.read().strip()

yourScore = f'Levels Survived: {levels_survived}'

#Creating variable for the Tkinter window
window = tkinter.Tk()

#Defining functions for the different buttons
def ExitGame():
  quit()

def SaveScore():
  field_names = ['username', 'levels']    
  username = askstring('Username', 'What is your username?')
  dict = {'username':username, 'levels':levels_survived}
  with open("game_scores.csv", "a", newline = '') as f:
      dictwriter = DictWriter(f, fieldnames=field_names)
      dictwriter.writerow(dict)

def BackToMM():
  #open Main Menu  
  scriptMM = 'main_menu.py'
  window.destroy()
  subprocess.run(['python', scriptMM])

window.title("YOU DIED")
window.geometry("600x420")

#Creating variables for window
myimage = Image.open("bg_dark.png")
resized_image = myimage.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
bg = ImageTk.PhotoImage(resized_image)

#Creating Labels and Buttons
bglabel = tkinter.Label(window, image=bg, borderwidth=0, highlightthickness=0)
GOTitle=tkinter.Label(window, text = "GAME OVER", fg="red", bg="black", font=("Cooper Black", 110))
displayTime=tkinter.Label(window, text = yourScore, fg="white", bg="black", font=("Arial", 30))
MMButton=tkinter.Button(window, text = "Back to Main Menu",font = 12, width = 60, height = 5, command = BackToMM)
SSButton=tkinter.Button(window, text = "Save Score",font = 12, width = 60, height = 5, command = SaveScore)
EGButton=tkinter.Button(window, text = "Exit Game",font = 12, width = 60, height = 5, command = ExitGame)

#Packing the objects
GOTitle.place(x = 990, y = 10)
displayTime.place(x = 1262, y = 300)
MMButton.place(x = 1202, y =500)
SSButton.place(x = 1202, y = 700)
EGButton.place(x = 1202, y = 900)
bglabel.place(x=0,y=0)

window.attributes('-fullscreen',True)
window.mainloop()