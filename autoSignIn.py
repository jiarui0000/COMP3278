import urllib
import numpy as np
import mysql.connector
import cv2
import pyttsx3
import pickle
import datetime, time
import train
import faceCapture
import sys

global customer_id

def autoSignIn():
    global customer_id
    now = time.time()
    login_flag = False

    # 1 Create database connection
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="u3563782", database="COMP3278_G12")
    cursor = myconn.cursor()


    #2 Load recognize and read label from model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    try:
        recognizer.read("TrainingLabel/train.yml")
    except:
        e = 'Model not found or corrupted,Please train the model by clicking Register New Student'
        print(e)

    labels = {"person_name": 1}
    with open("labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}


    # Define camera and detect face
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)


    # 4 Open the camera and start face recognition
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)

        for (x, y, w, h) in faces:
            print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)

            # 4.1 If the face is recognized
            if conf >= 30:
                # print(id_)
                # print(labels[id_])
                font = cv2.QT_FONT_NORMAL
                id = 0
                id += 1
                customer_id = labels[id_]
                color = (255, 0, 0)
                stroke = 2
                cv2.putText(frame, customer_id, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                # Find the customer information in the database.
                select = "SELECT customer_id, name FROM Customer WHERE customer_id='%s'" % (customer_id)
                name = cursor.execute(select)
                result = cursor.fetchall()
                # print(result)
                data = "error"
                for x in result:
                    data = x
                # If the customer's information is not found in the database
                if data == "error":
                    # the customer's data is not in the database
                    print("The customer", customer_id, "is NOT FOUND in the database.")

                # If the customer's information is found in the database
                else:
                    """
                    Implement useful functions here.
                    

                    """
                    hello = ("Hello ", result[0] , "Welcom to the iKYC System")
                    login_flag = True
                    print(hello)
                    break

            # 4.2 If the face is unrecognized
            else: 
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                hello = ("Your face is not recognized")
                print(hello)
        
        # image of the picture        
        imgbytes = cv2.imencode('.png', frame)[1].tobytes() 
    
        if (time.time() > now + 15) or (login_flag == True):
            break
                
    cap.release()
    cv2.destroyAllWindows()
    
    return login_flag


def regFaceID(user_id):
    faceCapture(user_id)
    train()

def signIn_idAndpwd(customer_id, pwd):
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="u3563782", database="COMP3278_G12")
    cursor = myconn.cursor()
    select = "SELECT password FROM Customer WHERE customer_id='%s'" % (customer_id)
    password = cursor.execute(select)
    result = cursor.fetchall()
    if (len(result)==0):
        return False
    
    return (result[0][0]==pwd)



if __name__ == '__main__':
    autoSignIn()
    print(customer_id)