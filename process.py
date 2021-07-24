from PIL import Image, ImageFilter
import sys
def processPic(img,width,height):
    r_array = []
    g_array = []
    b_array = []
    bl_array = []
    e4col = False
    lastRow = 0
    w = width-1
    h = 0
    buf = ""
    while h != height:
            r_array.append([1]*width)
            g_array.append([1]*width)
            b_array.append([1]*width)
            bl_array.append([1]*width)
            while w >= 0:
                    r,g,b,a = img.getpixel((w, h)) #get rgba of each pixel
                    #check if red, green, or blue is greatest in rgb values --- check if black or white also --> then append array differently for each switch case
                    if r > g and r > b :
                        e4col = True
                        r_array[h][w] = 0
                        lastRow = h
                        print("R", end="")
                    elif g > r and g > b :
                        e4col = True
                        g_array[h][w] = 0
                        lastRow = h
                        print("G", end="")
                    elif b > r and b > g :
                        b_array[h][w] = 0
                        lastRow = h
                        print("B", end="")
                    elif b < 50 and r < 50 and g < 50 :
                        bl_array[h][w] = 0
                        lastRow = h
                        buf=buf+"0"
                    else:
                        buf=buf+"1"
                    w = w-1 #move to next pixel -- use -1 to flip image -> make images not backward when printed
            w = width-1 #reset width counter
            h = h+1 #move to next row
    exec("val = hex(0b"+buf+");print(val.split('0x')[1])")
    #print(val.split("0x")[1])
    return (r_array,g_array,b_array,bl_array,e4col,lastRow)

filename = sys.argv[1]
img1 = Image.open(filename) #open image
img2=img1.convert("RGBA")
img = img2.transpose(Image.FLIP_LEFT_RIGHT)
width, height = img.size # get image size

print("{0:03}".format(width),end="")
print("{0:03}".format(height),end="")
r_array, g_array, b_array, bl_array, e4col, lastRow = processPic(img, width, height)

