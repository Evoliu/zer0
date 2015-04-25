import os,sys
import numpy
import PIL
from PIL import Image

def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

def ConvertToImages(file,output_path):
    name_sheet = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
    dic = unpickle(file)
    for i in range(10000):
	img_l = numpy.hsplit(dic["data"][i,:],3)
	img_pad = numpy.zeros((32,32,3),dtype=numpy.uint8)
	for m in range(3):
	    img_pad[:,:,m] = img_l[m].reshape((32,32))
	clasS = name_sheet[dic["labels"][i]]
	j = len(os.listdir(output_path+clasS+"/"))
	Image.fromarray(img_pad).save(output_path+clasS+"/"+clasS+"_"+str(j)+".png","PNG")

    
if __name__ == "__main__":
   ConvertToImages("/media/share/ryu/Dataset/cifar10/cifar10-images/cifar-10-batches-py/data_batch_1","/media/share/ryu/Dataset/cifar10/cifar10-images/Images_for_train/")
   ConvertToImages("/media/share/ryu/Dataset/cifar10/cifar10-images/cifar-10-batches-py/data_batch_2","/media/share/ryu/Dataset/cifar10/cifar10-images/Images_for_train/")
   ConvertToImages("/media/share/ryu/Dataset/cifar10/cifar10-images/cifar-10-batches-py/data_batch_3","/media/share/ryu/Dataset/cifar10/cifar10-images/Images_for_train/")
   ConvertToImages("/media/share/ryu/Dataset/cifar10/cifar10-images/cifar-10-batches-py/data_batch_4","/media/share/ryu/Dataset/cifar10/cifar10-images/Images_for_train/")
   ConvertToImages("/media/share/ryu/Dataset/cifar10/cifar10-images/cifar-10-batches-py/data_batch_5","/media/share/ryu/Dataset/cifar10/cifar10-images/Images_for_train/")
