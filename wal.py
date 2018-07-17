import os
def find(name,path,number):
    os.chdir(path)
    k=str(number)+'_'+name
    os.rename(name,k)

def sort_dir(filelist,path):
    number=0
    for filename in filelist:
        find(filename,path,number+1)
        number+=1