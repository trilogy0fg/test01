
"""scrolble widget"""
# root = tkinter.Tk()
#
# style = ttk.Style()
# style.theme_settings("default", {
#    "TCombobox": {
#        "configure": {"padding": 5},
#        "map": {
#            "background": [("active", "green2"),
#                           ("!disabled", "green4")],
#            "fieldbackground": [("!disabled", "green3")],
#            "foreground": [("focus", "OliveDrab1"),
#                           ("!disabled", "OliveDrab2")]
#        }
#    }
# })
# combo = ttk.Combobox().pack()
# root.tk.call('source', 'forest-light.tcl ')
#
# # Set the theme with the theme_use method
# ttk.Style().theme_use('forest-light')
#
#
#
# root.mainloop()

"""back ground changing colors"""
# import tkinter
# from tkinter import ttk
#
# root = tkinter.Tk()
#
# style = ttk.Style()
# style.map("C.TButton",
#     foreground=[('pressed', 'red'), ('active', 'blue')],
#     background=[('pressed', '!disabled', 'black'), ('active', 'white')]
#     )
#
# colored_btn = ttk.Button(text="Test", style="C.TButton").pack()
#
# root.mainloop()
"""rooling choises widget"""
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Combobox Widget')
#
#
# def month_changed(event):
#     msg = f'You selected {month_cb.get()}!'
#     showinfo(title='Result', message=msg)
#
#
# # month of year
# months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
#
# label = ttk.Label(text="Please select a month:")
# label.pack(fill='x', padx=5, pady=5)
#
# # create a combobox
# selected_month = tk.StringVar()
#
# month_cb = ttk.Combobox(root, textvariable=selected_month)
# month_cb['values'] = months
# month_cb['state'] = 'readonly'  # normal
# month_cb.pack(fill='x', padx=5, pady=5)
# root.tk.call('source', 'forest-light.tcl ')
#
# # Set the theme with the theme_use method
# ttk.Style().theme_use('forest-light')
# month_cb.bind('<<ComboboxSelected>>', month_changed)
#
# root.mainloop()
"""calendar"""
# import tkinter as tk
# from tkinter import ttk
# from tkcalendar import Calendar, DateEntry
#
# def example1():
#     def print_sel():
#         print(cal.selection_get())
#
#     top = tk.Toplevel(root)
#
#     cal = Calendar(top,
#                    font="Arial 14", selectmode='day',
#                    cursor="hand1", year=2021, month=9, day=1)
#     cal.pack(fill="both", expand=True)
#     ttk.Button(top, text="ok", command=print_sel).pack()
#
# def example2():
#     top = tk.Toplevel(root)
#
#     ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
#
#     cal = DateEntry(top, width=12, background='darkblue',
#                     foreground='white', borderwidth=2)
#     cal.pack(padx=10, pady=10)
#
# root = tk.Tk()
# s = ttk.Style(root)
# s.theme_use('clam')
#
# ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
# ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)
#
# root.mainloop()
"""calender2 whitout output"""
# import tkinter
#
# import tkcalendar
# import tkinter.simpledialog
#
# class CalendarDialog(tkinter.simpledialog.Dialog):
#     """Dialog box that displays a calendar and returns the selected date"""
#     def body(self, master):
#         self.calendar = tkcalendar.Calendar(master)
#         self.calendar.pack()
#
#     def apply(self):
#         self.result = self.calendar.selection
#
# # Demo code:
# def main():
#     root = tkinter.Tk()
#     root.wm_title("CalendarDialog Demo")
#
#     def onclick():
#         cd = CalendarDialog(root)
#         print(cd.result)
#
#     button = tkinter.Button(root, text="Click me to see a calendar!", command=onclick)
#     button.pack()
#     root.update()
#
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()
"""progress bar"""
# import tkinter as tk
# from tkinter import ttk
#
# # root window
# root = tk.Tk()
# root.geometry('300x120')
# root.title('Progressbar Demo')
#
# root.grid()
#
# # progressbar
# pb = ttk.Progressbar(
#     root,
#     orient='horizontal',
#     mode='indeterminate',
#     length=280
# )
# # place the progressbar
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
#
#
# # start button
# start_button = ttk.Button(
#     root,
#     text='Start',
#     command=pb.start
# )
# start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)
#
# # stop button
# stop_button = ttk.Button(
#     root,
#     text='Stop',
#     command=pb.stop
# )
# stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
#
#
# root.mainloop()
"""separator"""
# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Separator Widget Demo')
#
# ttk.Label(root, text="First Label").grid(row=1,column=1)
#
# separator = ttk.Separator(root, orient='horizontal')
# separator.grid(row=2)
# ttk.Label(root, text="Second Label").grid(row=3,column=1)
#
# root.mainloop()
'''tree view'''
# from tkinter import *
# from tkinter import ttk
# ws = Tk()
#
# ws.title('PythonGuides')
# ws.geometry('400x300')
# ws['bg']='#fb0'
#
# tv = ttk.Treeview(ws,columns=('Rank','nom','identifiant', 'deg','connector','specifications'),show='headings')
#
# tv['columns']=('Rank','nom','identifiant', 'deg','connector','specifications')
# tv.column('#0', width=0, stretch=NO)
# tv.column('Rank', width=80)
# tv.column('nom', width=80)
# tv.column('identifiant', width=80)
# tv.column('deg', width=80)
# tv.column('connector',  width=80)
# tv.column('specifications',  width=80)
#
# tv.heading('#0', text='', anchor=CENTER)
# tv.heading('Rank', text='Id', anchor=CENTER)
# tv.heading('identifiant', text='M/F', anchor=CENTER)
# tv.heading('identifiant', text='M/F', anchor=CENTER)
# tv.heading('deg', text='90/180', anchor=CENTER)
# tv.heading('connector', text='CONNECTOR', anchor=CENTER)
# tv.heading('specifications', text='SPECIFICATION ', anchor=CENTER)
#
#
# # Level 1
# T1=tv.insert("", 'end',iid='1',open=True, values=("1","FaAKRA","","","",""))
# T2=tv.insert("", 'end',iid='2',open=True, values=("2","Rosenberger","","","",""))
# T3=tv.insert("", 'end',iid='3',open=True, values=("3","Ring-Tongue","","","",""))
# T4=tv.insert("", 'end',iid='4',open=True, values=("4","MATE-AX","Female","180","114-94413 et 108-94515",""))
# T5=tv.insert("", 'end',iid='5',open=True, values=("5","coax","","","",""))
#
# # Level 2
# tv.insert(1, "end", "",values=("1.1","FAKRA ","","180"," 114-32145","AUTOMATED"))
# tv.insert(1, "end", "",values=("1.2","Female","180","114-13157","FIV",""))
# tv.insert(1, "end", "",values=("1.3","Male","180","114-13157","FIV",""))
# tv.insert(1, "end", "",values=("1.4","Female","180","AUTOMATED 114-32145","FA",""))
# tv.insert(1, "end", "",values=("1.5","Male","180","AUTOMATED 114-32145","FA",""))
# tv.insert(1, "end", "",values=("1.6","Female","180","AUTOMATED 114-32145","Sealed FA",""))
# tv.insert(1, "end", "",values=("1.7","Male","180","AUTOMATED 114-32145","Sealed FA",""))
#
# tv.insert(T2, "end", "", text="5QF SEALED", values=("2.1","Female","180","MA_59V047 AND MA_59V111","5QF SEALED",""))
# tv.insert(T2, "end", "", text="5QF SEALED", values=("2.2","Male","180","MA_59V046","5QF SEALED",""))
# tv.insert(T2, "end", "", text="Plug HSG 90 SEALED", values=("2.3","","90","MA_59V115","SEALED",""))
# tv.insert(T2, "end", "", text="Rosenberger Sealed", values=("2.4","Female","","MA_59V050","Sealed",""))
# tv.insert(T2, "end", "", text="Rosenberger Sealed", values=("2.5","Male","","MA_59V067","Sealed",""))
#
#
# tv.insert(T5, "end", "", text="5QF SEALED", values=("5.1","Female","180","114-18622 et 108-2129","",""))
# tv.insert(T5, "end", "", text="5QF SEALED", values=("5.2","Female","180","114-18622 et 108-2126","Sealed  TUBE",""))
# tv.insert(T5, "end", "", text="90 SEALED", values=("5.3","Female","180","114-18622 et 108-2129","with clip Slot",""))
# tv.insert(T5, "end", "", text="Rosenberger Sealed", values=("5.4","Female","180","114-18622 et 108-2129"," With Mount",""))
# tv.insert(T5, "end", "", text="Rosenberger Sealed", values=("5.5","Female","180","114-18622 et 108-2129","subassy",""))
# tv.insert(T5, "end", "", text="5QF SEALED", values=("5.6","Female","90","114-18623 et 108-94089","",""))
# tv.insert(T5, "end", "", text="5QF SEALED", values=("5.7","Male","180","114-18622 et 108-2129","",""))
# tv.insert(T5, "end", "", text="90 SEALED", values=("5.8","Male","180","114-18622 et 108-2129","",""))
# tv.insert(T5, "end", "", text="Rosenberger Sealed", values=("5.9","Male","180","114-18622 et 108-2129","",""))
# tv.insert(T5, "end", "", text="Rosenberger Sealed", values=("10","","","","",""))
#
#
# tv.pack()
# ws.mainloop()

