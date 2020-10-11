from tkinter import *
import datetime

with open("students.txt","r", encoding="utf-8") as students:
    student = students.read().split("\n")

def add():
    myStudent = clicked.get()
    date = datetime.datetime.now()
    date_2 = date.strftime('%d %B %Y')
    file_name = date_2 + " students which is in class.txt"
    with open(file_name,"a") as file:
        file.write(myStudent + "\n")

def execute():
    root = Tk()
    root.title("Which Student is in class?")
    root.geometry("400x200")
    root.tk_setPalette("#F5F5DC")
    return root

root = execute()

clicked = StringVar()
drop = OptionMenu(root, clicked, *student)
drop.pack(padx=25,pady=25)
myButton = Button(root,command=add,text="Add")
myButton.pack(padx=180)
myLabel = Label(root, text="Copyright - Ozan",fg="black",padx=5,pady=100)
myLabel.pack(side=RIGHT)

root.mainloop()

