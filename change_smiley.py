from PIL import Image
import numpy as np
#open the file smiley.bmp
im = Image.open('images/smiley.bmp')
#convert the image into a numpy array
a = np.asarray(im)
#convert the numpy array back into an image
im = Image.fromarray(a)
#save the image as a different file
im.save('images/smiley2.bmp')