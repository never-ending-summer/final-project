import random
from PIL import Image, ImageFont, ImageDraw

def main():
    colors = [generate_random_color() for _ in range(5)]
    create_image_palette(colors)
    print("Image Save Complete! Look for 'color_palette.png'")

def generate_random_color():
    return (random.randit(0,255), random.randit(0,255), random.randit(0, 255))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb)

#define create image function
#creates an image using previously generated information with set height
#return