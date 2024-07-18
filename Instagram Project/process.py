from instagrapi import Client
import instagrapi
from tkinter import messagebox, filedialog
from PIL import Image

def login(id,pas):
    cl = Client()
    try:    
        cl.login(id, pas)
        return cl,True
    except instagrapi.exceptions.BadPassword:
        return "Wrong Password",False
    except:
        print('Unknown Error')
        return "Unknown Error",False

def post(cl,image,capt):
    try:
        try:
            cl.photo_upload(path=image,caption=capt)
            return "Photo Uploaded",True
        except:
            cl.video_upload(path=image,caption=capt)
            return "Video Uploaded",True
    except instagrapi.exceptions.PhotoNotUpload:
        return "Please Choose JPG picture",False
    except:
        return "Unknown Error",False
    
def story(cl,image,capt):
    try:
        try:
            cl.photo_upload_to_story(path=image,caption=capt)
            return "Story Uploaded",True
        except:
            cl.video_upload_to_story(path=image,caption=capt)
            return "Story Uploaded",True
    except instagrapi.exceptions.PhotoNotUpload:
        return "Please Choose JPG picture",False
    except:
        return "Unknown Error",False
    
def dpchange(cl,image):
    try:
        cl.account_change_picture(image)
        return "Profile Picture Updated Successfully", True
    except:
        return "Please choose JPG picture",False
