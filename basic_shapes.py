from PIL import Image, ImageDraw

def create_circle_mask(width, height, center=None, radius=None):
    """Create a mask for a circle."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not center:
        center = (width // 2, height // 2)
    if not radius:
        radius = min(width, height) // 2
    leftUpPoint = (center[0] - radius, center[1] - radius)
    rightDownPoint = (center[0] + radius, center[1] + radius)
    draw.ellipse([leftUpPoint, rightDownPoint], fill=1)
    return mask

def create_square_mask(width, height, center=None, side=None):
    """Create a mask for a square."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not center:
        center = (width // 2, height // 2)
    if not side:
        side = min(width, height)
    leftUpPoint = (center[0] - side // 2, center[1] - side // 2)
    rightDownPoint = (center[0] + side // 2, center[1] + side // 2)
    draw.rectangle([leftUpPoint, rightDownPoint], fill=1)
    return mask

def create_rectangle_mask(width, height, center=None, rect_width=None, rect_height=None):
    """Create a mask for a rectangle."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not center:
        center = (width // 2, height // 2)
    if not rect_width:
        rect_width = width
    if not rect_height:
        rect_height = height
    leftUpPoint = (center[0] - rect_width // 2, center[1] - rect_height // 2)
    rightDownPoint = (center[0] + rect_width // 2, center[1] + rect_height // 2)
    draw.rectangle([leftUpPoint, rightDownPoint], fill=1)
    return mask

def create_ellipse_mask(width, height, center=None, hor_radius=None, ver_radius=None):
    """Create a mask for an ellipse."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not center:
        center = (width // 2, height // 2)
    if not hor_radius:
        hor_radius = width // 2
    if not ver_radius:
        ver_radius = height // 2
    leftUpPoint = (center[0] - hor_radius, center[1] - ver_radius)
    rightDownPoint = (center[0] + hor_radius, center[1] + ver_radius)
    draw.ellipse([leftUpPoint, rightDownPoint], fill=1)
    return mask
