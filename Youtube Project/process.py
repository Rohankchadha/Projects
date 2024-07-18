# Importing all necessary libraries
import cv2
import os,requests
from pytube import YouTube

def get_data(a):
	try:
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
		with open('savedfile.mp4','wb') as file:
			file.write(res.content)



		# Read the video from specified path
		cam = cv2.VideoCapture('savedfile.mp4')

		try:
			
			# creating a folder named data
			if not os.path.exists('data'):
				os.makedirs('data')

		# if not created then raise error
		except OSError:
			print ('Error: Creating directory of data')

		# frame
		currentframe = 0
		name_list=[]
		a=0
		while(True):
			# fps = cam.get(cv2.CAP_PROP_FPS)
			# print('frames per second =',fps)
			
			#reading from frame
			ret,frame = cam.read()
			if ret:
				fps = cam.get(cv2.CAP_PROP_FPS)
				if int(currentframe)%int(fps/2)==0:
					# if video is still left continue creating images
					name = 'data/frame' + str(a) + '.jpg'
					print ('Creating...' + name)
					name_list.append(name)
					cv2.imwrite(name, frame)
					a+=1
					# increasing counter so that it will
					# show how many frames are created
					print(currentframe)
			else:
				break
			currentframe += 1
		# Release all space and windows once done
		cam.release()
		cv2.destroyAllWindows()
		return name_list,True
	except:
		return "",False
