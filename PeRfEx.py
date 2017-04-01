#!/usr/bin/python3

import time
from time import gmtime, strftime
import sys
import re
from tkinter import * 

def redirector(outputStr=""):
	T = Text(windows, width=60, height=10, bg='black', font=("System", 15), fg="white")
	sys.stdout = StdoutRedirector(T)
	T.pack(side=TOP,padx=5, pady=5)
	T.insert(END, outputStr)

class IORedirector(object):
	'''A general class for redirecting I/O to this Text widget.'''
	def __init__(self,text_area):
		self.text_area = text_area

class StdoutRedirector(IORedirector):
	'''A class for redirecting stdout to this Text widget.'''
	def write(self,str):
		self.text_area.insert("end", str)

def getPerformances():
	inputstr = inputlog.get()
	inputrgx = inputregex.get()
	
	start = time.time()
	for i in range(1000000):
		re.search(inputrgx, inputstr)
	end = time.time()
	result = int((end-start)*1000)
	if re.search(inputrgx, inputstr):
		print(strftime("%Y-%m-%d %H:%M:%S", gmtime())+" -- ReGex Matched | Time Elapsed: "+str(result)+" (ms) ")
	else:
		print(strftime("%Y-%m-%d %H:%M:%S", gmtime())+" -- ReGex Not Matched | Time Elapsed: "+str(result)+" (ms) ")

# Create a GUI
windows = Tk()
windows.wm_title("PeRfEx")
windows['bg']='black'

input1 = StringVar()
input2 = StringVar()

# Title
title = Label(windows, text="- - - - - - - - \nP e R f E x \n- - - - - - - - ", font=("System", 30), fg="white", bg='black')
title.pack(side=TOP,padx=40, pady=20)

# Text Log
txtlog = Label(windows, text="Log", font=("System", 20), fg='white', bg='black')
txtlog.pack(side=TOP,padx=40, pady=20)

# Log Input
inputlog = Entry(windows, textvariable=input2, width=50, font=("System", 15), bg='white')
inputlog.pack(side=TOP, padx=50)

# Text Regex
txtrgx = Label(windows, text="ReGex", font=("System", 20), fg='white' ,bg='black')
txtrgx.pack(side=TOP, padx=40, pady=20)

# Regex Input
inputregex = Entry(windows, textvariable=input1, width=50, font=("System", 15), bg='white')
inputregex.pack(side=TOP, padx=40)

# Launch the calculation with the previous inputs
bouton = Button(windows, text="Go", command=getPerformances, font=("System", 15), fg="white", bg='black')
bouton.pack(side=TOP, padx=40, pady=20)

r = redirector()
windows.mainloop()