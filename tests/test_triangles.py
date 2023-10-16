import unittest
from triangles import create_equilateral_triangle_mask, create_isosceles_triangle_mask, create_right_triangle_mask, \
    create_scalene_triangle_mask


class TestTriangles(unittest.TestCase):

    def test_create_equilateral_triangle_mask(self):
        width, height = 100, 100
        mask = create_equilateral_triangle_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions can be added to check the shape of the triangle

    def test_create_isosceles_triangle_mask(self):
        width, height = 100, 100
        mask = create_isosceles_triangle_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions to check the shape of the triangle

    def test_create_right_triangle_mask(self):
        width, height = 100, 150
        mask = create_right_triangle_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions to check the shape of the triangle

    def test_create_scalene_triangle_mask(self):
        width, height = 100, 150
        mask = create_scalene_triangle_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions to check the shape of the triangle


if __name__ == '__main__':
    unittest.main()
