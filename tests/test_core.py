import unittest
from PIL import Image
from core import apply_mask_with_transparency
from basic_shapes import create_circle_mask
import os


class TestCore(unittest.TestCase):

    def test_apply_mask_with_transparency(self):
        img = Image.new('RGB', (100, 100), (255, 0, 0))  # Create a red image
        mask = create_circle_mask(100, 100)
        output_path = 'temp_output.png'
        output_img = apply_mask_with_transparency(img, mask, output_path)
        if os.path.exists(output_path):
            os.remove(output_path)

        # Check if the output image size matches the input
        self.assertEqual(output_img.size, img.size)

        # Check if the output image has an alpha channel (transparency)
        self.assertEqual(output_img.mode, 'RGBA')

        # Additional assertions can be added to check the transparency and content of the resulting image


if __name__ == '__main__':
    unittest.main()