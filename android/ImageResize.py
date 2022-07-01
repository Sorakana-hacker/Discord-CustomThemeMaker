from PIL import Image

img_1 = Image.open('image.jpg')
img_1_resize = img_1.resize(size=(540,1080), resample=Image.NEAREST)
img_1_resize = img_1_resize.save('ThemeImage.jpg', quality=95)