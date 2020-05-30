from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import tkinter.scrolledtext as scrolledtext
import pyperclip

########################################################################################################################
# SECTION 1
########################################################################################################################
root = Tk()
root.geometry("1200x6000")
#root["bg"] = "black"
root.title("A-Z Message Encryptor - Arpit Jain")

# variables, StringVar
star = StringVar()
star1 = StringVar()

# main window scrollbar
class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError("cannot use pack with this widget")
    def place(self, **kw):
        raise TclError("cannot use place with this widget")

vscrollbar = AutoScrollbar(root)
vscrollbar.grid(row=0, column=1, sticky=N+S)
hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)

canvas = Canvas(root, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)

vscrollbar.config(command=canvas.yview)
hscrollbar.config(command=canvas.xview)

# make the canvas expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = Frame(canvas)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(1, weight=1)

# frames
Tops = Frame(frame, relief=FLAT)
Tops.pack(side=TOP, pady = 10)

fbutton = Frame(frame)
fbutton.pack(side = TOP, pady = 10, padx = 20)

ftext = Frame(frame)
ftext.pack(pady = 5, expand = 1)

# title
lblInfo = Label(Tops, font=('helvetica', 50, 'bold'), text="Cryptograph", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

########################################################################################################################
# SECTION 2
########################################################################################################################

## FUNCTIONS MAPPING TO BUTTONS
# Reset function
def Reset():
    textBox1.delete("1.0", END)

# Reset button
btnReset = Button(fbutton, fg="white", font=('arial', 16, 'bold'), width=5, text="Reset", bg="blue", command=Reset, padx = 50).grid(row=1, column=1, padx = 10)

# Copy text to clipboard button
def copy_to_clipboard():
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

# Save file button
btnSaveFile = Button(fbutton, fg="white", font=('arial', 16, 'bold'), width=5, text="Save as", bg="orange", command=lambda: save(), padx = 50).grid(row=1, column=3, padx = 10)

# label
lbl1 = Label(ftext, font=('arial', 18, 'bold'), text="Input here", bd=16, anchor="w")
lbl1.grid(row=0, column=0)

lbl2 = Label(ftext, font=('arial', 18, 'bold'), text="Output here", bd=16, anchor="w")
lbl2.grid(row=0, column=1)

# text boxes with horizontal scrollbar
xscrollbar1 = Scrollbar(ftext, orient=HORIZONTAL)
xscrollbar1.grid(row=2, column=0, sticky=N+S+E+W, padx = 20)
textBox1=Text(ftext, height=18, width=51, bg = "powder blue", font=('arial', 16, 'bold'), wrap = NONE, xscrollcommand = xscrollbar1.set)
textBox1.grid(row=1, column=0, padx=20)
xscrollbar1.config(command=textBox1.xview)

xscrollbar2 = Scrollbar(ftext, orient=HORIZONTAL)
xscrollbar2.grid(row=2, column=1, sticky=N+S+E+W, padx = 20)
textBox2=Text(ftext, height=18, width=51, bg = "powder blue", font=('arial', 16, 'bold'), wrap = NONE, xscrollcommand = xscrollbar2.set)
textBox2.grid(row=1, column=1, padx = 20)
xscrollbar2.config(command=textBox2.xview)

########################################################################################################################
# SECTION 3
########################################################################################################################

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
        esult = esult.rstrip()
        textBox2.config(state = NORMAL)
        textBox2.delete("1.0", END)
        textBox2.insert(INSERT,esult)
        textBox2.config(state = DISABLED)
        star1.set(clear)
        star.set(esult)
    textBox1.after(100,Ref)


# main window scrollbar
canvas.create_window(0, 0, anchor=NW, window=frame)
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# keeps window alive
Ref()
root.mainloop()
