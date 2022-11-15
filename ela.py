import sys
from PIL import Image, ImageChops


if len(sys.argv) > 1:        # if image path is entered, assign in to variable inp 
    inp = sys.argv[1]

else:                        # if no image path is entered, use a default one we included
    print("No image supplied -- using the fake lotto ticket example.\n")
    inp = './lotto-fake.jpg'


TEMP = 'temp.jpg'       # temporary image name to save the ELA to
SCALE = 77              # Error Level scale.  Change this (along with the alpha value) to better check for manipulation
ALPHA = .66             # transparency level to blend the ELA with the original

def ELA():
    # Error Level Analysis for basic image forensics
    original = Image.open(inp)          # open up the input image
    original.save(TEMP, quality=95)     # re-save the image with a quality of 95%
    temporary = Image.open(TEMP)        # open up the re-saved image

    diff = ImageChops.difference(original, temporary)   # load in the images to look at pixel by pixel differences
    d = diff.load()                     # load the image into a variable
    WIDTH, HEIGHT = diff.size           # set the size into a tuple
    for x in range(WIDTH):                                  # row by row
        for y in range(HEIGHT):                             # column by column
            d[x, y] = tuple(k * SCALE for k in d[x, y])     # set the pixels to their x,y & color based on error


    diff.save('ela-saved.jpg')          # save the ELA version of the image
    #diff.show()                        # show the ELA version

    new_img = ImageChops.blend(temporary, diff, ALPHA)      # blend the original w/ the ELA @ a set alpha/transparency
    new_img.save('comp-saved.jpg', quality=95)              # save the image @ 95% quality

    new_img.show()          # display the blended image -- original + ELA

if __name__ == '__main__':
    ELA()
