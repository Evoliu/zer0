import os,sys
import numpy as np
import PIL
from PIL import Image
import shutil
import CheckDst.CkDst as CkDst

def im2double(image):
    image = np.asarray(image)
    minV = np.min(image.ravel())
    maxV = np.max(image.ravel())
    img = (image.astype('float')-minV)/(maxV-minV)
    return img

def Normalize(Root,Dst,label_sheet):
    CkDst(Dst,label_sheet)
    l1 = os.listdir(Root)
    for n in l1:
        SubRoot = Root+n+'/'
        l2 = os.listdir(SubRoot)
        for i in l2:
            ImgPath = SubRoot+i
            img = im2double(Image.open(ImgPath))
            Mean = img.mean()
            Std = img.std()
            Img = (img-Mean)/Std*0.28+0.6
            Img = Img*0.75+img*0.25
            Image.fromarray(Img,"RGB").save(Dst+n+'/'+i,"PNG")
