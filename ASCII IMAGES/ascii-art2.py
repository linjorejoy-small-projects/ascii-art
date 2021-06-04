# Import Libraries
from PIL import Image
import numpy as np

# Constants
ASCII_IMAGE_WIDTH = 512
#PIXEL_ARRAY = ["\U0001f926","\U0001f44b","\U0001f648","\U0001f602","\U0001f44d"]
PIXEL_ARRAY = ["M","H","O","J","a","o","i"," "]
#PIXEL_ARRAY = ["#","@","O","=","+","o","^","*","!","."]
LENGTH = len(PIXEL_ARRAY)
RANGE = int(255/(LENGTH - 1))


def get_img(image):
    """This Function returns the grayscale resized image of the imput image given as parameter

    Args:
        image (ImageObj): PIL.Image type of image

    Returns:
        ImageObj: grayscale value
    """
    actual_width, actual_height = image.size
    new_height = int(actual_height*ASCII_IMAGE_WIDTH/actual_width)
    resized_image = image.resize((ASCII_IMAGE_WIDTH,new_height))
    return resized_image.convert('L')


def pixels_to_ascii_string(image):
    """This method receives the image object and get the individual
    pixel value of each pixel and get a string curresponding to this 
    number from the PIXEL_ARRAY and adds it to the string.
        after every ASCII_IMAGE_WIDTH it adds a new Line Character to
    the String and finally returns this String

    Args:
        image (ImageObj): Gets the Image(Should be a 2-D array, so not color images)

    Returns:
        String: The string which is needed to be printedto the file
    """
    pixels = image.getdata()
    width, height = image.size
    imageArray = np.asarray(image)
    # print(imageArray)
    string = ""
    for i in range(height):
        for j in range(width):
            string += (PIXEL_ARRAY[imageArray[i,j]//RANGE] + PIXEL_ARRAY[imageArray[i,j]//RANGE])
        string += "\n"
    return string


def main():
    loc = input("Enter the Location of image : ")
    file_name = input("file_name : ")
    file_name += ".txt"
    try:
        image = Image.open(loc)
    except:
        print("{} is not a valid image address".format(loc))

    toPrint = pixels_to_ascii_string(get_img(image))

    with open(file_name, mode="w",encoding='utf8') as file:
        file.write(toPrint)



if __name__ == "__main__":
    main()
