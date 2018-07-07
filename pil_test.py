from PIL import Image, ImageEnhance
from matplotlib.pylab import plt

# fc = Image.open("fc.JPG")
# fc_a = fc.convert("RGBA")
# alpha = fc_a.split()[3]
# alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
# jt = Image.open("jt.PNG")
# print fc.mode, fc.size, alpha,jt.mode, jt.size
# def paste():
# 	layer = Image.new("RGBA", fc.size)
# 	img = Image.new("RGBA", jt.size)
# 	img.paste(jt)
# 	img.resize((500, 500))
# 	layer.paste(img)
# 	c = Image.composite(layer, fc, layer)
# 	plt.imshow(c)
# 	plt.show()


def reduce_opacity(image, opacity):
    assert opacity >= 0 and opacity <= 1

    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    else:
        image = image.copy()

    alpha = image.split()
    for i in alpha:	
	    plt.imshow(i)
	    plt.show()

    # print type(alpha)
    # alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    # print alpha
    # image = image.putalpha(alpha)
    # print image
    # plt.imshow(image)
    # plt.show()
    # image.save("hahaha.JPG")
    image.getpixel((0,0))
    return image

reduce_opacity(Image.open("jt.PNG"), 0.5)