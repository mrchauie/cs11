from PIL import Image
import numpy as np
#open the file smiley.bmp
im = Image.open('images/smiley.bmp')
#convert the image into a numpy array

def equateArray(arr1,arr2):
    if len(arr1) == len(arr2):
        for index in range(0,len(arr2)):
            if arr1[index] != arr2[index]:
                return False
        return True
    return False

a = np.asarray(im)
""" for x in range(0,len(a)):
    for color in range(0,len(a[0])):
        if equateArray(a[x][color],np.asarray([255,0,0])):
            print("pass")
            a[x][color][0] = 0
            a[x][color][2] = 255
            print(color) """
for x in a:
    for color in x:
        if equateArray(color,np.asarray([255,0,0])):
            color = np.asarray([0,0,255])
#convert the numpy array back into an image
im = Image.fromarray(a)
#save the image as a different file
im.save('images/smiley2.bmp')
