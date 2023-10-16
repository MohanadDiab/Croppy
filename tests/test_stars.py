import unittest
from stars import create_star_mask


class TestStars(unittest.TestCase):

    def test_create_star_mask(self):
        width, height = 100, 100
        mask = create_star_mask(width, height)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions can be added to check the shape of the star

    def test_create_star_mask_custom_points(self):
        width, height = 100, 100
        mask = create_star_mask(width, height, num_points=6)
        self.assertEqual(mask.size, (width, height))
        # Additional assertions to check the shape of the star with custom points


if __name__ == '__main__':
    unittest.main()