"""tix"""
# from tkinter import *
# import pandas as pd
#
# class TreeCheckList(object):
#     def __init__(self, root):
#         self.root = root
#
#         self.cl = ttk.CheckList(self.root)
#         self.cl.pack(fill=ttk.BOTH, expand=ttk.YES)
#         self.cl.hlist.config(bg='white', bd=0, selectmode='none', selectbackground='white', selectforeground='black', drawbranch=True, pady=5)
#
#         self.cl.hlist.add('ALL', text='All Messages')
#
#         self.cl.hlist.add('ALL.First', text='First')
#         self.cl.setstatus('ALL.First', "off")
#
#         self.cl.hlist.add('ALL.Second', text='Second')
#         self.cl.setstatus('ALL.Second', "off")
#
#         self.cl.autosetmode()
#
# def main():
#     root = ttk.Tk()
#     top = ttk.Toplevel(root)
#
#     checklist = TreeCheckList(top)
#     root.update()
#     top.tkraise()
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()
"""check box"""
# var= intVar()
# c=checkbutton(window2, text='', variable=var)
# c.pack
'''dropdown menus'''
# clicked= StingVar()
# clicked.set("value")
# drop= OptionMenu(window2, clicked, "","","","","",)
# drop.pack()
"""open file"""
# Importing Tkinter and Ttk
import tkinter as tk
from tkinter import ttk

