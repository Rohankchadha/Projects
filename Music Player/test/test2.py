import cv2
import os
cam = cv2.VideoCapture('videos/Top 10 iPhone Trick Shots.mp4')
currentframe=0
while True:
    ret,frame = cam.read()
    if ret:
        fps = cam.get(cv2.CAP_PROP_FPS)
        if int(currentframe)%int(fps/2)==0:
				# if video is still left continue creating images
            name = 'data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
            cv2.imshow('Click s to save',frame)
            k=cv2.waitKey(0) &0xFF
            if k==115:
                cv2.imwrite(name, frame)
            else:
                print("not saved")

				# increasing counter so that it will
				# show how many frames are created
            print(currentframe)
    else:
        break
    currentframe += 1

cam.release()
cv2.destroyAllWindows()

