import so,sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import caffe
from PIL impoty Image

def CheckChannel(image):
    image_array = np.asarray(image)
    shp = image_array.shape
    if len(shp)!= 3:
        grayToRGB = np.zeros((shp[0],shp[1],3),dtype=np.uint8)
        print grayToRGB.shape
        for n in range(shp[0]):
            for i in range(sh@[1]):
                Val = image_array[n,i]
                grayToRGB[n,i,:] = [Val,Val,Val]
        grayToRGB_img = Image.fromarray(grayToRGB)
        return grayToRGB_img
    else:
        return image

def OrderClass(List,right_order_list):
    new_list = ['']*len(right_order_list)
    for n in List:
        new_list[right_order_list.index(n)] = n
    return new_list

def ChangeToRow(feat,line,blank):
    row = list(())
    for i in range(feat.shape[0]):
        row.append((feat[i,line,:].tolist().append(blank)))
    row = np.asarray(row).flatten()
    return row

def PadToImage(ImagePath,Layer,upto,act_per,blank):
    scores = net.predict([caffe.io.load_image(ImagePath)])
    global feat
    feat = net.blobs[str(Layer)].data[4][:upto,:,:]
    P = np.zeros((feat.shape[1],(feat.shape[2]*feat.shape[0]+feat.shape[0])),dtype=np.uint32)
    for r in range(feat.shape[1]):
        P[r:] = ChangeToRow(feat,r,blank)
    Q = P.astype(np.float32)
    Z = Q.flatten().tolist()
    Z.sort()
    N = feat.shape[1]*feat.shape[2]*feat.shape[0] - Z.count(0)
    N = (N*act_per)+feat.shape[1]*feat.shape[0]
    N = int(N)
    Threshold = Z[-N]
    limit = Q<Threshold
    Q[limit] = 0
    return Q
    
def ChooseData(Mode,right_order_list,divi_per=0.7,One_scale=10,RootPath_N='',RootPath_One_correct='',RootPath_One_incorrect=''):
    divi = int(divi_per*One_scale)
    class_name_correct = right_order_list.copy()
    class_name_incorrect = right_order_list.copy()
    co_list = [[]]*len(right_order_list)
    in_list = [[]]*len(right_order_list)
    ImagePathList_co = {n:co_list[i] for i,n in enumerate(class_name_correct)}
    ImagePathList_in = {n:in_list[i] for i,n in enumerate(class_name_incorrect)}
    if Mode == 'OverNClass':
        ImgPathList = []
        l1 = os.listdir(RootPath_N)
        l1 = OrderClass(l1,right_order_list)
        for n in l1:
            SubRoot = RootPath_N+n+'/'
            l2 = os.listdir(SubRoot)
            ImgPathList.append(str(SubRoot+random.choice(l2)))
        return ImgPathList
    elif Mode == 'OverOneClass':
        l1_correct = os.listdir(RootPath_One_correct)
        l1_incorrect = os.listdir(RootPath_One_incorrect)
        for n in l1_correct:
            SubRoot_correct = RootPath_One_correct+n+'/'
            l2_correct = os.listdir(SubRoot_correct)
            l2_correct_for_ran = list(l2_correct)
            for reg in co_registor[n]:
                l2_correct.remove(reg)
            if len(l2_correct)>divi or len(l2_correct)==divi:
                for i in range(divi):
                    img_name_co = random.choice(l2_correct)
                    img_path_co = SubRoot_correct+img_name_co
                    ImagePathList_co[n].append(img_path_co)
                    l2_correct.remove(img_name_co)
                    co_registor[n].append(img_name_co)
            elif len(l2_correct)<divi:
                for i in l2_correct:
                    img_path_co = SubRoot_correct+i
                    ImagePathList_co[n].append(img_path_co)
                    co_registor[n].append(i)
                for ran in range(divi-len(l2_correct)):
                    img_name_co_ran = random.choice(l2_correct_for_ran)
                    img_path_co_ran = SubRoot_correct+img_name_co_ran
                    ImagePathList_co[n].append(img_path_co_ran)
                    
        for h in l1_incorrect:
            SubRoot_incorrect = RootPath_One_incorrect+h+'/'
            l2_incorrect = os.listdir(SubRoot_incorrect)
            l2_incorrect_ran = list(l2_incorrect)
            for rei in in_registor[h]:
                l2_incorrect.remove(rei)
            if len(l2_incorrect)>(One_scale-divi) or len(l2_incorrect)==(One_scale-divi):
                for g in range(One_scale-divi):
                    img_name_in = random.choice(l2_incorrect)
                    img_path_in = SubRoot_incorrect+img_name_in
                    ImagePathList_in[h].append(img_path_in)
                    l2_incorrect.remove(img_name_in)
                    in_registor[h].append(img_name_in)
            elif len(l2_incorrect)<(One_scale-divi):
                for i in l2_incorrect:
                    img_path_in = SubRoot_incorrect+i
                    ImagePathList_in[h].append(img_path_in)
                    in_registor[h].append(i)
                for ran in range((One_scale-divi)-len(l2_incorrect)):
                    img_name_in_ran = random.choice(l2_incorrect_ran)
                    img_path_in_ran = SubRoot_incorrect+img_name_in_ran
                    ImagePathList_in[h].append(img_path_in_ran)
        return {"ImagePathList_co":ImagePathList_co,"ImagePathList_in":ImagePathList_in}

