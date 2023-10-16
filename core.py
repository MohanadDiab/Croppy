import numpy as np
from PIL import Image


def apply_mask_with_transparency(image_path, mask, output_path):
    """
       Apply a given mask to an image and save the result with transparency.

       Parameters:
           - image_or_path: PIL.Image.Image object or path to the image
           - mask: Mask to be applied
           - output_path: Path where the result should be saved

       Returns:
           - PIL.Image.Image: Resulting image after applying the mask
       """
    if isinstance(image_path, str):
        # If it's a path, load the image
        image = Image.open(image_path).convert("RGBA")
    else:
        # Assume it's an Image object
        image = image_path.convert("RGBA")

    datas = image.getdata()

    new_data = []
    for item, mask_value in zip(datas, mask.getdata()):
        # Change all white (also shades of whites)
        # pixels to be transparent
        if mask_value == 0:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    image.putdata(new_data)
    image.save(output_path, "PNG")
    return image
