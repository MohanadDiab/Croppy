from PIL import Image, ImageDraw
import numpy as np

def create_star_mask(width, height, center=None, outer_radius=None, inner_radius=None, num_points=5):
    """Create a mask for a star with the specified number of points."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not center:
        center = (width // 2, height // 2)
    if not outer_radius:
        outer_radius = min(width, height) * 0.4
    if not inner_radius:
        inner_radius = outer_radius * 0.5
    vertices = []
    for i in range(num_points):
        angle = 2 * np.pi * i / num_points
        x = center[0] + outer_radius * np.sin(angle)
        y = center[1] - outer_radius * np.cos(angle)
        vertices.append((x, y))
        angle = 2 * np.pi * (i + 0.5) / num_points
        x = center[0] + inner_radius * np.sin(angle)
        y = center[1] - inner_radius * np.cos(angle)
        vertices.append((x, y))
    draw.polygon(vertices, fill=1)
    return mask