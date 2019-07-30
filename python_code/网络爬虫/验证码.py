import Image
import pytesseract
im = Image.open('img/198image.jpg')
aa = pytesseract.image_to_string(out_img)
print(aa)