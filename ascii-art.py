# Import Libraries
from PIL import Image, ImageOps
import numpy as np
import math

# Constants
ASCII_IMAGE_WIDTH = 150
PIXEL_ARRAY = ["#","@","O","=","+","o","^","*","!","."]
LENGTH = len(PIXEL_ARRAY)
RANGE = 255/LENGTH


def get_image():

    # location = input('Enter the Absolute or Relative location')
    location = "G:\Home\My Photos\potrait.jpg"
    imgArray = np.asarray(ImageOps.grayscale(Image.open(location)))
    print(imgArray)
    return imgArray


def listToString(s):  

    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  


def appendToFile(fileName, array):

    str = listToString(array)
    with open(fileName,'a') as file:
        file.write(str)


def get_symbol(value):
    
    return PIXEL_ARRAY[math.floor(value/RANGE)]

get_image()