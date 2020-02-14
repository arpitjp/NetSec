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
######
n, bs, subkey1, subkey2, eord, subkeylist, plaintext, ciphertextlist, padstate = 16, 64, "", "", 0, list(), "", list(), 0



import math
shift_table = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)

IPtable32 =[18,27,14,5,10,26,16,24,
    	2,15,31,17,30,19,8,9,
    	25,20,28,3,22,29,4,32,
    	12,13,21,23,6,11,7,1]

IIPtable32 = [0]*32
for i in range(0, 32):
    IIPtable32[IPtable32[i]-1]=i+1

IPtable128=[10,77,84,21,106,42,18,89,
    	66,7,94,48,82,81,78,28,
    	123,54,56,103,102,41,100,125,
    	74,12,24,122,46,109,126,15,
    	112,105,26,75,58,35,120,53,
    	34,108,40,107,96,110,98,95,
    	118,92,117,83,2,115,111,59,
    	90,19,127,99,79,71,69,61,
    	128,93,44,101,6,91,87,63,
    	116,1,114,47,22,68,124,73,
    	70,80,72,57,88,86,104,55,
    	121,9,76,17,30,45,51,50,
    	64,13,60,62,14,49,52,27,
    	65,33,23,25,36,38,43,119,
    	32,20,113,39,97,85,29,3,
    	67,37,16,11,8,31,4,5]

IIPtable128 = [0]*128
for i in range(0, 128):
    IIPtable128[IPtable128[i]-1]=i+1

EPtable32 = [5,12,7,13,9,2,14,6,16,10,3,11,1,15,4,8,10,5,15,3,6,1,2,9]
EPtable128 =[46,1,18,56,22,62,48,64,60,34,61,32,2,22,12,58,1,26,42,52,16,50,57,62,56,64,29,30,7,55,23,40,25,63,37,20,24,48,59,18,31,37,28,34,57,40,61,36,52,42,20,55,26,15,50,10,47,7,8,53,41,51,6,4,14,59,35,19,30,63,58,54,25,44,33,27,2,38,49,45,32,39,29,43,31,24,23,21,17,9,11,12,5,13,16,3]

Ptable32 =[6,13,2,1,10,16,8,15,11,14,4,3,7,9,12,5]
Ptable128 = [1,33,3,31,9,56,15,42,63,60,51,53,49,24,29,26,59,17,37,54,55,12,48,22,44,36,23,47,57,19,7,40,64,62,39,58,5,45,38,4,30,14,27,43,41,25,50,34,32,20,28,10,18,21,11,6,16,52,61,35,8,13,46,2]
################################### 64 BLOCK SIZE ######################################
IPtable64 = (58, 50, 42, 34, 26, 18, 10, 2,
             60, 52, 44, 36, 28, 20, 12, 4,
             62, 54, 46, 38, 30, 22, 14, 6,
             64, 56, 48, 40, 32, 24, 16, 8,
             57, 49, 41, 33, 25, 17, 9, 1,
             59, 51, 43, 35, 27, 19, 11, 3,
             61, 53, 45, 37, 29, 21, 13, 5,
             63, 55, 47, 39, 31, 23, 15, 7)

IIPtable64 = (40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25)

EPtable64 =  (32, 1, 2, 3, 4, 5,
              4, 5, 6, 7, 8, 9,
              8, 9, 10, 11, 12, 13,
              12, 13, 14, 15, 16, 17,
              16, 17, 18, 19, 20, 21,
              20, 21, 22, 23, 24, 25,
              24, 25, 26, 27, 28, 29,
              28, 29, 30, 31, 32, 1)

Ptable64 = (16, 7, 20, 21, 29, 12, 28, 17,
           1, 15, 23, 26, 5, 18, 31, 10,
           2, 8, 24, 14, 32, 27, 3, 9,
           19, 13, 30, 6, 22, 11, 4, 25)

PC1table32=[6,18,11,9,12,3,10,23,27,19,30,14,28,25,2,26,13,22,20,21,29,17,31,15,4,5,7,1]

PC1table64 = (57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27,
                19, 11, 3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4)

PC1table128=[55,1,25,23,61,95,97,92,107,19,115,116,109,90,71,85,75,91,12,125,111,100,7,67,110,126,83,113,17,105,124,35,31,28,101,103,43,26,123,10,122,51,117,99,108,106,11,68,121,15,46,102,5,45,98,119,34,77,57,52,70,20,37,93,78,73,53,63,79,94,62,81,66,127,49,60,58,33,74,39,59,44,69,50,87,89,65,36,30,82,38,9,42,29,14,21,84,47,27,18,6,22,86,76,118,54,114,41,3,13,4,2]