# Create the window
root = tk.Tk()
root.title('Azure')

# Place the window in the center of the screen
windowWidth = 800
windowHeight = 530
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))

# Create a style
style = ttk.Style(root)

# Just simply import the azure.tcl file
root.tk.call("source", "azure.tcl")
# Then set the theme you want with the set_theme procedure
root.tk.call("set_theme", "dark")

# Creating lists
option_list = ['', 'OptionMenu', 'Value 1', 'Value 2']
combo_list = ['Combobox', 'Editable item 1', 'Editable item 2']
readonlycombo_list = ['Readonly combobox', 'Item 1', 'Item 2']

# Create control variables
a = tk.IntVar()
b = tk.IntVar(value=1)
c = tk.IntVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_list[1])
f = tk.IntVar()
g = tk.IntVar(value=75)
h = tk.IntVar()

# Create a Frame for the Checkbuttons
checkframe = ttk.LabelFrame(root, text='Checkbuttons', width=210, height=200)
checkframe.place(x=20, y=12)

# Checkbuttons
check1 = ttk.Checkbutton(checkframe, text='Unchecked', variable=a, offvalue=0, onvalue=1)
check1.place(x=20, y=20)
check2 = ttk.Checkbutton(checkframe, text='Checked', variable=b, offvalue=0, onvalue=1)
check2.place(x=20, y=60)
check3 = ttk.Checkbutton(checkframe, text='Third state', variable=c, offvalue=0, onvalue=1)
check3.state(['alternate'])
check3.place(x=20, y=100)
check4 = ttk.Checkbutton(checkframe, text='Disabled', state='disabled')
check4.place(x=20, y=140)

# Create a Frame for the Radiobuttons
radioframe = ttk.LabelFrame(root, text='Radiobuttons', width=210, height=160)
radioframe.place(x=20, y=252)

# Radiobuttons
radio1 = ttk.Radiobutton(radioframe, text='Deselected', variable=d, value=1)
radio1.place(x=20, y=20)
radio2 = ttk.Radiobutton(radioframe, text='Selected', variable=d, value=2)
radio2.place(x=20, y=60)
radio3 = ttk.Radiobutton(radioframe, text='Disabled', state='disabled')
radio3.place(x=20, y=100)

# Separator
separator = ttk.Separator()
separator.place(x=20, y=235, width=210)

def scale_function(*arg):
    g.set(int(scale.get()))

# Scale
scale = ttk.Scale(root, from_=100, to=0, variable=g, command=scale_function)
scale.place(x=80, y=430)

# Progressbar
progress = ttk.Progressbar(root, value=0, variable=g, mode='determinate')
progress.place(x=80, y=480)

# Entry
entry = ttk.Entry(root)
entry.place(x=250, y=20)
entry.insert(0, 'Entry')

# Spinbox
spinbox = ttk.Spinbox(root, from_=0, to=100, increment=0.1)
spinbox.place(x=250, y=70)
spinbox.insert(0, 'Spinbox')

# Combobox
combobox = ttk.Combobox(root, value=combo_list)
combobox.current(0)
combobox.place(x=250, y=120)

# Read-only combobox
readonlycombo = ttk.Combobox(root, state='readonly', value=readonlycombo_list)
readonlycombo.current(0)
readonlycombo.place(x=250, y=170)

# Menu for the Menubutton
menu = tk.Menu(root, tearoff=0)
menu.add_command(label='Menu item 1')
menu.add_command(label='Menu item 2')
menu.add_separator()
menu.add_command(label='Menu item 3')
menu.add_command(label='Menu item 4')

# Menubutton
menubutton = ttk.Menubutton(root, text='Menubutton', menu=menu, direction='below')
menubutton.place(x=250, y=220)

# OptionMenu
optionmenu = ttk.OptionMenu(root, e, *option_list)
optionmenu.place(x=250, y=270)

def button_function():
    print('Button callback')

# Button
button = ttk.Button(root, text='Button', command=button_function)
button.place(x=250, y=320)

# Accentbutton
accentbutton = ttk.Button(root, text='AccentButton', command=button_function)
accentbutton.place(x=250, y=370)

# ToggleButton
togglebutton = ttk.Checkbutton(root, text='ToggleButton',  variable=f, offvalue=0, onvalue=1)
togglebutton.place(x=250, y=420)

