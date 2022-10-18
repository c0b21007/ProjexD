import tkinter as tk
from tkinter import messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy
    global mx, my
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] != 1:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)
    if (mx == 14) and (my == 7):
            tkm.showinfo("ゴール", "Congratulations!")
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習1

    canv = tk.Canvas(root, width=1500, height=900,bg="black")
    canv.pack()#練習2

    #練習9,10
    maze_lst = mm.make_maze(15, 9)
    #print(maze_lst) # 1:壁 0:床
    mm.show_maze(canv, maze_lst)  

    Inum = 0
    tori = tk.PhotoImage(file=f"fig/5.png")#練習3
    mx, my = 0, 1
    canv.create_image(mx, my, image=tori, tag="tori")

    key = ""  #現在押されているキー

    #練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc() 

    root.mainloop()