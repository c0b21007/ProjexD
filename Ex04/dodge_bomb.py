import pygame as pg
from pygame import font
import sys
from random import randint
from tkinter import messagebox as tkm
import time

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate
def main():
    st = time.time()
    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    # 練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    
    bomb_size = 40  #爆弾の大きさ
    
    # 練習5
    bomb1_sfc = pg.Surface((bomb_size*2, bomb_size*2)) # 空のSurface
    bomb1_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb1_sfc, (255, 0, 0), (bomb_size, bomb_size), bomb_size) # 円を描く
    bomb1_rct = bomb1_sfc.get_rect()
    bomb1_rct.centerx = randint(0, scrn_rct.width)
    bomb1_rct.centery = randint(0, scrn_rct.height)

    #ボム2個目
    bomb2_sfc = pg.Surface((bomb_size*2, bomb_size*2)) # 空のSurface
    bomb2_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb2_sfc, (0, 0, 255), (bomb_size, bomb_size), bomb_size) # 円を描く
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = randint(0, scrn_rct.width)
    bomb2_rct.centery = randint(0, scrn_rct.height)



    # 練習6
    vx1, vy1 = 1, 1
    vx2, vy2 = -1, 1
    hit_num1, hit_num2 = 1, 1
    acce1, acce2 = 0.15, 0.15
    clock = pg.time.Clock() # 練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) # 練習3

        # 練習7
        yoko1, tate1 = check_bound(bomb1_rct, scrn_rct)
        if tate1 == -1 or yoko1 == -1:
            hit_num1 += 1
            if hit_num1%3 == 0:
                vx1 += acce1*vx1
                vy1 += acce1*vy1
        vx1 *= yoko1
        vy1 *= tate1
        bomb1_rct.move_ip(vx1, vy1) # 練習6
        scrn_sfc.blit(bomb1_sfc, bomb1_rct) # 練習5

        # 練習7-2
        yoko2, tate2 = check_bound(bomb2_rct, scrn_rct)
        if tate2 == -1 or yoko2 == -1:
            hit_num2 += 1
            if hit_num2%3 == 0:
                vx2 += acce2*vx2
                vy2 += acce2*vy2
        vx2 *= yoko2
        vy2 *= tate2
        bomb2_rct.move_ip(vx2, vy2) # 練習6-2
        scrn_sfc.blit(bomb2_sfc, bomb2_rct) # 練習5-2

        # 練習8
        if tori_rct.colliderect(bomb1_rct) or tori_rct.colliderect(bomb2_rct): # こうかとんrctが爆弾rctと重なったら
            ed = time.time()
            tkm.showinfo("Hit", f"所要時間：{(ed-st):.2f}秒")
            tkm.showinfo("Hit", "残念！またがんばろう！")
            return

        pg.display.update() #練習2
        clock.tick(1000)





if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()