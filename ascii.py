from PIL import Image
from numpy import *
import sys

# get command line arguments
image = sys.argv[1]
xFinal = int(sys.argv[2])
# import image
temp = Image.open(image)
# get width and height
width, height = temp.size
percentage = xFinal/width
temp = temp.resize((int(width*percentage),int(height*percentage)))
# B&W .convert takes parameter for different conversion method
# 1 true or false, black or white
# L scalar 255 white 0 black everything inbetween exists
temp = temp.convert('L')
temp.show()
arr = array(temp)
art = []

# 1 conversion type
# for i in range(len(arr)):
#     temp = []
#     for j in range(len(arr[i])):
#         if arr[i][j]:
#             temp.append(" ")
#         else:
#             temp.append("$")
#     art.append(temp)

# L conversion type
for i in range(len(arr)):
    temp = []
    for j in range(len(arr[i])):
        # Add more elifs if you want to make the classification more specific
        if arr[i][j] >= 238:
            temp.append(" ")
        elif arr[i][j] >= 221:
            temp.append(".")
        elif arr[i][j] >= 204:
            temp.append("*")
        elif arr[i][j] >= 187:
            temp.append("I")
        elif arr[i][j] >= 170:
            temp.append("<")
        elif arr[i][j] >= 153:
            temp.append("?")
        elif arr[i][j] >= 136:
            temp.append("1")
        elif arr[i][j] >= 119:
            temp.append("/")
        elif arr[i][j] >= 102:
            temp.append("z")
        elif arr[i][j] >= 85:
            temp.append("C")
        elif arr[i][j] >= 68:
            temp.append("Z")
        elif arr[i][j] >= 51:
            temp.append("d")
        elif arr[i][j] >= 34:
            temp.append("o")
        elif arr[i][j] >= 17:
            temp.append("&")
        else:
            temp.append("$")
    art.append(temp)

file = open("result.txt", "w")
for line in art:
    for c in line:
        file.write(c)
    file.write("\n")
file.close()