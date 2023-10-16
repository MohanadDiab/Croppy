from PIL import Image, ImageDraw
import numpy as np


def create_equilateral_triangle_mask(width, height, center=None, side=None):
    """Create a mask for an equilateral triangle."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not center:
        center = (width // 2, height // 2)
    if not side:
        side = min(width, height)
    height_triangle = (side * (3 ** 0.5)) / 2
    point1 = (center[0], center[1] - height_triangle / 2)
    point2 = (center[0] - side / 2, center[1] + height_triangle / 2)
    point3 = (center[0] + side / 2, center[1] + height_triangle / 2)
    draw.polygon([point1, point2, point3], fill=1)
    return mask


def create_isosceles_triangle_mask(width, height, center=None, base=None, triangle_height=None):
    """Create a mask for an isosceles triangle."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not center:
        center = (width // 2, height // 2)
    if not base:
        base = width * 0.7
    if not triangle_height:
        triangle_height = height * 0.7
    point1 = (center[0], center[1] - triangle_height / 2)
    point2 = (center[0] - base / 2, center[1] + triangle_height / 2)
    point3 = (center[0] + base / 2, center[1] + triangle_height / 2)
    draw.polygon([point1, point2, point3], fill=1)
    return mask


def create_right_triangle_mask(width, height, center=None, base=None, triangle_height=None):
    """Create a mask for a right-angled triangle."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not center:
        center = (width // 2, height // 2)
    if not base:
        base = width * 0.7
    if not triangle_height:
        triangle_height = height * 0.7
    point1 = (center[0] - base / 2, center[1])
    point2 = (center[0] + base / 2, center[1])
    point3 = (center[0], center[1] - triangle_height)
    draw.polygon([point1, point2, point3], fill=1)
    return mask


def create_scalene_triangle_mask(width, height, vertices=None):
    """Create a mask for a scalene triangle."""
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    if not vertices:
        point1 = (width * 0.25, height * 0.2)
        point2 = (width * 0.75, height * 0.4)
        point3 = (width * 0.5, height * 0.9)
        vertices = [point1, point2, point3]
    draw.polygon(vertices, fill=1)
    return mask
