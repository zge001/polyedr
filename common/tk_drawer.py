from tkinter import *
from common.r3 import R3

# Размер окна
SIZE = 900
# Коэффициент гомотетии
SCALE = 1.5


def x(p, homothety):  # pragma: no cover
    """ преобразование x-координаты """
    return SIZE / 2 + SCALE * homothety * p.x


def y(p, homothety):  # pragma: no cover
    """" преобразование y-координаты """
    return SIZE / 2 - SCALE * homothety * p.y


class TkDrawer:  # pragma: no cover
    """ Графический интерфейс """

    # Конструктор
    def __init__(self, homothety=1.0):
        self.root = Tk()
        self.root.title("Изображение проекции полиэдра")
        self.root.geometry(f"{SIZE+5}x{SIZE+5}")
        self.root.resizable(False, False)
        self.root.bind('<Control-c>', quit)
        self.canvas = Canvas(self.root, width=SIZE, height=SIZE)
        self.canvas.pack(padx=5, pady=5)
        self.homothety = homothety

    # Завершение работы
    def close(self):
        self.root.quit()

    # Стирание существующей картинки
    def clean(self):
        self.canvas.create_rectangle(0, 0, SIZE, SIZE, fill="white")
        # Рисуем прямую x = -2
        self.draw_line(R3(-2.0, SIZE, 0.0), R3(-2.0, -SIZE, 0.0),
                       self.homothety, color="red")

    # Рисование линии
    def draw_line(self, p, q, homothety=1.0, color="black"):
        self.canvas.create_line(x(p, homothety), y(p, homothety),
                                x(q, homothety), y(q, homothety),
                                fill=color, width=1)
        self.root.update()


if __name__ == "__main__":  # pragma: no cover

    import time
    tk = TkDrawer()
    tk.clean()
    tk.draw_line(R3(0.0, 0.0, 0.0), R3(100.0, 100.0, 0.0))
    tk.draw_line(R3(0.0, 0.0, 0.0), R3(0.0, 100.0, 0.0))
    time.sleep(5)
