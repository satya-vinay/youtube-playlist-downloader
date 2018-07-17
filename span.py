from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
def returnlist(url):
    data = urlopen(url).read()
    soup = bs(data)
    k=1
    video_titles=[]
    for title in soup.findAll('li',class_="yt-uix-scroller-scroll-unit"):
        ti=title["data-video-title"]
        for i in r'\/"?:*<>|':
            if i in ti:
                ti=ti.replace(i,"")
        video_titles.append(ti+".mp4")
        k+=1
    return video_titles