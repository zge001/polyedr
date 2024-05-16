import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr

from math import pi, sqrt
from shadow.polyedr import Polyedr


class TestGoodVertexes(unittest.TestCase):

    @classmethod
    def setUp(self):
        pass

    # Вспомогательный метод создания полиэдра
    def __create_polyedr(self, fake_file_content, fake_file_path):
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    # Подходящая грань - треугольник с площадью 12.5
    def test_area01(self):
        fake_file_content = """1.0	0.0	0.0	0.0
7	2	7
0.0 0.0 0.0
5.0 0.0 0.0
5.0 5.0 0.0
0.0 5.0 0.0
-5.0 1.0 3.0
0.0 1.0 3.0
-5.0 6.0 3.0
4	1    2    3    4
3	6    5    7"""
        fake_file_path = 'data/two_planes.geom'
        self.__create_polyedr(fake_file_content, fake_file_path)
        self.assertEqual(self.polyedr.good_area, 12.5)

    # Подходящая грань - квадрат с площадью 25.0
    def test_area02(self):
        fake_file_content = """1.0	45.0	0.0	0.0
7	2	7
-3.0 0.0 0.0
2.0 0.0 0.0
2.0 5.0 0.0
-3.0 5.0 0.0
1.0 1.0 3.0
6.0 1.0 3.0
1.0 6.0 3.0
4	1    2    3    4
3	6    5    7"""
        fake_file_path = 'data/two_planes.geom'
        self.__create_polyedr(fake_file_content, fake_file_path)
        self.assertEqual(self.polyedr.good_area, 25.0)

    # Две грани параллелепипеда с площадью 1 и
    # одна грань с площадь корень из двух
    def test_area03(self):
        fake_file_content = """1.0 0.0 0.0 45.0
8 6 24
-3.0 0.0 0.5
-3.0 1.0 0.5
-2.0	1.0	0.5
-2.0	0.0	0.5
-2.0	0.0	-0.5
-2.0	1.0	-0.5
-1.0	1.0	-0.5
-1.0	0.0	-0.5
4	1    2    3    4
4	1    2    6    5
4	2    3    7    6
4	4    3    7    8
4	1    4    8    5
4	5    6    7    8"""
        fake_file_path = 'data/parallelepiped.geom'
        self.__create_polyedr(fake_file_content, fake_file_path)
        self.assertEqual(self.polyedr.good_area, 1.0 + 1.0 + sqrt(2))

    def test_area04(self):
        fake_file_content = """1.0 0.0 40.0 90.0
4 4 12
1.0	2.0	1.0
1.0	0.0 -1.0
-1.0 2.0 -1.0
-1.0 0.0 1.0
3 1 2 3
3 1 2 4
3 1 3 4
3 2 3 4"""
        fake_file_path = 'data/tetrahedron.geom'
        self.__create_polyedr(fake_file_content, fake_file_path)
        self.assertAlmostEqual(self.polyedr.good_area, 4.0 * sqrt(3))

    # Коэффициент гомотетии не влияет на результат
    def test_area05(self):
        fake_file_content = """1000.0 0.0 40.0 90.0
4 4 12
1.0	2.0	1.0
1.0	0.0 -1.0
-1.0 2.0 -1.0
-1.0 0.0 1.0
3 1 2 3
3 1 2 4
3 1 3 4
3 2 3 4"""
        fake_file_path = 'data/tetrahedron.geom'
        self.__create_polyedr(fake_file_content, fake_file_path)
        self.assertAlmostEqual(self.polyedr.good_area, 4.0 * sqrt(3))