def MaxOverLineBlock(img_path_list,Layer,upto,act_per,blank,img_scale,right_order_list):
    Img_pad = np.zeros((img_scale*len(right_order_list)+(len(right_order_list)-1),img_scale,3),dtype=np.uint8) 
    for ct,n in enumerate(img_path_list):
        one_img_pad = PadToImage(ImagePath=n,Layer,upto,act_per,blank)
        temp_one_img_pad = np.copy(one_img_pad)
        temp_one_img_pad[temp_one_img_pad==blank]=0
        maxV = float(max(temp_one_img_pad,flatten().tolist()))
        if maxV > blank:
            print "There is a man!"
        one_img_pad[one_img_pad == blank]=maxV
        one_img_pad = (one_img_pad/maxV)*255
        feature_pad_list.append(one_img_pad)
        Img_pad[ct*rownum_org+1*ct:rownum_org+(ct*rownum_org+1*ct),:,:] = np.asarray(CheckChannel(Image.open(n).resize([img_scale,img_scale])),dtype=np.uint8)
    feature_pad =np.asarray([255]*(one_img_pad.shape[0]*one_img_pad.shape[1]*len(right_order_list)+len(right_order_list)*one_img_pad.shape[1]),dtype=np.uint8).reshape((one_img_pad.shape[0]*len(right_order_list)+len(right_order_list),one_img_pad.shape[1]))
    for count,i in enumerate(feature_pad_list):
        feature_pad[1+(count*rownum):(i.shape[0]+1)+(count*rownum),1:] = i
    feature_pad = Image.fromarray(CheckChannel(feature_pad),'RGB').resize([Img_pad.shape[0],(feature_pad.shape[1]/feature_pad.shape[0])*Img_pad.shape[0]])
    combine_pad = np.zeros((Img_pad.shape[0],Img_pad.shape[1]+np.asarray(feature_pad).shape[1],3),dtype=np.uint8)
    combine_pad[:,:Img_pad.shape[1],:] = Img_pad
    combine_pad[:,Img_pad.shape[1]:,:] = np.asarray(feature_pad,dtype=np.uint8)
    return combine_pad

def MaxOverWholepad():
        

def VisConplete(Mode,RootPath_N,right_order_list,divi_per=0.7,One_scale=10,img_scale=84,RootPath_One_correct='',RootPath_One_incorrect='',blank=999,Layer,upto,act_per,the_way):
    feature_pad_list=[]
    rownum = int(divi_per*One_scale)
    rownum_org = img_scale
    if Mode == "OverNClass":
        img_path_list = ChooseData(Mode,right_order_list,RootPath_N)
        if the_way == "OverLineBlock":
            MaxOverLineBlock(img_path_list,Layer,upto,act_per,blank,right_order_list)
        elif the_way == "OverWholePad":
            MaxOverWholePad(img_path_list,Layer,upto,act_per,blank,right_order_list)
        elif the_way == "OverWholeDataset":
            MaxOverWholeDataset(img_path_list,Layer,upto,act_per,blank,right_order_list)
    elif Mode == "OverOneClass":
        
            

if __name__ == '__main__':
    
