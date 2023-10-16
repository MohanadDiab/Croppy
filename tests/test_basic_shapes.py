import unittest
from basic_shapes import create_circle_mask, create_square_mask, create_rectangle_mask, create_ellipse_mask

class TestBasicShapes(unittest.TestCase):

    def test_create_circle_mask(self):
        width, height = 100, 100
        mask = create_circle_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions can be added to check the shape of the circle

    def test_create_square_mask(self):
        width, height = 100, 100
        mask = create_square_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions to check the shape of the square

    def test_create_rectangle_mask(self):
        width, height = 100, 150
        mask = create_rectangle_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions to check the shape of the rectangle

    def test_create_ellipse_mask(self):
        width, height = 100, 150
        mask = create_ellipse_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions to check the shape of the ellipse

if __name__ == '__main__':
    unittest.main()
