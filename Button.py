# Poschanan Thongsri 6001012620033
# My Blog : http://poschanan.blogspot.com/
# referent : https://pythonprogramming.net/placing-text-pygame-buttons/?completed=/making-interactive-pygame-buttons/


class Button():
    black = (0, 0, 0)
    red = (255, 0, 0)
    gray = (130, 130, 130)

    button = {'.': [0, 550, black], '0': [100, 550, black], '1': [0, 450, black], '2': [100, 450, black],
              '3': [200, 450, black], '4': [0, 350, black], '5': [100, 350, black], '6': [200, 350, black],
              '7': [0, 250, black], '8': [100, 250, black], '9': [200, 250, black],
              'C': [0, 150, gray], '<--': [100, 150, gray],
              '+': [300, 350, red], '-': [300, 250, red], '*': [300, 150, red], '/': [200, 150, red],
              '=': [300, 450, red], '(': [200, 550, red], ')': [300, 550, red]}
    # เป็นการกำหนดค่าของตัวอักษรในเเต่ละปุ่ม

    def __init__(self, Surface):
        self.Surface = Surface
        self.creat_button()
        self.numText()

    def creat_button(self):
        import pygame
        pygame.init()
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.Surface, (0, 0, 0), [0, 0, 400, 150])

        for i in Button.button:
            if pygame.mouse.get_pressed()[0] == 1:  # เมื่อกดปุ่ม
                if Button.button[i][0] + 100 > pos[0] > Button.button[i][0] and Button.button[i][1] + 100 > pos[1] > Button.button[i][1]:     # ใส่ค่า x,y เพื่อให้มันนำไปเปรียบเทียบ (ซึ่งถูกกรอกไว้แล้วในตอนต้น) เพื่อใช้ในการวาดรูปสี่เหลี่ยมที่ใช้ใน button ให้ปุ่มเปลี่ยนสี
                    pygame.draw.rect(self.Surface, (51, 51, 255), [Button.button[i][0],Button.button[i][1],100,100])
                    text = pygame.font.SysFont('helvetica', 40).render(i, True, (255, 255, 255))
                    self.Surface.blit(text, (Button.button[i][0] + (100 / 2.5), Button.button[i][1] + (100 / 4)))

                    pygame.mixer.music.load("button_click_01.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(1)
                    # เป็นการใส่เสียงเมื่อกดปุ่มลงไป

            else:
                pygame.draw.rect(self.Surface, Button.button[i][2], [Button.button[i][0], Button.button[i][1], 100, 100])
                text = pygame.font.SysFont('helvetica', 40).render(i, True, (255, 255, 255))
                self.Surface.blit(text, ((Button.button[i][0] + (100 / 2.5)), (Button.button[i][1] + (100 / 4))))
            # else นี้เป็นการวาดปุ่มตามค่าที่ใส่เข้ามา

    def numText(self):
        import pygame
        pos = pygame.mouse.get_pos()

        for i in Button.button:
            if pygame.mouse.get_pressed()[0] == 1:
                if Button.button[i][0] + 100 > pos[0] > Button.button[i][0] and Button.button[i][1] + 100 > pos[1] > Button.button[i][1]:
                    return i
        # เป็นการนำค่าของแต่ละปุ่มออกไปใช้งาน