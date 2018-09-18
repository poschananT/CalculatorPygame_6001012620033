# Poschanan Thongsri 6001012620033
# My Blog : http://poschanan.blogspot.com/

import pygame
import Button
from Button import *

pygame.init()
pygame.display.Info()

win = pygame.display.set_mode((400,650), pygame.RESIZABLE)
pygame.display.set_caption('Calculator')
win.fill((255,255,255))
# set window beginning such as caption, color of background

num = []
countnum = 0

while True:
    Button(win).creat_button()   # class button created

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # close Calculator

        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)

        if event.type == pygame.MOUSEBUTTONDOWN:    # when you click
            if Button(win).numText() == '<--':
                num.pop(-1)
                countnum -= 1
            # delete number by .pop()
            elif Button(win).numText() == 'C':
                num.clear()
                countnum = 0
            # delete all number in list by .clear()
            elif Button(win).numText() == '=':  # when you click button " = "
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
                # check the input equation if equation is false Calculator will show 'ERROR'

                else:
                    equals = eval(''.join(num))
                    num.clear()
                    num += str(equals)
                    #num.append(str(equals))
                    print(num)
                # use eval() calculate equation

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
            # scope the input number in equation


    text1 = pygame.font.SysFont('helvetica', 50).render(''.join(num), True, (255, 255, 255))
    win.blit(text1, (15, 75))
    # show number at window beginning

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
