#Steganographie
from PIL import Image

def CodeAsciiVersListe(num):
    liste=[]
    for c in format(num,"08b"):
        liste.append(c)
    return(liste)

def FusionDeuxListes(listeA, listeB):
    liste=[]
    for i in range(0,4):
        liste.append(listeA[i])
    for i in range(0,4):
        liste.append(listeB[i])

    return(liste)

def ListeVersAscii(liste):
    strBin=""
    for c in liste:
        strBin=strBin+c
    
    return(int(strBin,base=2))

def fusionPixel(pixel1, pixel2):
    pixel=list((0,0,0))

    for i in range(0,3):
        bin1=CodeAsciiVersListe(pixel1[i])
        bin2=CodeAsciiVersListe(pixel2[i])
        fusion=FusionDeuxListes(bin1, bin2)
        pixel[i]=ListeVersAscii(fusion)
    return tuple(pixel)

def Codage(photo1, photo2):
    width1, height1 = photo1.size
    width2, height2 = photo2.size
    
    if width1==width2 and height1==height2 :
        photoResult=Image.new(mode = "RGB", size = (width1, height1))
        for y in range(0,height1):
            for x in range(0,width1):
                coordinates = x, y
                pixel1=photo1.getpixel(coordinates)
                pixel2=photo2.getpixel(coordinates)
                pixelResut=fusionPixel(pixel1, pixel2)
                photoResult.putpixel(coordinates,pixelResut)
        return photoResult
    else :
        print("Les images doivent avoir la même taille")
        return -1

def decodagePixel(pixel):
    pixel1=[]
    pixel2=[]
    for i in range(0,3):
        bin=CodeAsciiVersListe(pixel[i])
        bin1=bin[:4]+['0','0','0','0']
        bin2=bin[4:]+['0','0','0','0']

        #print("bin="+str(bin))
        #print("bin1="+str(bin1))
        #print("bin2="+str(bin2))

        pixel1.append(ListeVersAscii(bin1))
        pixel2.append(ListeVersAscii(bin2))

    return(tuple(pixel1), tuple(pixel2))

def Decodage(photo):
    width, height = photo.size
    
    photo1=Image.new(mode = "RGB", size = (width, height))
    photo2=Image.new(mode = "RGB", size = (width, height))

    for y in range(0,height):
        for x in range(0,width):
            coordinates = x, y
            pixel=photo.getpixel(coordinates)
            doublePixel=decodagePixel(pixel)
            photo1.putpixel(coordinates,doublePixel[0])
            photo2.putpixel(coordinates,doublePixel[1])
    
    photo1.show()
    photo2.show()
    
'''
# Codage
photo1 = Image.open('ressources/image1.jpg')
photo2 = Image.open('ressources/image3.jpg')

photoResult=Codage(photo1, photo2)
photoResult.show()
photoResult.save("ressources/PhotoCoded2.png")
'''


# Decodage 
photo = Image.open('ressources/PhotoCoded2.png')
Decodage(photo)


'''
ListeA=CodeAsciiVersListe(150)
ListeB=CodeAsciiVersListe(50)
print(ListeA)
print(ListeB)
result=(FusionDeuxListes(ListeA, ListeB))
print(result)
print(ListeVersAscii(result))
'''