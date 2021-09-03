from PIL import Image
import numpy as np

#define constants for readibility
RED = 0
GREEN = 1
BLUE = 2

#open the file smiley.bmp
im = Image.open('images/smiley.bmp')
#convert the image into a numpy array
a = np.asarray(im)

width = len(a)
height = len(a[0])
print(f'width:{width} height:{height}')


for w in range(width):
    for h in range(height):
        if a[w][h][RED] == 255 and a[w][h][GREEN] == 0 and a[w][h][BLUE] == 0:
            a[w][h][RED] = 0
            a[w][h][BLUE] = 255

#convert the numpy array back into an image
im = Image.fromarray(a)
#save the image as a different file
im.save('images/smiley2.bmp')