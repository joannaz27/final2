import pygame as pg

class Bobby:
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.image = pg.image.load("images/bobby.png")
        self.image_size = self.image.get_size()
        self.rescale_image(self.image)
        self.rect = pg.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 1.3, self.image_size[1] * 1.3)
        self.image = pg.transform.scale(self.image, scale_size)

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        self.rect = pg.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left":
            self.x = self.x - self.delta
        self.rect = pg.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up":
            self.y = self.y - self.delta
        self.rect =pg.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pg.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
