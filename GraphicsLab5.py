from ComputerGraphics.ComputerGraphics.GraphicsLab3 import *
"""
    Паралелепіпед.
    Метод інтерполяції: метод найменших квадратів.
    Метод видалення невидимих ліній та поверхонь:
    алгоритм плаваючого обрію.

"""


class VectorParallelepiped(Parallelepiped):

    def __init__(self):
        super().__init__()

    def draw(self, matrix, dye, random_colors):

        def setPixel(color="red", width=1):
            """ Ставить пікселі """
            return lambda x, y: self.canvas.create_rectangle(x, y, x + width, y + width,
                                                             fill=color, outline=color)

        # ------------------------- алгоритм Брезенхема + MNK ----------------------------------
        def MNK(x1, y1, x2, y2, func):
            """
            :param x1:
            :param y1:
            :param x2:
            :param y2:
            :param func: функція для обробки точки
            :return:
            """
            # -------- алгоритм Брезенхема для визначення параметрів матриць MNK ----------------
            dx = x2 - x1
            dy = y2 - y1
            sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
            sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
            if dx < 0:
                dx = -dx
            if dy < 0:
                dy = -dy
            if dx > dy:
                pdx, pdy = sign_x, 0
                es, el = dy, dx
            else:
                pdx, pdy = 0, sign_y
                es, el = dx, dy
            x, y = x1, y1
            error, t = el / 2, 0

            func(x, y)
            # todo check
            # obj = Point(x, y)
            # obj.setFill('orange')
            # obj.draw(win)

            while t < el:
                error -= es
                if error < 0:
                    error += el
                    x += sign_x
                    y += sign_y
                else:
                    x += pdx
                    y += pdy
                t += 1
                func(x, y)
                # todo check
                # obj = Point(x, y)
                # obj.setFill('orange')
                # obj.draw(win)
            # -------- оголошення нульового та одиничного МНК масивів ------------------
            stopt = t
            # print(stopt)
            Yin = np.zeros((stopt, 1))
            F = np.ones((stopt, 2))
            FX = np.ones((stopt, 2))

            # print('Fvx=', F)
            # print('Yivx=', Yin)
            # -------- алгоритм Брезенхема для заповнення  матриць MNK ------------------
            dx = x2 - x1
            dy = y2 - y1
            sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
            sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
            if dx < 0: dx = -dx
            if dy < 0: dy = -dy
            if dx > dy:
                pdx, pdy = sign_x, 0
                es, el = dy, dx
            else:
                pdx, pdy = 0, sign_y
                es, el = dx, dy
            x, y = x1, y1
            error, t = el / 2, 0

            func(x, y)
            # todo check
            # obj = Point(x, y)
            # obj.setFill('orange')
            # obj.draw(win)
            while t < el:
                error -= es
                if error < 0:
                    error += el
                    x += sign_x
                    y += sign_y
                else:
                    x += pdx
                    y += pdy
                t += 1
                func(x, y)
                # todo check
                # obj = Point(x, y)
                # ---------------------- формування матриці F - MNK ----------------------------------
                #             tt = t
                tt = t - 1
                # print('tt=', tt)
                Yin[tt, 0] = float(y)
                F[tt, 1] = float(x)
                FX[tt, 1] = float(x)
                # todo
                # obj.setFill('orange')
                # obj.draw(win)
            # ----------------- корегування матрицы F для випадку координат констант ---------------
            for i in range(0, stopt):
                F[i, 1] = i
            # ------------------------------- алгоритм - MNK --------------------------------------
            FT = F.T
            FFT = FT.dot(F)
            FFTI = np.linalg.inv(FFT)
            FFTIFT = FFTI.dot(FT)
            C = FFTIFT.dot(Yin)
            Yout = F.dot(C)
            # ----------------------- контроль обчислень алгоритма - MNK --------------------------
            # print('F=', F)
            # print('Yin=', Yin)
            # print('FT=', FT)
            # print('FFT=', FFT)
            # print('FFTI=', FFTI)
            # print('FFTIFT=', FFTIFT)
            # print('C=', C)
            # print('Yout=', Yout, 'Yin=', Yin)
            # print('Yin=', Yin)
            # -------------------- побудова ліній за координатами МНК ---------------------------------

            for i in range(0, stopt):
                XMNK = FX[i, 1]
                YMNK = Yout[i, 0]
                func(x, y)
                # todo check
                # obj = Point(XMNK, YMNK)
                # obj.setFill('violet')
                # obj.draw(win)
            return MNK

        def draw_polygon(*point, contour_color="black", fill_color="red"):
            """
            Функція дидаляє невидимі лінії та малює фігуру
            :param point:
            :param contour_color:
            :param fill_color:
            :return:
            """

            # зафарбовуємо область
            self.canvas.create_polygon(*point, fill=fill_color, outline=fill_color)
            # малюємо контур
            for i in range(-1, len(point) - 1):
                MNK(*point[i], *point[i + 1], setPixel(color=contour_color))

        # запам'ятовуємо час початку обрахунків
        star_time = time.time()
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, 800, 800, fill="#6e6e6e")
        # округлюємо всі координати
        matrix = tuple(map(lambda item: tuple(map(int, item)), matrix))

        # малюємо бічні грані
        draw_polygon(matrix[3], (matrix[3][0], matrix[3][1] + 100),
                     (matrix[2][0], matrix[2][1] + 100), matrix[2],
                     contour_color=dye, fill_color=random_colors[0])
        draw_polygon(matrix[2], (matrix[2][0], matrix[2][1] + 100),
                     (matrix[1][0], matrix[1][1] + 100), matrix[1],
                     contour_color=dye, fill_color=random_colors[1])
        draw_polygon(matrix[3], (matrix[3][0], matrix[3][1] + 100),
                     (matrix[0][0], matrix[0][1] + 100), matrix[0],
                     contour_color=dye, fill_color=random_colors[2])
        draw_polygon(matrix[0], (matrix[0][0], matrix[0][1] + 100),
                     (matrix[1][0], matrix[1][1] + 100), matrix[1],
                     contour_color=dye, fill_color=random_colors[3])

        # малюєм контур верхньої грані
        draw_polygon(*matrix, contour_color=dye, fill_color=random_colors[4])

        while (time.time() - star_time) < 0.2:
            pass
        root.update()
        return self


odj = VectorParallelepiped()
odj.ran()
