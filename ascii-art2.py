# Import Libraries
from PIL import Image


# Constants
ASCII_IMAGE_WIDTH = 150
PIXEL_ARRAY = ["#","@","O","=","+","o","^","*","!","."]
LENGTH = len(PIXEL_ARRAY)
RANGE = int(255/(LENGTH - 1))


def get_img(image):
    actual_width, actual_height = image.size
    new_height = int(actual_height*ASCII_IMAGE_WIDTH/actual_width)
    resized_image = image.resize((ASCII_IMAGE_WIDTH,new_height))
    return resized_image.convert('L')

def pixels_to_ascii_string(image):
    pixels = image.getdata()
    charecters = "".join( [PIXEL_ARRAY[pixel//(RANGE)] for pixel in pixels] )
    return charecters


def set_line_break(listOfChar):
    new_data = "\n".join([listOfChar[index:(index+ASCII_IMAGE_WIDTH)] for index in range(0, len(listOfChar), ASCII_IMAGE_WIDTH)])
    return new_data

def main():
    loc = input("Enter the Location of image")
    try:
        image = Image.open(loc)
    except:
        print("{} is not a valid image address".format(loc))

    new_image = pixels_to_ascii_string(get_img(image))
    toPrint = set_line_break(pixels_to_ascii_string(get_img(image)))

    with open("ascii-art2.txt", "w") as file:
        file.write(toPrint)

main()