# Switch
switch = ttk.Checkbutton(root, text='Switch on',  variable=h, offvalue=0, onvalue=1)
switch.place(x=250, y=470)
switch.invoke()

def switch_function():
    if h.get():
        switch.config(text='Switch on')
    else:
        switch.config(text='Switch off')

switch.config(command=switch_function)

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.pack(padx=5, pady=5, side='bottom', anchor='se')

# Notebook
notebook = ttk.Notebook(root)
notebookTab1 = ttk.Frame(notebook, width=335, height=150)
notebook.add(notebookTab1, text='Tab 1')
notebookTab2 = ttk.Frame(notebook, width=335, height=150)
notebook.add(notebookTab2, text='Tab 2')
notebookTab3 = ttk.Frame(notebook, width=335, height=150)
notebook.add(notebookTab3, text='Tab 3')
notebook.place(x=420, y=330)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(root)
treeFrame.place(x=420, y=20)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side='right', fill='y')

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
treeview.pack()

treeScroll.config(command=treeview.yview)

treeview.column("#0", width=120)
treeview.column(1, anchor='w', width=100)
treeview.column(2, anchor='w', width=100)

treeview.heading("#0", text="Treeview", anchor='center')
treeview.heading(1, text="Column 1", anchor='center')
treeview.heading(2, text="Column 2", anchor='center')

treeview.insert(parent='', index='end', iid=1, text="Parent", values=("Item 1", "Value 1"))
treeview.item(1, open=True)
treeview.insert(parent=1, index='end', iid=2, text="Child", values=("Subitem 1.1", "Value 1.1"))
treeview.insert(parent=1, index='end', iid=3, text="Child", values=("Subitem 1.2", "Value 1.2"))
treeview.insert(parent=1, index='end', iid=4, text="Child", values=("Subitem 1.3", "Value 1.3"))
treeview.insert(parent=1, index='end', iid=5, text="Child", values=("Subitem 1.4", "Value 1.4"))
treeview.insert(parent='', index='end', iid=6, text="Parent", values=("Item 2", "Value 2"))
treeview.item(6, open=True)
treeview.insert(parent=6, index='end', iid=13, text="Child", values=("Subitem 2.1", "Value 2.1"))
treeview.insert(parent=6, index='end', iid=7, text="Sub-parent", values=("Subitem 2.2", "Value 2.2"))
treeview.item(7, open=True)
treeview.insert(parent=7, index='end', iid=8, text="Child", values=("Subitem 2.2.1", "Value 2.2.1"))
treeview.insert(parent=7, index='end', iid=9, text="Child", values=("Subitem 2.2.2", "Value 2.2.2"))
treeview.selection_set(9)
treeview.insert(parent=7, index='end', iid=10, text="Child", values=("Subitem 2.2.3", "Value 2.2.3"))
treeview.insert(parent=6, index='end', iid=11, text="Child", values=("Subitem 2.3", "Value 2.3"))
treeview.insert(parent=6, index='end', iid=12, text="Child", values=("Subitem 2.4", "Value 2.4"))
treeview.insert(parent='', index='end', iid=14, text="Parent", values=("Item 3", "Value 3"))
treeview.item(14, open=True)
treeview.insert(parent=14, index='end', iid=15, text="Child", values=("Subitem 3.1", "Value 3.1"))
treeview.insert(parent=14, index='end', iid=16, text="Child", values=("Subitem 3.2", "Value 3.2"))
treeview.insert(parent=14, index='end', iid=17, text="Child", values=("Subitem 3.3", "Value 3.3"))
treeview.insert(parent=14, index='end', iid=18, text="Child", values=("Subitem 3.4", "Value 3.4"))
treeview.insert(parent='', index='end', iid=19, text="Parent", values=("Item 4", "Value 4"))
treeview.item(19, open=True)
treeview.insert(parent=19, index='end', iid=20, text="Child", values=("Subitem 4.1", "Value 4.1"))
treeview.insert(parent=19, index='end', iid=21, text="Sub-parent", values=("Subitem 4.2", "Value 4.2"))
treeview.item(21, open=True)
treeview.insert(parent=21, index='end', iid=22, text="Child", values=("Subitem 4.2.1", "Value 4.2.1"))
treeview.insert(parent=21, index='end', iid=23, text="Child", values=("Subitem 4.2.2", "Value 4.2.2"))
treeview.insert(parent=21, index='end', iid=24, text="Child", values=("Subitem 4.2.3", "Value 4.2.3"))
treeview.insert(parent=19, index='end', iid=25, text="Child", values=("Subitem 4.3", "Value 4.3"))

root.mainloop()
"""load document"""
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
#
# # Root window
# root = tk.Tk()
# root.title('Display a Text File')
# root.resizable(False, False)
# root.geometry('550x250')
#
# # Text editor
# text = tk.Text(root, height=12)
# text.grid(column=0, row=0, sticky='nsew')
#
#
# def open_text_file():
#     # file type
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )
#     # show the open file dialog
#     f = fd.askopenfile(filetypes=filetypes)
#     # read the text file and show its content on the Text
#     text.insert('1.0', f.readlines())
#
#
# # open file button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=open_text_file
# )
#
# open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)
#
#
# root.mainloop()
# import tkinter module
# import tkinter module
# Program to make a simple
# login screen
'''application'''

