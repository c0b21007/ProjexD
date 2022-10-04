import tkinter as tk
from tkinter import messagebox as tkm
import math
root = tk.Tk()
root.geometry("475x555")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right")
entry.grid(row=0, column=0, columnspan=3)

def button_click(event):
    button = event.widget
    num = button["text"]
    entry.insert(tk.END, num)
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
###「=」コマンド
def click_equal(event):
    siki = entry.get()
    result = eval(siki)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
###クリアコマンド
def click_delete(event):
    entry.delete(0, tk.END)

### %コマンド 
def click_nijou(event):
    siki = entry.get()
    res0 = eval(siki)
    result_fin = res0/100
    entry.delete(0, tk.END)
    entry.insert(tk.END, result_fin)

### 「√」コマンド 
def click_root(event):
    num_root = int(entry.get())
    result = math.sqrt(num_root)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

### 2乗コマンド 
def click_nijou(event):
    siki = entry.get()
    res0 = eval(siki)
    result_fin = res0*res0
    entry.delete(0, tk.END)
    entry.insert(tk.END, result_fin)

r = 1
c = 0
numbers = list(range(9, -1, -1))

for i, num in enumerate(numbers, 1):
    button = tk.Button(root, text = f"{num}",font = ("", 30), width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row = r, column = c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0
### 「=」ボタンの実装 
button = tk.Button(root, text = "=",font = ("", 30), width=4, height=2)
button.bind("<1>", click_equal)
button.grid(row = r, column = c)
###　クリアボタンの実装
c+=1
button = tk.Button(root, text = "C",font = ("", 30), width=4, height=2)
button.bind("<1>", click_delete)
button.grid(row = r, column = c)
### 四則演算・小数点ボタンの実装
r=0
c=0
hugou = ["+", "-", "*", "/", ".", "(", ")"]
for i, num in enumerate(hugou, 1):
    button = tk.Button(root, text = f"{num}",font = ("", 30), width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row = r, column = 3+c)
    r+=1
    if r==5:
        r=0
        c+=1

### 「√」ボタンの実装
button = tk.Button(root, text = "√",font = ("", 30), width=4, height=2)
button.bind("<1>", click_root)
button.grid(row = 2, column = 4)

### 2乗ボタンの実装
button = tk.Button(root, text = "^",font = ("", 30), width=4, height=2)
button.bind("<1>", click_nijou)
button.grid(row = 3, column = 4)

### %ボタンの実装
button = tk.Button(root, text = "%",font = ("", 30), width=4, height=2)
button.bind("<1>", click_nijou)
button.grid(row = 4, column = 4)

root.mainloop()