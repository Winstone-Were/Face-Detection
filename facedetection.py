# import the opencv library 
import cv2 
  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  


vid = cv2.VideoCapture(0) 
  
while(True): 
      
    ret, frame = vid.read()  

    # convert to gray scale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces: 
        #  face  
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w] 
  
        eyes = eye_cascade.detectMultiScale(roi_gray)  
  
        #Teyes 
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2) 

    cv2.imshow('frame', frame) 
      

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  

vid.release() 
cv2.destroyAllWindows() 