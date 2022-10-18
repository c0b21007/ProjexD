import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori", cx, cy)
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

    tori = tk.PhotoImage(file="fig/5.png")#練習3
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = ""  #現在押されているキー

    #練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()

    

    root.mainloop()