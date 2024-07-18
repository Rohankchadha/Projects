from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os,cv2,shutil
import process,Frame2,db

class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        # self.root.overrideredirect(True)
        self.root.geometry("600x600+200+30")
        # self.root.wm_attributes('-transparentcolor','black')
        
    def capt(self):
        face_dec=cv2.CascadeClassifier('face_model1.xml')
        smile_dec=cv2.CascadeClassifier('smile_model.xml')
        try:
            shutil.rmtree('check')
            os.rmdir('check')
            os.mkdir('check')
        except:
            os.mkdir('check')
        # define a video capture object
        vid = cv2.VideoCapture(0)
        currentframe=0
        pictures=[]
        while(True):

            # Capture the video frame
            # by frame
            ret, frame = vid.read()
            frame = cv2.flip(frame,1)
            if not ret:
                break
            gs_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces=face_dec.detectMultiScale(gs_frame)
            
            # print(faces)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (34, 250, 150),4)
                # print(x,y,w,h)
                the_face=frame[y:(y+h),x:(x+w)]
                # print(the_face)
                gs_the_face=cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

                smiles=smile_dec.detectMultiScale(gs_the_face,1.7,20)

                if len(smiles)>0:
                    cv2.putText(frame, "Smiling", (x,y+h+40), fontScale=2, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))
                # for (x_,y_,w_,h_) in smiles:
                #     cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (34, 30, 200),2)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            # cv2.createButton('Click',lambda :click(frame),None,cv2.QT_PUSH_BUTTON,1)

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice


            k=cv2.waitKey(1) &0xFF        
            if k==13:
                # print(currentframe)
                # cv2.imshow('Captured Picture | Click s to save',frame)
                name='check/captured'+str(currentframe)+'.jpg'
                cv2.imwrite(name, frame)
                dec=process.detect(name)
                print(dec.person.get_image(0))
                a=dec.person.get_image(0)
                b=dec.person.name
                Frame2.Frame1.name=b
                a=a.resize((200,200))
                a.save('check/datafile.jpg')
                break
                
            elif k==113:
                break 
            currentframe+=1
            # print(currentframe)
        # After the loop release the cap object
        vid.release()
        cv2.destroyAllWindows()
        self.fr1.destroy()
        obj=Frame2.Frame1(self.root)
        obj.create1()

    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=600)
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="Attendance \nSystem")
        self.label.place(x=150,y=140,width=300,height=100)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        # self.txt = Label(self.fr1, text="Paste URL")
        # self.txt.place(x=220,y=195)
        # self.txt.config(bg="black", fg="white")
        # self.ent = Entry(self.fr1)
        # self.ent.place(x=320, y=190, width=380, height=30)
        # self.btn = Button(self.fr1, text="Process", command=lambda: self.process(self.ent.get()))
        # self.btn.config( font=(20),fg="white", bg="navy blue")
        # self.btn.place(x=400,y=320,width=220,height=50)
        self.btn1 = Button(self.fr1, text="Mark Attendance", command=self.capt)
        self.btn1.config(font=(20),fg="white", bg="red")
        self.btn1.place(x=140,y=390,width=320,height=100)
        self.btn2 = Button(self.fr1, text="Exit", command=exit)
        self.btn2.config(font=(20),fg="white", bg="red")
        self.btn2.place(x=140,y=500,width=320,height=40)

if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()