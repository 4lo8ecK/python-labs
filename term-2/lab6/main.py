from PIL import Image, ImageDraw

IMG_WIDTH = 854
IMG_HEIGHT = 480

# Создание неба
img = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), (215, 235, 250))

draw = ImageDraw.Draw(img)


HORIZON = 200
# горы
m1 = [(-50, HORIZON), (70, 150), (240, HORIZON)]
m2 = [(200, HORIZON), (360, 130), (523, HORIZON)]
m3 = [(360, HORIZON), (600, 175), (780, HORIZON)]
m4 = [(200, HORIZON), (360, 130), (523, HORIZON)]

draw.polygon(m1, fill="white")
draw.polygon(m2, fill="white")
draw.polygon(m3, fill="white")


img.save('./tst.png', 'PNG')