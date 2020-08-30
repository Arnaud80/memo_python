#Mesure le diametre d un cercle

from PIL import Image

#img = Image.open('ressources/Flag_of_Bangladesh.png')
img = Image.open('ressources/bd.png')
#img.show()

width, height = img.size
print("width=" + str(width))
print("height=" + str(height))

#Vert : (0, 106, 78)
#Rouge : (244, 42, 65)
#rouge=(244, 42, 65)
rouge=1
cordinate = (0, 0)

print(img.getpixel(cordinate))
diametre=0
largeur=0
count=0
pixel=img.getpixel(cordinate)

for y in range(0,height):
    if largeur > diametre :
        diametre=largeur

    largeur=0

    for x in range(0,width):
        cordinate = x, y
        pixel=img.getpixel(cordinate)
        if pixel==rouge :
            count=count+1
            largeur=largeur+1

print("Diametre = " + str(diametre))
print("Count = " + str(count))
#print("Rouge = " + rouge)
#print("Pixel = " + pixel)
