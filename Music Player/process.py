# Importing all necessary libraries
import os,requests
from tkinter import filedialog

def get_data(a):
	# try:
		from pytube import YouTube
		import moviepy.editor as editor
		yt = YouTube(a)
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
		mp4=[('MP4 (Video)', '.mp4')]
		fl=filedialog.asksaveasfile(initialfile=yt.title, filetypes=mp4)
		fl=yt.title
		print(fl)
		with open('videos/'+fl+'.mp4','wb') as file:
			file.write(res.content)
		new_file = open('songs/'+fl+'.mp3','wb')
		# print(new_file)
		
		mp3file=editor.VideoFileClip('videos/'+fl+'.mp4')
		mp3file.audio.write_audiofile('songs/'+fl+'.mp3')
		mp3file.close()
		# print(mp3file)
# 		return True,"Song saved locally"
# 	except:
# 		return False,'Private Video or Something Wrong'
# # get_data('https://www.youtube.com/watch?v=6TbG2EJITQY')
# get_data('https://www.youtube.com/watch?v=nc6a39xldVw')