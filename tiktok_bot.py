import pyautogui as pg
import time

#Point(x=1048, y=504) หน้าวิดีโอ
#Point(x=627, y=542) กดใจ
#Point(x=1422, y=1000) คอมเม้น
#Point(x=1334, y=556) เลื่อน

for i in range(3):
    pg.moveTo(1048,504)
    pg.click()
    time.sleep(2)
    pg.doubleClick(627,542)
    time.sleep(2)
    pg.click(1422,1000)
    pg.typewrite('Nice!')
    pg.typewrite(['enter'])
    time.sleep(2)
    pg.click(1334,556)



