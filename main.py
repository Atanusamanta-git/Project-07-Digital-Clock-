#Use Graphis Display
import tkinter as tk
#Use For time module
from time import strftime #strftime mean ma apni time or date ko apni pasand se set kar sakta hoon
# First make root window

root= tk.Tk()
#Set tital mean Clock ka name
root.title("Digital Clock")

#Update time And Display time in Particular label and Place, make function

def time():
    string=strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time) #Isse hamara time func har samay update hoga or label me current time or date dekhayega

#Define label usge for font,size,colour,Bg colour etc..

label=tk.Label(root,font=('Captain', 50, 'bold'),background='black',foreground='red')
#label ko root me pack karenge
label.pack(anchor='center')

time()
root.mainloop()

