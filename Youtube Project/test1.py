from pytube import YouTube
import requests
yt = YouTube("https://www.youtube.com/watch?v=VnM_XyCxHW8")
data=yt.streaming_data
print(yt.title)
lst=[]
for i in data['formats']:
    # print(i)
    if i['qualityLabel']=='720p':
        lst.append(i['url'])
print(lst)
url=lst[0]
headers = {'Content-Type':'application/json', 'x-app-id':'cf603149', 'x-app-key':'cbbd0d41f6db22ef430c149072faa50a'}
res=requests.get(url,headers)
# print(res.content)
with open('savedfile.mp4','wb') as file:
    file.write(res.content)
# mp4_files = yt.streams.filter(file_extension="mp4")
# print(mp4_files)
# mp4_369p_files = mp4_files.get_by_resolution("360p")
# print(mp4_369p_files)
# mp4_369p_files.download("videos")