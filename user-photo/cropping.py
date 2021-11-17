import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def crop(name):
    Open the input image as numpy array, convert to RGB
    img=Image.open(name).convert("RGB")
    npImage=np.array(img)
    h,w=img.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,min(h,w),min(h,w)],0,360,fill=255)
    a=min(h,w)


    # Convert alpha Image to numpy array
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save(name[:-4]+'_photo.png')
    im = Image.open(name[:-4]+'_photo.png')

    a=min(im.size)
    im=im.crop((0,0,a,a))
    im.save(name[:-4]+'_photo.png')

def docrop():
    for i in range(100):
        try:
            crop(i.toToString("000")+'.jpg')
        except:
            x=1
