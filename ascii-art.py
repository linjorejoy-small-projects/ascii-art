# Import Libraries
from PIL import Image, ImageOps
import numpy as np
import math


# Constants
ASCII_IMAGE_WIDTH = 150
PIXEL_ARRAY = ["#","@","O","=","+","o","^","*","!","."]
LENGTH = len(PIXEL_ARRAY)
RANGE = 255/LENGTH


def get_image_pixels():

    # location = input('Enter the Absolute or Relative location')
    location = "G:\Home\My Photos\potrait.jpg"
    imgArray = np.asarray(ImageOps.grayscale(Image.open(location)))
    # print(imgArray)
    return imgArray


def listToString(s):  

    str1 = ""  
    for ele in s:  
        str1 += str(ele)   
    return str1  


def appendToFile(fileName, array):

    str = listToString(array)
    with open(fileName,'a') as file:
        file.write(str)


def get_symbol(value):
    if((value-5) == 0):
        return PIXEL_ARRAY[0]
    return str(PIXEL_ARRAY[(value-6)//math.floor(RANGE)])


def main():

    pixeValues = get_image_pixels()
    height = math.floor(pixeValues.shape[0]*ASCII_IMAGE_WIDTH/pixeValues.shape[1])
    symbolArray = np.empty((height, ASCII_IMAGE_WIDTH), dtype='S')

    for i in range(height):
        for j in range(ASCII_IMAGE_WIDTH):
            yPos = math.floor(i*pixeValues.shape[0]/height)
            xPos = math.floor(j*pixeValues.shape[1]/ASCII_IMAGE_WIDTH)
            symbolArray[i,j] = get_symbol(pixeValues[yPos, xPos])
    print(symbolArray.shape)

    for i in range(height):
        appendToFile("ascii-art.txt", symbolArray[i].tolist())

# pixeValues = get_image_pixels()
# print(pixeValues[792,700])
main()