PC2table32 = [12,25,4,27,20,19,24,18,28,22,21,17,3,15,9,14,10,5,8,6,11,1,2,13]
PC2table64 = (14, 17, 11, 24, 1, 5, 3, 28,
                15, 6, 21, 10, 23, 19, 12, 4,
                26, 8, 16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55, 30, 40,
                51, 45, 33, 48, 44, 49, 39, 56,
                34, 53, 46, 42, 50, 36, 29, 32)
PC2table128 = [85,102,9,65,35,53,99,29,20,45,104,75,100,4,21,14,23,3,13,98,106,6,27,79,57,42,111,12,69,38,108,64,54,32,96,51,91,36,82,74,110,70,88,84,78,86,66,11,76,67,60,77,56,68,52,50,94,92,105,55,97,49,62,63,28,48,40,59,44,80,71,101,87,1,41,73,46,30,83,22,26,34,5,103,37,18,24,89,17,47,19,10,25,7,8,2]

sBox=[
		[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
		0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
		4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
		15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ],

		[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
		3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
		0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
		13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ],

		[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
		13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
		13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
		1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

		[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
		13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
		10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
		3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

		[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
		14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
		4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
		11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

		[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
		10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
		9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
		4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

		[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
		13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
		1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
		6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ],

		[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
		1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
		7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
		2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],

		[9,4,11,3,1,15,10,14,13,8,7,6,5,12,2,0,7,11,3,1,14,6,12,2,15,13,5,9,10,8,4,0,1,5,14,8,13,3,11,9,15,12,6,0,7,2,10,4,11,15,14,12,13,8,1,2,3,4,5,9,7,10,6,0],

		[7,10,3,11,15,1,5,14,12,13,8,0,6,9,2,4,2,7,4,11,10,3,15,13,9,8,6,14,5,1,0,12,4,0,12,14,13,8,11,9,15,5,10,6,7,3,2,1,2,1,15,0,10,7,6,14,13,11,4,8,9,5,12,3],

		[9,14,11,12,5,1,15,2,10,4,13,6,7,8,3,0,2,3,12,11,6,13,8,10,15,5,0,14,7,9,4,1,6,9,2,1,15,10,4,0,11,13,8,14,7,5,3,12,12,9,6,2,0,10,4,13,14,8,11,7,5,3,15,1],

		[6,4,12,11,10,5,14,1,15,13,9,7,2,8,0,3,3,8,9,1,11,13,15,2,10,14,5,7,4,6,12,0,5,2,15,12,13,10,7,11,8,9,6,14,1,4,3,0,10,7,2,5,15,12,13,14,9,8,4,6,11,1,0,3],

		[6,11,12,2,13,3,15,8,9,5,14,1,7,10,0,4,4,0,6,1,14,15,11,9,10,13,8,5,7,3,2,12,5,12,9,10,13,2,7,0,15,14,3,6,1,8,11,4,8,1,0,6,4,5,12,14,13,7,11,15,9,10,3,2],

		[14,13,10,11,15,12,8,1,6,3,4,7,2,9,0,5,7,1,14,8,15,11,13,10,12,9,6,5,3,4,2,0,14,2,4,7,15,1,11,8,6,13,9,5,12,3,0,10,13,1,9,10,14,6,11,15,5,2,8,7,4,3,12,0],

		[14,0,8,9,6,13,15,3,11,1,12,5,2,4,10,7,7,12,3,13,14,10,15,11,9,8,6,2,5,0,1,4,3,14,1,10,11,5,9,8,15,13,12,4,7,2,6,0,3,1,7,15,13,4,14,9,12,0,8,5,11,10,2,6],

		[11,2,15,5,13,10,7,8,3,4,12,14,9,6,1,0,2,4,6,12,10,8,14,1,15,13,9,5,7,11,0,3,7,15,3,4,14,5,11,1,9,13,8,2,6,10,12,0,13,11,14,15,5,12,1,2,10,4,7,9,6,8,3,0]
]

########################################################################################
#if n, bs, key changes, reset them
ciphertextlist = list()#list of list containing all individual ciphertext at each round
subkey1 = list()#all subkeys of key1 at each round
subkey2 = list()#all subkeys of key2 at each round

#hex to bin, vice versa
HTI = dict(zip(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],range(52)))
ITB = dict(zip(range(52),["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]))

def setpara(zn = 16, zbs = 64, zsubkey1, zsubkey2 = "", zeord=0):
    global n, bs, subkey1, subkey2, eord
    n, bs, subkey1, subkey2, eord = zn, zbs, zsubkey1, zsubkey2, zeord
    if bs is 64:
        IPtable = IPtable64
        IIPtable = IIPtable64
        EPtable = EPtable64
        Ptable = Ptable64
        PC1table = PC1table64
        PC2table = PC2table64
    elif bs is 32:
        IPtable = IPtable32
        IIPtable = IIPtable32
        EPtable = EPtable32
        Ptable = Ptable32
        PC1table = PC1table32
        PC2table = PC2table32
    elif bs is 128:
        IPtable = IPtable128
        IIPtable = IIPtable128
        EPtable = EPtable128
        Ptable = Ptable128
        PC1table = PC1table128
        PC2table = PC2table128

def subkey_gen(key, n):
    global IPtable, IIPtable, EPtable, Ptable, PC1table, PC2table, sBox
    temp = ""
    subkey = list()
    # pc1 on key
    for s in PC1table:
        temp += key[s - 1]
    # split
    temp1 = temp[0: 28]
    temp2 = temp[28:]
    # shift both parts
    for i in range(0, n):
        t = shift_table[i]
        for j in range(0, t):  # rotate
            temp1 = temp1[1:] + temp1[:1]
            temp2 = temp2[1:] + temp2[:1]
        k = temp1 + temp2

        l = ""
        for s in PC2table:
            l += k[s - 1]
        subkey.append(l)
    return subkey

def fiestal(plaintext, subkeylist, eord, bs, n):
    global IPtable, IIPtable, EPtable, Ptable, PC1table, PC2table, sBox, ciphertextlist
    if eord is 1:
        subkeylist = lambda: [ele for ele in reversed(subkeylist)]

    blocks = len(plaintext)/bs
    for j in range(0, n):#rounds
        ans = ""
        for i in range(0, blocks):#block by block process
            text = plaintext[i*bs : (i+1)*bs]
            ltext = text[0 : bs/2]
            rtext = text[bs/2 : ]
            ttt = ltext
            ltext = rtext
            a = ""
            for s in EPtable:#E perm
                a += rtext[s-1]
            #xor key and
            b = subkeylist[i]
            y = int(a, 2) ^ int(b, 2)
            rtext = bin(y)[2:].zfill(len(a))
            t = ""
            for s in range(0, bs/8):
                b = rtext[s*6 : (s+1)*6]
                c = b[:1] + b[5:]
                d = b[1:5]
                r = int(c, 2)
                c = int(d, 2)
                t += bin(sBox[s][16*r + c])
            rtext = t
            t = ""
            for s in Ptable:
                t += rtext[s-1]
            rtext = t
            # xor
            y = int(rtext, 2) ^ int(ttt, 2)
            rtext = bin(y)[2:].zfill(len(a))
            ans += rtext+ltext
        plaintext = ans
        ciphertextlist.append(ans)
    ans = ans[32:] + ans[:32]
    ciphertextlist.append(ans)

def process(n, bs, key, plaintext, eord=0):
    pad_state = 0
    ans = ""
    global IPtable, IIPtable, EPtable, Ptable, PC1table, PC2table, sBox, ciphertextlist
    # hex to bin plaintext
    for s in plaintext:
        ans += ITB[HTI[s]]
    plaintext = ans
    ans = ""

    # key reduction to bs and hex to bin key
    key = key[ : bs/4]
    for s in plaintext:
        ans += ITB[HTI[s]]
    plaintext = ans
    ans = ""

    # padding plaintext
    if len(plaintext)%bs is not 0:
        padwidth = (math.floor(len(plaintext)/bs)+1)*bs
        pad_state = padwidth - len(plaintext)
        plaintext.ljust(padwidth, 1)
        plaintext.ljust(padwidth, 0)
    #padding key
    if len(key) is not bs:
        key.ljust(bs, 1)
        key.ljust(bs, 0)

    #subkey generation
    subkey1 = subkey_gen(key, n)#subkey in bits

    #processtext
    fiestal(plaintext, subkey1, eord, bs, n)




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

btn = Button(fleft1, fg="white", width = 10, font=('arial', 14), text="Encrypt", bg="grey", command = lambda: [setpara(), make(textBoxentry.get("1.0",END), 0), textBoxentry.delete("1.0", END)])
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
