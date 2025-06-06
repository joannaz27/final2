import pygame as pg

class Bob:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pg.image.load("images/bob.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pg.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 1.1, self.image_size[1] * 1.1)
        self.image = pg.transform.scale(self.image, scale_size)


