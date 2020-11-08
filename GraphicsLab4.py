from ComputerGraphics.ComputerGraphics.GraphicsLab3 import *

"""
Оскільки 4 робота відрізняється від третьої
лише малюванянням зображення, то викорисатаємо
механізми настлідування, та перевизначення
"""


class GrowthParallelepiped(Parallelepiped):

    def __init__(self):
        super().__init__()

    def draw(self, matrix, dye, random_colors):
        """
        Перевизначена функція із попередньої роботи
        точки по яким малюється фігура та кольори для неї
        беруться з попередньої роботи
        """

        def setPixel(color="red", width=1):
            """ Ставить пікселі """
            return lambda x, y: self.canvas.create_rectangle(x, y, x + width, y + width,
                                                             fill=color, outline=color)

        # алгоритм Брезенхейма
        def draw_line(x1, y1, x2, y2, func):
            """
            :param y2:
            :param x2:
            :param y1:
            :param x1:
            :param func: функція яка має приймати координати пікселя
                         і розбираться з ними(наприклад малює його)
            """
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

            func(x, y, )

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
                func(x, y, )
            return self

        def draw_polygon(*point, contour_color="black", fill_color="red"):
            """
            спочатку розрахуємо теоретично точки протилежних ліній
            потім зафарбуємо лініями
            намалюємо контури
            :param fill_color:
            :param contour_color:
            :param point:
            :return:
            """
            list1 = []  # координати пікселів
            list2 = []  # для паралельних прямих
            # записуємо координати
            draw_line(*point[1], *point[2], lambda x, y: list1.append((x, y)))
            draw_line(*point[0], *point[3], lambda x, y: list2.append((x, y)))
            # зафарбовуємо область
            for i in range(min(len(list1), len(list2))):
                draw_line(*list1[i], *list2[i], setPixel(color=fill_color))
            # малюємо контур
            for i in range(-1, len(point) - 1):
                draw_line(*point[i], *point[i + 1], setPixel(color=contour_color))

        # запам'ятовуємо час початку обрахунків
        star_time = time.time()
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, 800, 800, fill="#6e6e6e")
        # округлюємо всі координати
        matrix = tuple(map(lambda item: tuple(map(int, item)), matrix))

        # малюємо бічні грані із заливкою від раста до раста
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

        # малюєм контур верхньої грані із заливкою від раста до раста
        draw_polygon(*matrix, contour_color=dye, fill_color=random_colors[4])

        while (time.time() - star_time) < 0.05:
            pass
        root.update()
        return self


odj = GrowthParallelepiped()
odj.ran()