# from tkinter import *
#
# if __name__ == '__main__':
#     form = Tk()
#
#     getFld = IntVar()
#
#     form.wm_title('File Parser')
#
#     stepOne = LabelFrame(form, text=" 1. Enter File Details: ")
#     stepOne.grid(row=0, columnspan=7, sticky='W', \
#                  padx=5, pady=5, ipadx=5, ipady=5)
#
#     helpLf = LabelFrame(form, text=" Quick Help ")
#     helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
#                 sticky='NS', padx=5, pady=5)
#     helpLbl = Label(helpLf, text="Help will come - ask for it.")
#     helpLbl.grid(row=0)
#
#     stepTwo = LabelFrame(form, text=" 2. Enter Table Details: ")
#     stepTwo.grid(row=2, columnspan=7, sticky='W', \
#                  padx=5, pady=5, ipadx=5, ipady=5)
#
#     stepThree = LabelFrame(form, text=" 3. Configure: ")
#     stepThree.grid(row=3, columnspan=7, sticky='W', \
#                    padx=5, pady=5, ipadx=5, ipady=5)
#
#     inFileLbl = Label(stepOne, text="Select the File:")
#     inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)
#
#     inFileTxt = Entry(stepOne)
#     inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)
#
#     inFileBtn = Button(stepOne, text="Browse ...")
#     inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
#
#     outFileLbl = Label(stepOne, text="Save File to:")
#     outFileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)
#
#     outFileTxt = Entry(stepOne)
#     outFileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)
#
#     outFileBtn = Button(stepOne, text="Browse ...")
#     outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)
#
#     inEncLbl = Label(stepOne, text="Input File Encoding:")
#     inEncLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2)
#
#     inEncTxt = Entry(stepOne)
#     inEncTxt.grid(row=2, column=1, sticky='E', pady=2)
#
#     outEncLbl = Label(stepOne, text="Output File Encoding:")
#     outEncLbl.grid(row=2, column=5, padx=5, pady=2)
#
#     outEncTxt = Entry(stepOne)
#     outEncTxt.grid(row=2, column=7, pady=2)
#
#     outTblLbl =Label(stepTwo, \
#           text="Enter the name of the table to be used in the statements:")
#     outTblLbl.grid(row=3, column=0, sticky='W', padx=5, pady=2)
#
#     outTblTxt = Entry(stepTwo)
#     outTblTxt.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE')
#
#     fldLbl = Label(stepTwo, \
#                            text="Enter the field (column) names of the table:")
#     fldLbl.grid(row=4, column=0, padx=5, pady=2, sticky='W')
#
#     getFldChk = Checkbutton(stepTwo, \
#                            text="Get fields automatically from input file",\
#                            onvalue=1, offvalue=0)
#     getFldChk.grid(row=4, column=1, columnspan=3, pady=2, sticky='WE')
#
#     fldRowTxt = Entry(stepTwo)
#     fldRowTxt.grid(row=5, columnspan=5, padx=5, pady=2, sticky='WE')
#
#     transChk = Checkbutton(stepThree, \
#                text="Enable Transaction", onvalue=1, offvalue=0)
#     transChk.grid(row=6, sticky='W', padx=5, pady=2)
#
#     transRwLbl = Label(stepThree, \
#                  text=" => Specify number of rows per transaction:")
#     transRwLbl.grid(row=6, column=2, columnspan=2, \
#                     sticky='W', padx=5, pady=2)
#
#     transRwTxt = Entry(stepThree)
#     transRwTxt.grid(row=6, column=4, sticky='WE')
#
#     form.mainloop()
'''open file name '''
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
#
# # create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')
#
#
# def select_file():
#     filetypes = (
#         ('text files', '*.docx'),
#         ('All files', '*.*')
#     )
#
#     filename = fd.askopenfilename(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes)
#
#     filename.LoadFileDialog(
#         title='Selected File',
#         message=filename
#     )
#
#
# # open button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=select_file
# )
#
# open_button.pack(expand=True)
#
#
# # run the application
# root.mainloop()

'''read txt file'''
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
#
# # Root window
# root = tk.Tk()
# root.title('Display a Text File')
# root.resizable(False, False)
# root.geometry('550x250')

# Text editor
# text = tk.Text(root, height=12)
# text.grid(column=0, row=0, sticky='nsew')
#
#
# def open_text_file():
#     # file type
#     filetypes = (
#         ('text files', '*.pdf'),
#         ('All files', '*.*')
#     )
#     # show the open file dialog
#     f = fd.askopenfile(filetypes=filetypes)
#     # read the text file and show its content on the Text
#     text.insert('1.0', f.readlines())
#
#
# # open file button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=open_text_file
# )
#
# open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)
#
#
# root.mainloop()






