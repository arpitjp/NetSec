from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import pyperclip

root = Tk()
root.geometry("1366x768")
root.title("A-Z Message Encryptor - Arpit Jain")

photoclose = PhotoImage(file = r"/home/arpitjp/PycharmProjects/assignment1/close.png")
photoclose = photoclose.subsample(16, 16)
photocopy = PhotoImage(file = r"/home/arpitjp/PycharmProjects/assignment1/copy.png")
photocopy = photocopy.subsample(16, 16)

#COMBOBOX STYLE   [applies to all comboboxes]
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'none',
                                       'fieldbackground': 'white',
                                       'background': 'grey',
                                       'selectforeground': 'black'
                                       }}}
                        )
combostyle.theme_use('combostyle')

#VARIABLES
star = StringVar(root)
r = 0
rowcounter = 0
fieldboxes = list()
fieldlabels = list()
output = list()

#FRAMES
ftitle = Frame(root)
ftitle.pack()

fpara = Frame(root)
fpara.pack(pady = 10)

fcontent = Frame(root)
fcontent.pack(pady = 25)

fleft = Frame(fcontent)
fleft.pack(side = LEFT, padx = 50, expand = YES, fill = Y)
fleft1 = Frame(fleft)
fleft1.grid(row = 0, column = 0, pady=10)
fleft2 = Frame(fleft)
fleft2.grid(row = 1, column = 0, pady = 10)


fright = Frame(fcontent)
fright.pack(side = LEFT, padx = 50, fill = BOTH)

#FUNCTIONS
def makeKeys():
    showkeys = Text(fright, height=50, width=82, font=('arial', 10), wrap=WORD, borderwidth=0, bd=0,
                        highlightthickness=0)
    showkeys.grid(column=0, row=1,columnspan = 3, pady = 20)

def updatelabel():#updates label after removal
    global r
    for i in range(0, r):
        fieldlabels[i].config(text=str(i+1))

def copy_to_clipboard():#copy function
    garb = star.get()
    pyperclip.copy(garb)
    pyperclip.paste()

def decrement():#take care of list removal parameter
    global r
    r = r-1

def process(text):#encryption logic
    ftext = text
    return ftext

def make(text, state=0):#spawns text boxes
    global r, rowcounter
    ftext = process(text)
    output.append(ftext)
    ####################
    lb = Label(fleft2, text= str(r+1) , font=('arial', 13, "bold"), anchor="w")
    lb.grid(column = 0, row = rowcounter)
    fieldlabels.append(lb)
    ######################
    textBox1 = Text(fleft2, height=3, width=51, font=('arial', 10), wrap=WORD,borderwidth =0, bd=0, highlightthickness = 0)
    textBox1.grid(column =1, row= rowcounter, padx = 5, columnspan = 2)
    textBox1.tag_config('warning', background="white", foreground="black")
    fieldboxes.append(textBox1)
    #########
    btn = Button(fleft2, borderwidth =0, bd=0, highlightthickness = 0, image = photoclose,
                 command=lambda: [textBox1.destroy(),btn.destroy(), btn1.destroy(),lb.destroy(), fieldlabels.remove(lb), fieldboxes.remove(textBox1), decrement(), updatelabel(), output.remove(ftext)])
    btn.grid(column = 3, row=rowcounter, padx = 5)
    #######
    btn1 = Button(fleft2, borderwidth=0, bd=0, highlightthickness = 0, image=photocopy)
    btn1.grid(column=4, row=rowcounter)
    ############
    r = r+1
    rowcounter = rowcounter + 1
    textBox1.insert(INSERT, "Input: " + text + "\n" + "Output: " + ftext, 'warning')
    textBox1.config(state=DISABLED)

def show():#debugging
    for i in fieldboxes:
        print(i.get("1.0", END))

#MAIN CANVAS   MAIN CANVAS MAIN CANVAS   MAIN CANVAS   MAIN CANVAS   MAIN CANVAS   MAIN CANVAS
lbltitle = Label(ftitle, font=('arial', 22, 'bold'), text="PA1 - DES", fg="Black")
lbltitle.grid(row=0, column=0, pady = 20)

#hyperparameters comboboxes
labelRound = Label(fpara, text="Round", font=('arial', 14), anchor="w")
labelRound.grid(column=0, row=0)
comboRound = ttk.Combobox(fpara, values=[1, 8, 16, 32], state="readonly", width = 10, justify = 'center')
comboRound.grid(column=1, row=0, padx = 10)
comboRound.current(2)

labelWidth = Label(fpara, text="         BlockSize", font=('arial', 14), anchor="w")
labelWidth.grid(column=2, row=0)
comboWidth = ttk.Combobox(fpara, values=[32, 64, 128], state="readonly", width = 10, justify = 'center')
comboWidth.grid(column=3, row=0, padx = 10)
comboWidth.current(1)

lbkey1 = Label(fpara, text="         Key1", font=('arial', 14), anchor="w")
lbkey1.grid(row=0, column=4, padx = 5)
key1 = Entry(fpara, width = 17)
key1.grid(row=0, column=5, padx = 5)

lbkey2 = Label(fpara, text="         Key2", font=('arial', 14), anchor="w")
lbkey2.grid(row=0, column=6, padx = 5)
key2 = Entry(fpara, width = 17)
key2.grid(row=0, column=7, padx = 5)

lbinp1 = Label(fpara, text="         Inp 1", font=('arial', 14), anchor="w")
lbinp1.grid(row=0, column=8, padx = 5)
eninp1 = Entry(fpara, width = 10)
eninp1.grid(row=0, column=9, padx = 5)

lbinp2 = Label(fpara, text="         Inp 2", font=('arial', 14), anchor="w")
lbinp2.grid(row=0, column=10, padx = 5)
eninp2 = Entry(fpara, width = 10)
eninp2.grid(row=0, column=11, padx = 5)

###############################LEFT PART
#lbinsert = Label(fleft1, text="Input Here", font=('arial', 15), anchor="w")
#lbinsert.grid(row=0, column=0, columnspan = 2)
textBoxentry = Text(fleft1, height=5, width=70, font=('arial', 10), wrap=WORD,borderwidth =0, bd=0, highlightthickness = 0)
textBoxentry.grid(column =0, row= 1, columnspan = 2)

btn = Button(fleft1, fg="white", width = 10, font=('arial', 14), text="Encrypt", bg="grey", command = lambda: [make(textBoxentry.get("1.0",END), 0), textBoxentry.delete("1.0", END)])
btn.grid(row = 2, column = 0)

btn1 = Button(fleft1, fg="white", width = 10, font=('arial', 14), text="Decrypt", bg="grey", command = lambda: [make(textBoxentry.get("1.0",END), 1), textBoxentry.delete("1.0", END)])
btn1.grid(row= 2, column = 1)

#right part
btn = Button(fright, fg="white",height = 2, width = 15, font=('arial', 14), text="Show Round Keys", bg="grey", command = lambda: makeKeys())
btn.grid(row = 0, column = 0, padx = 30)

btn1 = Button(fright, fg="white", height = 2, width = 15, font=('arial', 14), text="Avalanche - Text", bg="grey")
btn1.grid(row = 0, column = 1, padx =30)

btn2 = Button(fright, fg="white", height = 2, width = 15, font=('arial', 14), text="Avalanche - Key", bg="grey")
btn2.grid(row = 0, column = 2, padx =30)


root.mainloop()
