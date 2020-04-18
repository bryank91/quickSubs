import tkinter
from tkinter import messagebox
from sbox import tk_get_file_path

# used for testing
from time import sleep

top = tkinter.Tk()
label = tkinter.Label(top, text = "Waiting for task to be finished")

def specifyDirectory():
	# display file system here. reuses the function from outside
	tk_get_file_path()
	
	# message box if required
	# messagebox.showinfo("Hello Python", "Hello World");

	# shows a spinner to indicate its loading
	label.pack()

	# once load finishes, spinner disappears 

button = tkinter.Button(top, text = "Import Subtitles", command=specifyDirectory)

button.pack()
top.mainloop()
