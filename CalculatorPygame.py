# Poschanan Thongsri 6001012620033
# My Blog : http://poschanan.blogspot.com/

import pygame
import Button
from Button import *

pygame.init()
pygame.display.Info()

win = pygame.display.set_mode((400,650), pygame.RESIZABLE)  #pygame.RESIZABLE
pygame.display.set_caption('Calculator')
win.fill((255,255,255))
#เป็นการกำหนดหน้าต่างเริ่มต้น

num = []
countnum = 0

while True:
    Button(win).creat_button()   # เรียกclassที่สร้างไว้ออกมาใช้งาน

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # เป็นขั้นตอนของการสั่งปิดการใช้งานcalculator

        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)

        if event.type == pygame.MOUSEBUTTONDOWN:    # เมื่อกดปุ่มจะเข้ามาทำงาน ดังนี้
            if Button(win).numText() == '<--':
                num.pop(-1)
                countnum -= 1
            # การลบเลขออก โดยจะทำการ pop ค่าออกจากในlist
            elif Button(win).numText() == 'C':
                num.clear()
                countnum = 0
            # เป็นการลบตัวเลขที่ใส่เข้าไปทั้งหมด โดยการสั่งclearข้อมูลทั้งหมดที่อยู่ในlist
            elif Button(win).numText() == '=':  # เมื่อกดปุ่มเท่ากับ
                if ')' not in num and '(' in num:
                    num.clear()
                    num.append('ERROR')

                elif '(' not in num and ')' in num:
                    num.clear()
                    num.append('ERROR')

                elif num[-1] == '+' or num[-1] == '-' or num[-1] == '*' or num[-1] == '/':
                    num.clear()
                    num.append('ERROR')

                elif num[-1] == '0' and num[-2] == '/':
                    num.clear()
                    num.append('ERROR')
                    print(num)
                # เป็นการตรวจสอบว่าสมการที่กรอกเข้ามานั้นผิดไหม ถ้าผิดมันจะเข้าไปตาม if elif ข้างบนเเล้วแสดง ERROR

                else:
                    equals = eval(''.join(num))
                    num.clear()
                    num += str(equals)
                    #num.append(str(equals))
                    print(num)
                # ถ้าสมการที่กรอกถูกต้องจะเข้ามาทำงานที่นี่ โดยจะคำนวณโดยใช้ eval() เเล้วทำการลบข้อมูลเดิมออกจากนั้นก็ใส่ข้อมูลใหม่หรือก็คือ คำตอบลงไปแทน

            else:
                if Button(win).numText() in '1234567890.':
                    if 7 > countnum >= 0:
                        num.append(Button(win).numText())
                        print(num)
                        countnum += 1
                        print(countnum)
                else:
                    num.append(Button(win).numText())
                    print(num)
                    countnum = 0
            # เป็นขั้นตอนของการกำหนดให้ตัวเลขมีขอบเขตในการคำนวณ ไม่เกิน 7 ตำแหน่ง


    text1 = pygame.font.SysFont('helvetica', 50).render(''.join(num), True, (255, 255, 255))
    win.blit(text1, (15, 75))
    # เป็นการแสดงตัวเลขขึ้นไปที่หน้าต่างที่สร้างเอาไว้ในตอนต้น

    pygame.display.update()
    
"""
  Test Case
34 + 78 = 112
(22.1 + 15) - 3 = 34.1
543 / 0 = ERROR
92 / = ERROR
(54 * 2) + (42 / 2) = 129.0
(12 + 9  - 45 = ERROR
674 * 53 = 35722
-34 - 45 = -79
39 - (56 * 3) = -129
34 / 2 = 17.0
"""
