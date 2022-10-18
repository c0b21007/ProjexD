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
    global tori
    if key == "Up":
        my -= 1
        cy = 100*my+50
        tori = tk.PhotoImage(file=f"fig/1.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
    if key == "Down":
        my += 1
        cy = 100*my+50
        tori = tk.PhotoImage(file=f"fig/2.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
    if key == "Left":
        mx -= 1
        cx = 100*mx+50
        tori = tk.PhotoImage(file=f"fig/3.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
    if key == "Right":
        mx += 1
        cx = 100*mx+50
        tori = tk.PhotoImage(file=f"fig/4.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
    if maze_lst[my][mx] != 1:
        if maze_lst[my][mx] == 4:
            mx, my = 0, 1
            fall = True
        else:
            cx, cy = mx*100+50, my*100+50
    else:
        if fall == False:
            if key == "Up":
                my += 1
                cy = 100*my+50
                tori = tk.PhotoImage(file=f"fig/1.png")
                canv.create_image(cx, cy, image=tori, tag="tori")
            if key == "Down":
                my -= 1
                cy = 100*my+50
                tori = tk.PhotoImage(file=f"fig/2.png")
                canv.create_image(cx, cy, image=tori, tag="tori")
            if key == "Left":
                mx += 1
                cx = 100*mx+50
                tori = tk.PhotoImage(file=f"fig/3.png")
                canv.create_image(cx, cy, image=tori, tag="tori")
            if key == "Right":
                mx -= 1
                cx = 100*mx+50
                tori = tk.PhotoImage(file=f"fig/4.png")
                canv.create_image(cx, cy, image=tori, tag="tori")
    canv.coords("tori", cx, cy)
    if (mx == 14) and (my == 7):
        tkm.showinfo("ゴール", "Congratulations!")
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#ウィンドウ作成

    canv = tk.Canvas(root, width=1500, height=900,bg="black")
    canv.pack()#Canvas生成

    #迷路作成&描画
    maze_lst = mm.make_maze(15, 9)
    #print(maze_lst) # 1:壁 0:床
    mm.show_maze(canv, maze_lst)  

    tori = tk.PhotoImage(file=f"fig/9.png")#こうかとんのインスタンス生成
    mx, my = 0, 1
    canv.create_image(mx, my, image=tori, tag="tori")

    key = ""  #現在押されているキー

    #KeyPressとKeyReleaseの設定
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    #常時起動するリアルタイム処理関数の定義
    main_proc() 

    root.mainloop()