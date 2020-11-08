from tkinter import *
import numpy as np
import random
from math import cos, sin, radians
import time

root = Tk()
root.geometry("800x800")


def sleep(method):
    def wait(self, matrix, hue):
        root.update()
        time.sleep(0.02)
        return method(self, matrix, hue)

    return wait


class Parallelepiped(Canvas):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.master.title("Увіііі!!!")
        self.pack(fill=BOTH, expand=1)
        # параметри паралелепіпеда
        self.a = 150  # довжина сторини
        a = self.a
        self.o = (300, 300, 400)  # початкова точка
        self.matrix = np.array([[self.o[0], self.o[1], self.o[2], 1],
                                [self.o[0] - a, self.o[1], self.o[2], 1],
                                [self.o[0] - a, self.o[1] - a, self.o[2], 1],
                                [self.o[0], self.o[1] - a, self.o[2], 1],
                                [self.o[0], self.o[1], self.o[2] - a, 1],
                                [self.o[0] - a, self.o[1], self.o[2] - a, 1],
                                [self.o[0] - a, self.o[1] - a, self.o[2] - a, 1],
                                [self.o[0], self.o[1] - a, self.o[2] - a, 1],
                                ])
        self.canvas.pack(fill=BOTH, expand=1)

    @sleep
    def draw(self, matrix, dye, random_colors):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, 800, 800, fill="#6e6e6e")
        # малюєм верхній паралелограм
        self.canvas.create_polygon(tuple(map(lambda cor: (cor[0], cor[1]), matrix)),
                                   outline=dye,
                                   fill='#6e6e6e', width=7)
        # малюємо нижній паралелограм
        self.canvas.create_polygon(tuple(map(lambda cor: (cor[0], cor[1] - 100), matrix)),
                                   outline=dye,
                                   fill='#6e6e6e', width=7)
        # малюємо ребра
        for item in matrix:
            self.canvas.create_polygon(item[0], item[1], item[0], item[1] - 100,
                                       outline=dye,
                                       fill='#ffff00', width=7)
        return self

    def projection(self):
        return self.matrix \
            .dot([[cos(120), 0, -sin(120), 0],
                  [0, 1, 0, 0],
                  [sin(120), 0, cos(120), 0],
                  [0, 0, 0, 0]]) \
            .dot([[1, 0, 0, 0],
                  [0, cos(120), sin(120), 0],
                  [0, -sin(120), cos(120), 0],
                  [0, 0, 0, 0]])

    def turn(self, point, hue):
        def forX(angle):
            return self.a * cos(radians(angle)) + point[0]

        def forY(angle):
            return (self.a * sin(radians(angle)) + point[1]) * cos(radians(80))

        r = lambda: random.randint(0, 255)
        random_colors = tuple(('#%02X%02X%02X' % (r(), r(), r())) for i in range(6))
        for i in range(0, 120, 10):
            self.draw([(forX(i + j), forY(i + j)) for j in range(0, 271, 90)], hue,
                      random_colors)
        return self

    def ran(self):
        while 1:
            color = iter(("#732bf0", "#2becf0", "#A4C639", "#fc884e", "#CD00CD"))
            self.turn((400, 2300), next(color))
            self.turn((200, 800), next(color))
            self.turn((600, 800), next(color))
            self.turn((600, 3800), next(color))
            self.turn((200, 3800), next(color))


if __name__ == '__main__':
    obj = Parallelepiped()
    obj.ran()