# from tkinter import ttk
#
# import os
# from PIL import Image, ImageTk
# from ttkwidgets.utilities import get_assets_directory
#
# IM_CHECKED = os.path.join(get_assets_directory(), "checked.png")      # These three checkbox icons were isolated from
# IM_UNCHECKED = os.path.join(get_assets_directory(), "unchecked.png")  # Checkbox States.svg (https://commons.wikimedia.org/wiki/File:Checkbox_States.svg?uselang=en)
# IM_TRISTATE = os.path.join(get_assets_directory(), "tristate.png")    # by Marekich [CC BY-SA 3.0  (https://creativecommons.org/licenses/by-sa/3.0)]
#
#
# class CheckboxTreeview(ttk.Treeview):
#     """
#     :class:`ttk.Treeview` widget with checkboxes left of each item.
#
#     .. note::
#         The checkboxes are done via the image attribute of the item,
#         so to keep the checkbox, you cannot add an image to the item.
#     """
#
#     def __init__(self, master=None, **kw):
#         """
#         Create a CheckboxTreeview.
#         :param master: master widget
#         :type master: widget
#         :param kw: options to be passed on to the :class:`ttk.Treeview` initializer
#         """
#         ttk.Treeview.__init__(self, master, style='Checkbox.Treeview', **kw)
#         # style (make a noticeable disabled style)
#         style = ttk.Style(self)
#         style.map("Checkbox.Treeview",
#                   fieldbackground=[("disabled", '#E6E6E6')],
#                   foreground=[("disabled", 'gray40')],
#                   background=[("disabled", '#E6E6E6')])
#         # checkboxes are implemented with pictures
#         self.im_checked = ImageTk.PhotoImage(Image.open(IM_CHECKED), master=self)
#         self.im_unchecked = ImageTk.PhotoImage(Image.open(IM_UNCHECKED), master=self)
#         self.im_tristate = ImageTk.PhotoImage(Image.open(IM_TRISTATE), master=self)
#         self.tag_configure("unchecked", image=self.im_unchecked)
#         self.tag_configure("tristate", image=self.im_tristate)
#         self.tag_configure("checked", image=self.im_checked)
#         # check / uncheck boxes on click
#         self.bind("<Button-1>", self._box_click, True)
#
#     def expand_all(self):
#         """Expand all items."""
#
#         def aux(item):
#             self.item(item, open=True)
#             children = self.get_children(item)
#             for c in children:
#                 aux(c)
#
#         children = self.get_children("")
#         for c in children:
#             aux(c)
#
#     def collapse_all(self):
#         """Collapse all items."""
#
#         def aux(item):
#             self.item(item, open=False)
#             children = self.get_children(item)
#             for c in children:
#                 aux(c)
#
#         children = self.get_children("")
#         for c in children:
#             aux(c)
#
#     def state(self, statespec=None):
#         """
#         Modify or inquire widget state.
#
#         :param statespec: Widget state is returned if `statespec` is None,
#                           otherwise it is set according to the statespec
#                           flags and then a new state spec is returned
#                           indicating which flags were changed.
#         :type statespec: None or sequence[str]
#         """
#         if statespec:
#             if "disabled" in statespec:
#                 self.bind('<Button-1>', lambda e: 'break')
#             elif "!disabled" in statespec:
#                 self.unbind("<Button-1>")
#                 self.bind("<Button-1>", self._box_click, True)
#             return ttk.Treeview.state(self, statespec)
#         else:
#             return ttk.Treeview.state(self)
#
#     def change_state(self, item, state):
#         """
#         Replace the current state of the item.
#         i.e. replace the current state tag but keeps the other tags.
#
#         :param item: item id
#         :type item: str
#         :param state: "checked", "unchecked" or "tristate": new state of the item
#         :type state: str
#         """
#         tags = self.item(item, "tags")
#         states = ("checked", "unchecked", "tristate")
#         new_tags = [t for t in tags if t not in states]
#         new_tags.append(state)
#         self.item(item, tags=tuple(new_tags))
#
#     def tag_add(self, item, tag):
#         """
#         Add tag to the tags of item.
#
#         :param item: item identifier
#         :type item: str
#         :param tag: tag name
#         :type tag: str
#         """
#         tags = self.item(item, "tags")
#         self.item(item, tags=tags + (tag,))
#
#     def tag_del(self, item, tag):
#         """
#         Remove tag from the tags of item.
#
#         :param item: item identifier
#         :type item: str
#         :param tag: tag name
#         :type tag: str
#         """
#         tags = list(self.item(item, "tags"))
#         if tag in tags:
#             tags.remove(tag)
#             self.item(item, tags=tuple(tags))
#
#     def insert(self, parent, index, iid=None, **kw):
#         """
#         Creates a new item and return the item identifier of the newly created item.
#
#         :param parent: identifier of the parent item
#         :type parent: str
#         :param index: where in the list of parent's children to insert the new item
#         :type index: int or "end"
#         :param iid: item identifier, iid must not already exist in the tree. If iid is None a new unique identifier is generated.
#         :type iid: None or str
#         :param kw: other options to be passed on to the :meth:`ttk.Treeview.insert` method
#
#         :return: the item identifier of the newly created item
#         :rtype: str
#         .. note:: Same method as for the standard :class:`ttk.Treeview` but
#                   add the tag for the box state accordingly to the parent
#                   state if no tag among
#                   ('checked', 'unchecked', 'tristate') is given.
#         """
#         if self.tag_has("checked", parent):
#             tag = "checked"
#         else:
#             tag = 'unchecked'
#         if "tags" not in kw:
#             kw["tags"] = (tag,)
#         elif not ("unchecked" in kw["tags"] or "checked" in kw["tags"] or
#                   "tristate" in kw["tags"]):
#             kw["tags"] += (tag,)
#
#         return ttk.Treeview.insert(self, parent, index, iid, **kw)
#
#     def get_checked(self):
#         """Return the list of checked items that do not have any child."""
#         checked = []
#
#         def get_checked_children(item):
#             if not self.tag_has("unchecked", item):
#                 ch = self.get_children(item)
#                 if not ch and self.tag_has("checked", item):
#                     checked.append(item)
#                 else:
#                     for c in ch:
#                         get_checked_children(c)
#
#         ch = self.get_children("")
#         for c in ch:
#             get_checked_children(c)
#         return checked
#
#     def _check_descendant(self, item):
#         """Check the boxes of item's descendants."""
#         children = self.get_children(item)
#         for iid in children:
#             self.change_state(iid, "checked")
#             self._check_descendant(iid)
#
#     def _check_ancestor(self, item):
#         """
#         Check the box of item and change the state of the boxes of item's
#         ancestors accordingly.
#         """
#         self.change_state(item, "checked")
#         parent = self.parent(item)
#         if parent:
#             children = self.get_children(parent)
#             b = ["checked" in self.item(c, "tags") for c in children]
#             if False in b:
#                 # at least one box is not checked and item's box is checked
#                 self._tristate_parent(parent)
#             else:
#                 # all boxes of the children are checked
#                 self._check_ancestor(parent)
#
#     def _tristate_parent(self, item):
#         """
#         Put the box of item in tristate and change the state of the boxes of
#         item's ancestors accordingly.
#         """
#         self.change_state(item, "tristate")
#         parent = self.parent(item)
#         if parent:
#             self._tristate_parent(parent)
#
#     def _uncheck_descendant(self, item):
#         """Uncheck the boxes of item's descendant."""
#         children = self.get_children(item)
#         for iid in children:
#             self.change_state(iid, "unchecked")
#             self._uncheck_descendant(iid)
#
#     def _uncheck_ancestor(self, item):
#         """
#         Uncheck the box of item and change the state of the boxes of item's
#         ancestors accordingly.
#         """
#         self.change_state(item, "unchecked")
#         parent = self.parent(item)
#         if parent:
#             children = self.get_children(parent)
#             b = ["unchecked" in self.item(c, "tags") for c in children]
#             if False in b:
#                 # at least one box is checked and item's box is unchecked
#                 self._tristate_parent(parent)
#             else:
#                 # no box is checked
#                 self._uncheck_ancestor(parent)
#
#     def _box_click(self, event):
#         """Check or uncheck box when clicked."""
#         x, y, widget = event.x, event.y, event.widget
#         elem = widget.identify("element", x, y)
#         if "image" in elem:
#             # a box was clicked
#             item = self.identify_row(y)
#             if self.tag_has("unchecked", item) or self.tag_has("tristate", item):
#                 self._check_ancestor(item)
#                 self._check_descendant(item)
#             else:
#                 self._uncheck_descendant(item)
#                 self._uncheck_ancestor(item)





