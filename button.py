import pygame as pg

pg.init()

height= 1300
width = 800
size = (height, width)
screen = pg.display.set_mode(size)

pg.font.init()
font = pg.font.Font('fonts/handwritten.ttf', 60)



class Button:
    def __init__(self, text, x_pos, y_pos, w, h, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.w = w
        self.h = h
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_text = font.render(self.text, True, 'red')
        button_rect = pg.rect.Rect((self.x_pos, self.y_pos), (self.w, self.h))
        if self.enabled:
            if self.hover():
                pg.draw.rect(screen, 'grey', button_rect, 0, 5)
            else:
                pg.draw.rect(screen, 'white', button_rect, 0, 5)
        else:
            pg.draw.rect(screen, 'black', button_rect, 0, 5)

        pg.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 10, self.y_pos ))

    def check_click(self):
        mouse_pos = pg.mouse.get_pos()
        left_click = pg.mouse.get_pressed()[0]
        button_rect =  pg.rect.Rect((self.x_pos, self.y_pos), (150, 50))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

    def hover(self):
        mouse_pos = pg.mouse.get_pos()
        left_click = pg.mouse.get_pressed()[0]
        button_rect =  pg.rect.Rect((self.x_pos, self.y_pos), (150, 50))
        if button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False