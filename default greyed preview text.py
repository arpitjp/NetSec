import tkinter as tk

def handle_focus_in(_):
    full_name_entry.delete(0, tk.END)
    full_name_entry.config(fg='black')

def handle_focus_out(_):
    full_name_entry.delete(0, tk.END)
    full_name_entry.config(fg='grey')
    full_name_entry.insert(0, "Example: Joe Bloggs")

def handle_enter(txt):
    print(full_name_entry.get())
    handle_focus_out('dummy')

root = tk.Tk()

label = tk.Label(root, text='First and last name:')
label.grid(sticky='e')

full_name_entry = tk.Entry(root, bg='white', width=30, fg='grey')
full_name_entry.grid(row=1, column=1, pady=15, columnspan=2)

full_name_entry.insert(0, "Example: Joe Bloggs")

full_name_entry.bind("<FocusIn>", handle_focus_in)
full_name_entry.bind("<FocusOut>", handle_focus_out)
full_name_entry.bind("<Return>", handle_enter)


root.mainloop()

