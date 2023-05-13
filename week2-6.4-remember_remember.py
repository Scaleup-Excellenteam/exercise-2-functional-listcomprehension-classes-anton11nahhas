import PIL
from PIL import Image


IMG_PATH = 'resources/code.png'

def remember(path):
    """
    this program imports pil (pillow) module that can manipulates and operates on images
    this function opens the given image and loads its pixels onto a matrix, loop through
    the matrix and for each pixel check if the pixel is black and change the row num of the
    black pixel to its char form and extract the hidden message.
    for the code.png image the output should be:
    Place gunpowder beneath the House of Lords. 11/05/1605
    :param path: path for the image
    :return: returns the extracted hidden message
    """
    result = ""
    img = PIL.Image.open(path)
    pix = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pix[x, y] == 1:
                result += chr(y)
    return result


def main():
    print(remember(IMG_PATH))


if __name__ == "__main__":
    main()
