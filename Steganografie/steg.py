#Steganografie - ukládání zprávy do obrázku
#Holý program bez GUI

from PIL import Image

def zakoduj(img, zprava):
    lenght = len(zprava)
    
   #limituje délku textu 
   
    if lenght > 255: 
        print("Text je příliž dlouhý. Nepřekračuj délku 255 znaků!")
        return False
    if img.mode != 'RGB':
        print("Nesprávný formát obrázku!")
        return False
    
    #Kopie obrázku
    zakodovano = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r,g,b =  img.getpixel((col, row))
            if row == 0 and col == 0 and index < lenght:
                asc = lenght
            elif index  <= lenght:
                c= zprava[index -1]
                asc = ord(c)
            else:
                asc = r
                zakodovano.putpixel((col, row), (asc, g, b))
                index += 1
            return zakodovano
def dekoduj(img):
        width, height = img.size
        zprava= ""
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r,g,b = img.getpixel((col, row))
                except ValueError:
                    r,g,b,a = img.getpixel((col, row))
                if row == 0 and col == 0:
                    lenght = r
                elif index <= lenght:
                    zprava += chr(r)
                index += 1
            return zprava
        

original_image_file = "obrazek_motyla_1.jpg"
img =  Image.open(original_image_file)
#test RGB
print(img, img.mode)
zakodovany_img = "enc_" + original_image_file
tajna_zprava = "Hello World"
print(len(tajna_zprava))

img_kodovany = zakoduj(img, tajna_zprava)

#uložení zakodovaneho obrázku
if img_kodovany:
    img_kodovany.save(zakodovany_img)
    print("{} uloženo!".format(zakodovany_img))
    
    import os
    os.startfile(zakodovany_img)
    
 #Dekodování obrázku   
    img2 = Image.open(zakodovany_img)
    skryty_text = dekoduj(img2)
    print("Skrytá zpráva:\n{}".format(skryty_text))

