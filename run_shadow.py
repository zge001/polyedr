#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    # for name in ["ccc", "cube", "box", "king", "cow"]:
    for name in ["tetrahedron"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        polyedr = Polyedr(f"data/{name}.geom")
        polyedr.draw(tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        print(f"Суммарная площадь граней ровно с одной хорошей точкой: \
            {polyedr.good_area}")

        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
