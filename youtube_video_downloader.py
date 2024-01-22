# pip install pytube

from pytube import YouTube

link = "https://www.youtube.com/watch?v=_9-iTUM-RS0"
youtube_1 =  YouTube(link)

#print(youtube_1.title)
#print(youtubr_1.thumbnail_url)

videos =youtube_1.streams.all()#all formate

vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter the index number of list: "))
videos[strm].download()
print("video successfully downloaded")


