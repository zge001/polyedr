import unittest
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr

from math import pi, sqrt
from shadow.polyedr import Polyedr


class TestGoodVertexes(unittest.TestCase):

    @classmethod
    def setUp(self):
        pass

    # Подходящая грань - треугольник с площадью 12.5
    def test_area01(self):
        fake_file_content = """40.0	0.0	-20.0	45.0
8	2	8
0.0 0.0 0.0
5.0 0.0 0.0
5.0 5.0 0.0
0.0 5.0 0.0
1.0 1.0 3.0
6.0 1.0 3.0
6.0 6.0 3.0
1.0 6.0 3.0
4	1    2    3    4
3	6    5    8"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)
        self.assertEqual(self.polyedr.good_area, 12.5)

    # Подходящая грань - треугольник с площадью 12.5
    def test_area02(self):
        fake_file_content = """40.0	0.0	-20.0	45.0
8	2	8
0.0 0.0 0.0
5.0 0.0 0.0
5.0 5.0 0.0
0.0 5.0 0.0
1.0 1.0 3.0
6.0 1.0 3.0
6.0 6.0 3.0
1.0 6.0 3.0
4	1    2    3    4
3	6    5    8"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)
        self.assertEqual(self.polyedr.good_area, 12.5)
