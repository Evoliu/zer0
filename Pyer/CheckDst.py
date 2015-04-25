import os,sys
import shutil

def CkDst(Dst,label_sheet):
    if not os.path.isdir(Dst):
        os.mkdir(Dst)
        {os.mkdir(Dst+n+'/') for n in label_sheet}
    elif (0 in {os.path.isdir(Dst+i+'/') for i in label_sheet}) or len(label_sh\
eet)!=len(os.listdir(Dst)):
        {shutil.rmtree(Dst+n+'/') for n in os.listdir(Dst)}
        {os.mkdir(Dst+n+'/') for n in label_sheet}
