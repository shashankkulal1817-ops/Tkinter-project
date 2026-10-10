# IMPORT TKINTER FOR CREATING GUI APPS:
import tkinter as tk
from tkinter import filedialog,messagebox

# MAIN WINDOW CODE:
root=tk.Tk()
root.title("simple text editor")
root.geometry("800x600")

# CREATE TEXT AREA:
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("helvetica",18)
)
text.pack(expand=True,fill=tk.BOTH)

# MAIN LOGIC STARTS NOW:
# FUNCTION 1-TO CREATE A NEW FILE:
def newfile():
    text.delete(1.0,tk.END)

# FUNCTION 2-TO OPEN A NEW FILE:
def openfile():
    #open file dialogue:
    filepath=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("text files ","*.txt")]
    )
    if filepath:
        # open selected file:
        with open(filepath,"r")as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

# FUNCTION 3-SAVE THE FILE:
def savefile():
    # open save file dialogue
    filepath=filedialog.asksaveasfilename(
      defaultextension=".txt",
      filetypes=[("text files","*.txt")]
    )            
    if filepath:
        with open(filepath,"w")as file:
            file.write(text.get(1.0,tk.END))
    messagebox.showinfo("info","file saved succesfully")

# CREATE MENU BAR:
menu=tk.Menu(root)
root.config(menu=menu)
filemenu=tk.Menu(menu)

# NEW,OPEN FILE,SAVE,EXIT

# ADD FILEMENU TO MENU BAR:
menu.add_cascade(label="file",menu=filemenu)
filemenu.add_command(label="new",command=newfile)
filemenu.add_command(label="open",command=openfile)
filemenu.add_command(label="save",command=savefile)   
filemenu.add_separator()
filemenu.add_command(label="exit",command=root.quit)   


# STARTS AND KEEPS THE WINDOW OPEN:
root.mainloop()