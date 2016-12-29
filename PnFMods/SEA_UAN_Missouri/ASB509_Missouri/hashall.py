import os
import hashlib;
import sys;
import re
import time
reload(sys);
import warnings
warnings.filterwarnings("ignore")
def file_extension(path): 
  return os.path.splitext(path)[1]

def listFiles(dirPath):

    fileList=[]

    for root,dirs,files in os.walk(dirPath):

        for fileObj in files:

            fileList.append(os.path.join(root,fileObj))

    return fileList

def GetFileNameAndExt(filename):
	import os
	(filepath,tempfilename) = os.path.split(filename);
	(shotname,extension) = os.path.splitext(tempfilename);
	return shotname

sys.setdefaultencoding("utf-8");

def hashdir(fileDir):
    pass
    for filename in os.listdir(fileDir):
        print filename
        if file_extension(filename) == '.anca':
            continue
        if file_extension(filename) == '.primitives':
            continue
        if file_extension(filename) == '.splash':
            continue
        if file_extension(filename) == '.model':
            fp = open(fileDir+filename,'r+');
            fdata = fp.read();
            fp.close();
            fdata=fdata.replace('\t','').replace('\n','')
            #fp = open(fileDir+filename,'r+');
            fp = open(fileDir+filename,'w');
            fp.write(fdata)
            fp.close();
            #print(fdata)
            continue
        if file_extension(filename) == '.visual':
            fp = open(fileDir+filename,'r+');
            fdata = fp.read();
            fp.close();
            fdata=fdata.replace('\t','').replace('\n','')
            #fp = open(fileDir+filename,'r+');
            fp = open(fileDir+filename,'w');
            fp.write(fdata)
            fp.close();
            #print(fdata)
            continue
        if file_extension(filename) == '.mfm':
            fp = open(fileDir+filename,'r+');
            fdata = fp.read();
            fp.close();
            fdata=fdata.replace('\t','').replace('\n','')
            #fp = open(fileDir+filename,'r+');
            fp = open(fileDir+filename,'w');
            fp.write(fdata)
            fp.close();
            #print(fdata)
        fp = open(fileDir+filename,'rb');
        fdata = fp.read();
        fp.close();
        md5 = hashlib.md5();
        md5.update(fdata);
        print md5.hexdigest()+file_extension(filename);
        newfilename = md5.hexdigest()+file_extension(filename);
        #time.sleep(0.1)
        try:
            os.rename(fileDir+filename,fileDir+newfilename);
        except:
            os.remove(fileDir+filename)

        print('done')
        if file_extension(filename) == '.dds':
            oldfilename = GetFileNameAndExt(filename)+'.tga';
            newfilename = md5.hexdigest()+'.tga';
            pass
        else:
            oldfilename = filename;
            newfilename = md5.hexdigest()+file_extension(filename);
        regex = ur'FUNC_SYS_ADD_ACCDETAIL'
        fileList = listFiles(fileDir)
        for fileObj in fileList:
            if file_extension(fileObj) == '.anca':
                continue
            if file_extension(fileObj) == '.dds':
                continue
            if file_extension(fileObj) == '.primitives':
                continue
            if file_extension(fileObj) == '.splash':
                continue
            f = open(fileObj,'r+')
            all_the_lines=f.readlines()
            f.seek(0)
            f.truncate()
            for line in all_the_lines:
                f.write(line.replace(oldfilename,newfilename)) 
            f.close()

if os.path.exists("./aircraft/"):
	hashdir("./aircraft/")
if os.path.exists("./catapult/"):
	hashdir("./catapult/")
if os.path.exists("./director/"):
	hashdir("./director/")
if os.path.exists("./finder/"):
	hashdir("./finder/")
if os.path.exists("./gun/"):
	hashdir("./gun/")
if os.path.exists("./radar/"):
	hashdir("./radar/")
if os.path.exists("./ship/"):
	hashdir("./ship/")