# from tkinter import *
# from tkinter import ttk
# import tkinter.font as font
# import csv
#
# root = Tk()
# root.title("A") #title shown in bar
#
# TableMargin = ttk.Frame(root)
# TableMargin.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# root.state('zoomed') #fullscreen
#
# # Setting Theme
#
# style = ttk.Style()
# style.configure('Treeview',rowheight=30)
# style.theme_use("clam")
#
# #Heading
# label = ttk.Label(TableMargin, text='Orders')
# label['font'] = font.Font(size=20, weight="bold")
# label.grid(row=0, sticky=(N),pady=5)
#
# #Designing of Table
# style = ttk.Style()
# style.configure("Treeview.Heading", font=(None, 13))
# # scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
# # scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
# tree = ttk.Treeview(TableMargin, columns=("Table No.", "Order", "Time", "Served"), height=400, selectmode="extended") #, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set
# # scrollbary.config(command=tree.yview)
# # scrollbary.pack(side=RIGHT, fill=Y)
# # scrollbarx.config(command=tree.xview)
# # scrollbarx.pack(side=BOTTOM, fill=X)
# tree.heading('Table No.', text="Table No.", anchor=W)
# tree.heading('Order', text="Order", anchor=W)
# tree.heading('Time', text="Time", anchor=W)
# tree.heading('Served', text="Served", anchor=W)
# tree.column('#0', stretch=NO, minwidth=0, width=0)
# tree.column('#1', stretch=NO, minwidth=0, width=100)
# tree.column('#2', stretch=NO, minwidth=0, width=600)
# tree.column('#3', stretch=NO, minwidth=0, width=100)
# tree.column('#4', stretch=NO, minwidth=0, width=100)
#
# tree.grid(row=0, pady=50,padx=190,sticky=(N, E, S))
#
# with open('C:\Users\Usuario\OneDrive\Bureau\username') as f:
#     reader = csv.DictReader(f, delimiter=',')
#     for row in reader:
#         table = row['Table']
#         order = row['Order']
#         time = row['Time']
#         var = IntVar()
#         served = ttk.Checkbutton(TableMargin, text="", variable=var)
#         served.grid()
#         tree.insert("", 1, values=(table, order, time, served))



