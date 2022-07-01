from PIL import Image

img_1 = Image.open('image.jpg')
img_1_resize = img_1.resize(size=(1000,1564), resample=Image.NEAREST)#リサイズ処理
img_1_resize = img_1_resize.save('ThemeImage.jpg', quality=95)#保存