import tkinter as tk
from tkinter import messagebox as tkm
root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right")
entry.grid(row=0, column=0, columnspan=3)

def button_click(event):
    button = event.widget
    num = button["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)

r = 1
c = 0

numbers = list(range(9, -1, -1))
plus = ["+"]

for i, num in enumerate(numbers + plus, 1):
    button = tk.Button(root, text = f"{num}",font = ("", 30), width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row = r, column = c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0
    
root.mainloop()
