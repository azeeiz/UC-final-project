######AVT
from tkinter import *
from tkinter import filedialog, ttk
from tkmacosx import * 
from tkinter.filedialog import *

import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt 
import csv


win = Tk()
win.geometry("700x500")
win.title("Auto-Visualization Tool")

style= ttk.Style()
style.theme_use('clam')

frame= Frame(win)
frame.pack(pady=20)

def openFile():
    filepath = filedialog.askopenfilename()
    if filepath:
        try:
            filepath= r"{}".format(filepath)
            df = pd.read_csv(filepath)
        except ValueError:
            label.config(text="File could not be opened")
        except FileNotFoundError:
            label.config(text="File not found")
    clear_treeview()
    tree["column"] = list(df.columns)
    tree["show"] =  "headings"

    for col in tree["column"]:
        tree.heading(col, text=col)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
            tree.insert("", "end", values=row)

    tree.pack()


def clear_treeview():
    tree.delete(*tree.get_children())

tree = ttk.Treeview(frame)


def graphFile():
    Names = []
    Values = []
    filepath = filedialog.askopenfilename()
    if filepath:
        try:
            filepath= r"{}".format(filepath)
            df = pd.read_csv(filepath)
        except ValueError:
            label.config(text="File could not be opened")
        except FileNotFoundError:
            label.config(text="File not found")
    with open(filepath,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            Names.append(row[0])
            Values.append(int(row[1]))
  
    plt.scatter(Names, Values, color = 'g',s = 100)
    plt.xticks(rotation = 25)
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Your Graph', fontsize = 18)
  
    plt.show()



browse_button = Button(win, text='Browse',command= openFile)
browse_button.pack()

graph_button = Button(win, text='Graph', command= graphFile)
graph_button.pack()

label = Label(win, text='')
label.pack(pady=20)

ext_btn = Button(win, text="Exit", command=win.quit)
ext_btn.pack()


win.mainloop()
