from tkinter import *
import numpy as np
from math import cos, sin
import time


def sleep():
    root.update_idletasks()
    root.update()
    time.sleep(0.1)


class Diamond1(Canvas):

    def __init__(self):
        super().__init__()
        self.master.title("Увіііі!!!")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.matrix = np.array([[400, 300],  # task 1
                                [450, 400],
                                [400, 500],
                                [350, 400]])
        self.canvas.pack(fill=BOTH, expand=1)

    @sleep
    def draw(self):  # task 1
        self.canvas.create_rectangle(0, 0, 800, 800,
                                     fill="#6e6e6e")
        coordinates = []
        tuple(map(lambda x: coordinates.extend(map(round, *x.tolist())), self.matrix))
        self.canvas.create_polygon(*coordinates,
                                   outline='#d1d100',
                                   fill='#ffff00', width=5
                                   )
        return self

    def scale(self, coefficient):  # task 1
        self.matrix = self.matrix.dot(np.diag([coefficient] * 2))
        return self

    def turn(self, angle):  # task 1
        self.matrix = self.matrix.dot([[cos(angle), sin(angle)],
                                       [-sin(angle), cos(angle)]])
        return self

    def move(self, x=0.0, y=0.0):  # task 1
        self.matrix = self.matrix + np.array([[x, y]] * 4)
        return self


class Diamond2(Diamond1):

    def __init__(self):
        super().__init__()
        self.matrix = tuple(np.array(i) for i in self.matrix)

    def scale(self, coefficient):  # task 2
        self.matrix = tuple(map(lambda x: x.dot(np.diag([coefficient] * 2)), self.matrix))
        return self

    def turn(self, angle):  # task 2
        self.matrix = tuple(map(lambda x: x.dot([[cos(angle), sin(angle)],
                                                 [-sin(angle), cos(angle)]]), self.matrix))
        return self

    def move(self, x=0.0, y=0.0):  # task 2
        self.matrix = tuple(map(lambda item: item + np.array([[x, y]]), self.matrix))
        return self


class Diamond3(Diamond2):

    def __init__(self):
        super().__init__()

    def scale(self, coefficient):  # task 3
        self.matrix = tuple(map(lambda x: x.dot(np.diag([coefficient] * 2)), self.matrix))
        return self

    def turn(self, angle):  # task 3
        self.matrix = tuple(map(lambda x: x.dot([[cos(angle), sin(angle)],
                                                 [-sin(angle), cos(angle)]]), self.matrix))
        return self

    def move(self, x=0.0, y=0.0):  # task 3
        self.matrix = tuple(map(lambda item: item + np.array([[x, y]]), self.matrix))
        return self


def test(obj):
    while 1:
        for i in range(5):
            obj.turn(50).scale(1.2).move(x=-185, y=70).draw()
        for i in range(5):
            obj.turn(50).scale(0.834).move(x=-20, y=180).draw()
        obj.matrix = np.array([[400, 300],   # зброс до завоцьких
                               [450, 400],
                               [400, 500],
                               [350, 400]])


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x800")
    diamond1 = Diamond1()
    # diamond2 = Diamond2()
    # diamond3 = Diamond3()
    test(diamond1)
    # test(diamond2)
    # print(diamond2.draw())
