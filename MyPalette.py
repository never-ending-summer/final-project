import random
from PIL import Image, ImageFont, ImageDraw

def main():
    colors = [generate_random_color() for _ in range(5)]
    create_image_palette(colors)
    print("Image Save Complete! Look for 'color_palette.png'")

def generate_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0, 255))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def create_image_palette(colors):
    width = 1280
    height = 720
    block_width = width // len(colors)

    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    for i, color in enumerate(colors):
        draw.rectangle([(i * block_width, 0), ((i + 1) * block_width - 1, height)], fill=color)

        hex_code = rgb_to_hex(color)
        text_position = (i * block_width + 10, height - 30)
        draw.text(text_position, hex_code, fill = (0, 0, 0), font=font)

    image.save("color_palette.png")

if __name__ == "__main__":
    main()