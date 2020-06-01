from PIL import Image

image = Image.open("a_screenshot.png")

image.show()

print(f'Format: {image.format}, Size: {image.size}, Mode: {image.mode}')

new_image = Image.new('RGB', (500, 548))

pixels = image.load()
for y in range(548):
    for x in range(500):
        # pixels[x, y] = (x, y, 255)
        # print(f'x:{x}, y:{y}, RGB:{pixels[x, y]}')
        new_colour = ((pixels[x, y][0] + pixels[x, y][1] + pixels[x, y][2]) / 3)
        new_colour = int(new_colour)
        pixels[x, y] = (new_colour, new_colour, new_colour)

pixels_two = new_image.load()
for y in range(548):
    for x in range(500):
        pixels_two[x,y] = pixels[x,y]


new_image.show()
