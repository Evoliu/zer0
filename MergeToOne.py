import numpy
import os,sys
import shutil
###########################################################
## Wo de di yi ge di gui sou suo suan fa!!hao J dong!!!! ##
###########################################################

##   for mining, need a list beforhand to restore paths pointing the files that you want  ##
def mining(Root,label_sheet):
    l1=os.listdir(Root)
    if len(l1)==len(label_sheet) and not(0 in {(n in label_sheet) for n in l1}):
        path_list.append(Root)
    else:
        for n in l1:
            SubRoot = Root+n+"/"
            if os.path.isdir(SubRoot) and len(n)!=0: 
                mining(SubRoot,label_sheet)

def GrabAndDrop(Root,Dst,label_sheet):
    Root = str(Root)
    Dst = str(Dst)
    count = 0
    #if not os.path.isdir(Dst):
    #    os.mkdir(Dst)
    #    {os.mkdir(Dst+n+'/') for n in label_sheet}
    #elif (0 in {os.path.isdir(Dst+i+'/') for i in label_sheet}) or len(label_sheet)!=len(os.listdir(Dst)):
    #    {shutil.rmtree(Dst+n+'/') for n in os.listdir(Dst)}
    #    {os.mkdir(Dst+n+'/') for n in label_sheet}
    mining(Root,label_sheet)
    print path_list
    print len(path_list)
    for path in path_list:
        path_l1 = os.listdir(path)
        for n in path_l1:
            Sub_path = path+n+'/'
            path_l2 = os.listdir(Sub_path)
            for i in path_l2:
                img_path = Sub_path+i
                shutil.copy(img_path,Dst+n+"/"+i)
                count+= 1
                print "Have merged images: "+str(count)+"."

if __name__ == "__main__":
    Root = "/media/share/ryu/Dataset/FMD_v2_for_train/"
    label_sheet = ["metal","paper","fabric","glass","foliage","wood","plastic","stone","leather","water"]
    Dst = "/media/share/ryu/Dataset/Mer_FirstShotAugU_and_FMD_v2_for_train/Dataset/"
    path_list=[]
    GrabAndDrop(Root,Dst,label_sheet)