# def generate():
#     #connection to database / creating
#     conn = sqlite3.connect('datos.db')
#     #creating cursor
#     c=conn.cursor()
#     #insert function
#     c.execute("SELECT APPLICATION SPECIFICATION FROM Applications specifications WHERE APPLICATION SPECIFICATION= ")
#     #commit changes to data database
#     conn.comit()
#     #close Connection
#     conn.close()





#Importing the required packages

# from docxcompose.composer import Composer
# from docx import Document as Document_compose
# #filename_master is name of the file you want to merge the docx file into
# master = Document_compose(filename_master)
#
# composer = Composer(master)
# #filename_second_docx is the name of the second docx file
# doc2 = Document_compose(filename_second_docx)
# #append the doc2 into the master using composer.append function
# composer.append(doc2)
# #Save the combined docx with a name
# composer.save("combined.docx")

''''''''''''''''''''''''''''''''

# If you want to merge multiple documents into one docx file you can use the below function
# #Filename_master is the name of the file you want to merge all the document into
# #files_list is a list containing all the filename of the docx file to be merged
# def combine_all_docx(filename_master,files_list):
#     number_of_sections=len(files_list)
#     master = Document_compose(filename_master)
#     composer = Composer(master)
#     for i in range(0, number_of_sections):
#         doc_temp = Document_compose(files_list[i])
#         composer.append(doc_temp)
#     composer.save("combined_file.docx")
# #For Example
# #filename_master="file1.docx"
# #files_list=["file2.docx","file3.docx","file4.docx",file5.docx"]
# #Calling the function
# #combine_all_docx(filename_master,files_list)
# #This function will combine all the document in the array files_list into the file1.docx and save the merged document into combined_file.docx
# '''''''''''''''''''''''''''''''''''''''''''
#
# from docx import Document
#
# files = ['file1.docx', 'file2.docx']
#
# def combine_word_documents(files):
#     merged_document = Document()
#
#     for index, file in enumerate(files):
#         sub_doc = Document(file)
#
#         # Don't add a page break if you've reached the last file.
#         if index < len(files)-1:
#            sub_doc.add_page_break()
#
#         for element in sub_doc.element.body:
#             merged_document.element.body.append(element)
#
#     merged_document.save('merged.docx')
#
# combine_word_documents(files)





''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # For complete examples and data files, please go to https://github.com/aspose-words-cloud/aspose-words-cloud-python
# import os
# import asposewordscloud
# import asposewordscloud.models.requests
# from shutil import copyfile
#
#
# # Please get your Client ID and Secret from https://dashboard.aspose.cloud.
# client_id='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx'
# client_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#
# words_api = asposewordscloud.WordsApi(client_id,client_secret)
# words_api.api_client.configuration.host='https://api.aspose.cloud'
#
#
# remoteFolder = 'Temp'
# localFolder = 'C:/Temp'
# localFileName = 'destination.docx'
# remoteFileName = 'destination.docx'
# localFileName1 = 'source.docx'
# remoteFileName1 = 'source.docx'
#
# #upload file
# words_api.upload_file(asposewordscloud.models.requests.UploadFileRequest(open(localFolder + '/' + localFileName,'rb'),remoteFolder + '/' + remoteFileName))
# words_api.upload_file(asposewordscloud.models.requests.UploadFileRequest(open(localFolder + '/' + localFileName1,'rb'),remoteFolder + '/' + remoteFileName1))
#
# #append Word documents
# requestDocumentListDocumentEntries0 = asposewordscloud.DocumentEntry(href=remoteFolder + '/' + remoteFileName1, import_format_mode='KeepSourceFormatting')
#
# requestDocumentListDocumentEntries = [requestDocumentListDocumentEntries0]
# requestDocumentList = asposewordscloud.DocumentEntryList(document_entries=requestDocumentListDocumentEntries)
# request = asposewordscloud.models.requests.AppendDocumentRequest(name=remoteFileName, document_list=requestDocumentList, folder=remoteFolder, dest_file_name= remoteFolder + '/' + remoteFileName)
#
# result = words_api.append_document(request)
#
# #download file
# request_download=asposewordscloud.models.requests.DownloadFileRequest(remoteFolder + '/' + remoteFileName)
# response_download = words_api.download_file(request_download)
# copyfile(response_download, localFolder + '/' +"Append_output.docx")
