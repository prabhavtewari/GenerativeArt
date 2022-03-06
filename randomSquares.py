import random
from datetime import datetime
from PIL import Image, ImageDraw


run_id = datetime.timestamp(datetime.now())
print('Run ID : '+str(run_id))
image = Image.new('RGB', (2000, 2000))
width, height = image.size

dim = 100
numberOfSquares = random.randint(5, 400)

drawImage = ImageDraw.Draw(image)
for i in range(0, numberOfSquares):
    x = random.randint(0, width)
    y = random.randint(0, height)
    squareShape = [
        (x, y), (x+dim, y+dim)
    ]
    drawImage.rectangle(squareShape, fill=(
        255, random.randint(0, 255), random.randint(0, 255)))

image.save(f'./output/rand-squares-{run_id}.png')