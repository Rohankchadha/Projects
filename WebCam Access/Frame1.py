# import the opencv library
import cv2

face_dec=cv2.CascadeClassifier('face_model1.xml')
smile_dec=cv2.CascadeClassifier('smile_model.xml')
# define a video capture object
vid = cv2.VideoCapture(0)

while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
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

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
