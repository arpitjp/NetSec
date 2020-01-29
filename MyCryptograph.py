from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import tkinter.scrolledtext as scrolledtext
import pyperclip

root = Tk()
root.geometry("1200x6000")
#root["bg"] = "black"
root.title("A-Z Message Encryptor - Arpit Jain")

star = StringVar()
star1 = StringVar()
# frames
Tops = Frame(root, relief=FLAT)
Tops.pack(side=TOP, pady = 10)

fbutton = Frame(root)
fbutton.pack(side = TOP, pady = 10, padx = 20)

ftext = Frame(root)
ftext.pack(pady = 5, expand = 1)

# title
lblInfo = Label(Tops, font=('helvetica', 50, 'bold'), text="Cryptograph", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

# Reset function
def Reset():
    textBox1.delete("1.0", END)
# Reset button
btnReset = Button(fbutton, fg="white", font=('arial', 16, 'bold'), width=5, text="Reset", bg="blue", command=Reset, padx = 50).grid(row=1, column=1, padx = 10)

""""
# Exit function
def qExit():
    root.destroy()
# Exit button
btnExit = Button(fbutton, fg="white", font=('arial', 16, 'bold'), width=5, text="Exit", bg="red", command=qExit, padx = 50).grid(row=1, column=2, padx = 10)
"""
# Copy text to clipboard button
def copy_to_clipboard():
    #root.clipboard_clear()
    garb = star.get()
    pyperclip.copy(garb)
    pyperclip.paste()
# copy button
btnCopyToClipboard = Button(fbutton, fg="white", font=('arial', 16, 'bold'), width=5, text="Copy", bg="purple", command=lambda: copy_to_clipboard(), padx = 50).grid(row=1, column=2, padx = 10)


# Open file function
def open_file():
    file = askopenfile(mode='r', filetypes=[('All Files', '*')])
    if file is not None:
        content = file.read()
        file.close()
        textBox1.insert(INSERT, content)
# Open text file button
btnOpenFile = Button(fbutton, fg="white", font=('arial', 16, 'bold'), width=5, text="Open file", bg="green", command=open_file, padx = 50).grid(row=1, column=0, padx = 10)

# Save file function
def save():
    name = asksaveasfile(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("Word files", ".doc"), ("All files", "*")], initialdir="dir", title="Save as")
    with open(name.name, "w") as data:
        data.write(star.get())
# SAve file button
btnSaveFile = Button(fbutton, fg="white", font=('arial', 16, 'bold'), width=5, text="Save as", bg="orange", command=lambda: save(), padx = 50).grid(row=1, column=3, padx = 10)

# label
lbl1 = Label(ftext, font=('arial', 16, 'bold'), text="Input here", bd=16, anchor="w")
lbl1.grid(row=0, column=0)

lbl2 = Label(ftext, font=('arial', 16, 'bold'), text="Output here", bd=16, anchor="w")
lbl2.grid(row=0, column=1)


# text boxes
textBox1=Text(ftext, height=18, width=50, bg = "powder blue", font=('arial', 16, 'bold'))
textBox1.grid(row=1, column=0, padx=20)

textBox2=Text(ftext, height=18, width=50, bg = "powder blue", font=('arial', 16, 'bold'))
textBox2.grid(row=1, column=1, padx = 20)

# encryption logic
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",range(52)))
I2L = dict(zip(range(52),"ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"))

# encryption function
def Ref(esult=None):
    clear = textBox1.get("1.0",END)
    if clear != star1.get():
        esult = ""
        for c in clear:
            if c.isalpha(): esult += I2L[ (L2I[c]) ] ##If condition is whether c is alphabet or not
            else: esult += c
        textBox2.config(state = NORMAL)
        textBox2.delete("1.0", END)
        textBox2.insert(INSERT,esult)
        textBox2.config(state = DISABLED)
        star1.set(clear)
        star.set(esult)
    textBox1.after(100,Ref)

# keeps window alive
Ref()
root.mainloop()

