import random 
import sys
import pygame as pg



WIDTH, HEIGHT = 1600, 900


def hantei(rct):
    left, top, right, bottom = rct
    if left < 0:
        bleft = False
    else:
        bleft = True
    if 1600-right < left:
        bright = False
    else:
        bright = True
    if top < 0:
        btop = False
    else:
        btop = True
    if 900-bottom < top:
        bbottom = False
    else:
        bbottom = True
    return (bleft, bright, btop, bbottom)


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))
    x, y = random.randint(10, WIDTH-10), random.randint(10, HEIGHT-10)
    kk_img_rct = kk_img.get_rect()
    kk_img_rct.center = 900, 400
    bakudan_rct = enn.get_rect()
    bakudan_rct.center = x, y
    vx, vy = +5, +5
    img_dct = {(-5, 0):pg.image.load("ex02/fig/3.png"), 
               (-5, -5):pg.transform.rotozoom(pg.image.load("ex02/fig/3.png"), -45, 1.0),
               (-5, +5):pg.transform.rotozoom(pg.image.load("ex02/fig/3.png"), +45, 1.0),
               (0, +5):pg.transform.rotozoom(pg.image.load("ex02/fig/3.png"), +90, 1.0),
               (+5, 0):pg.transform.flip(pg.image.load("ex02/fig/3.png"), True, False),
               (+5, -5):pg.transform.rotozoom(pg.transform.flip(pg.image.load("ex02/fig/3.png"), True, False), +45, 1.0),
               (+5, +5):pg.transform.rotozoom(pg.transform.flip(pg.image.load("ex02/fig/3.png"), True, False), -45, 1.0),
               (0, -5):pg.transform.rotozoom(pg.transform.flip(pg.image.load("ex02/fig/3.png"), True, False), +90, 1.0),
               (0, 0):pg.image.load("ex02/fig/3.png"), 
               }
    accs = [a for a in range(1, 11)]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        key_lst = pg.key.get_pressed()
        合計移動量 = [0, 0]
        if key_lst[pg.K_UP]: 合計移動量[1] -= 5
        if key_lst[pg.K_DOWN]: 合計移動量[1] += 5
        if key_lst[pg.K_LEFT]: 合計移動量[0] -= 5 
        if key_lst[pg.K_RIGHT]: 合計移動量[0] += 5
        kk_img = img_dct[tuple(合計移動量)]
        kk_img_rct.move_ip(合計移動量)
        kk_img_rct_bool = hantei(kk_img_rct)
        kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
        if not kk_img_rct_bool[0]:
            kk_img_rct[0] = 0
        if not kk_img_rct_bool[1]:
            kk_img_rct[0] = 1600-kk_img_rct[3]
        if not kk_img_rct_bool[2]:
            kk_img_rct[1] = 0
        if not kk_img_rct_bool[3]:
            kk_img_rct[1] = 900-kk_img_rct[3]
        bakudan_rct_bool = hantei(bakudan_rct)
        if not bakudan_rct_bool[0]:
            vx = -vx
        if not bakudan_rct_bool[1]:
            vx = -vx
        if not bakudan_rct_bool[2]:
            vy = -vy
        if not bakudan_rct_bool[3]:
            vy = -vy
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        bakudan_rct.move_ip((avx, avy))
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_img_rct)
        screen.blit(enn, bakudan_rct)
        if kk_img_rct.colliderect(bakudan_rct):
            return

        pg.display.update()   
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()