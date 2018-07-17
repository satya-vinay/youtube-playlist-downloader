from pytube import Playlist
import os
import getpass
import wal
import span
def download_playlist(url):
    pl = Playlist(url)
    user=getpass.getuser()
    while(True):
        foldername=input("Enter the folder name")
        try:
            path=r'C:\users\{0}\Downloads\{1}'.format(user,foldername)
            os.mkdir(path)
            break
        except FileExistsError:
            YorN=input("Folder Exists are you sure to continue in this folder(Y/N)")
            if(YorN=="Y"):
                break
            else:
                continue
    pl.download_all(path)
    return path
url=input("Enter the URL of the playList")
path=download_playlist(url)
filelist=span.returnlist(url)
wal.sort_dir(filelist,path)
print(filelist)
print(url)