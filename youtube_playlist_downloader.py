# pip install pytube

#for downloading playlist

from pytube import Playlist
py = Playlist("https://www.youtube.com/playlist?list=PLcDUxUcRRNCaxkeQ-Cg0Y2R1Ep99jKuon")
# print(f'Downloading : {py.title}')
for video in py.videos:
    video.streams.first().download()
# videos = list(enumerate(video))
# for i in videos:
#     print(i)
# print()
# strm=int(input("enter the index number of list : "))
# video[strm].download()
print("Playlist downloaded successfully")