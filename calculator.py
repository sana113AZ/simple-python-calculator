from operator import truediv


import tkinter as tk

#open window
root = tk.Tk()
root.title("calculator")

entry = tk.Entry(root, width=20, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

def click(value):
    entry.insert(tk.END,value)
def clear():
    entry.delete(0,tk.END)
def calculator():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"error")

buttons = [
    '7', '8','9','+',
    '4', '5','6','-',
    '1','2','3','*',
    'c','0','=','/'
]
row =1
col=0
for b in buttons:
    if b=='c':
        cmd =clear
    elif b=='=':
        cmd = calculator
    else:
        cmd = lambda val = b : click(val)
    tk.Button(root, text=b, width=5, height=2, font=('Arial', 14),
              command=cmd).grid(row=row, column=col, padx=2, pady=2)

    col +=1
    if col > 3:
        col=0
        row +=1
root.mainloop()
