import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime as dt
import mysql.connector

path = 'images'
userImages = []   # List of Images
userNames = []   # List Of Users
userImageList = os.listdir(path)   # Loading Users Images
for user in userImageList:
    userImg = cv2.imread(f'{path}/{user}')
    userImages.append(userImg)
    userNames.append(os.path.splitext(user)[0])


def encodings(u_images):
    enlist = []    # Encode List
    for img in u_images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        enlist.append(encode)
    return enlist


def attendance(name, crtime, crdate):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aditi@246_Sri",
        database='attendance'
    )
    curobj = db.cursor()
    queryextract = "SELECT * FROM ATTENDEES"
    curobj.execute(queryextract)
    lname = curobj.fetchall()
    listofnames = []
    listofdates = []

    for row in lname:
        listofnames.append(row[0])
        listofdates.append(row[2])

    if (name, crdate) not in zip(listofnames, listofdates):
        query = "INSERT INTO ATTENDEES VALUES (%s, %s, %s)"
        val = (name, crtime, crdate)
        curobj.execute(query, val)
        db.commit()
        print("Record Entered")


encodeListKnown = encodings(userImages)
print("Encodings Completed Successfully")

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)
    encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = userNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
            cv2.line(frame, (x1, y1), (x1+20, y1), (0, 255, 0), 4)
            cv2.line(frame, (x1, y1), (x1, y1+20), (0, 255, 0), 4)
            cv2.line(frame, (x2, y1), (x2-20, y1), (0, 255, 0), 4)
            cv2.line(frame, (x2, y1), (x2, y1+20), (0, 255, 0), 4)
            cv2.line(frame, (x1, y2), (x1+20, y2), (0, 255, 0), 4)
            cv2.line(frame, (x1, y2), (x1, y2-20), (0, 255, 0), 4)
            cv2.line(frame, (x2, y2), (x2-20, y2), (0, 255, 0), 4)
            cv2.line(frame, (x2, y2), (x2, y2-20), (0, 255, 0), 4)
            cv2.putText(frame, name, (x1+25, y2+30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
            cv2.putText(frame, "Press Esc To Close", (25, 25), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
            now = dt.now()
            crtime = now.strftime('%H:%M:%S')
            crdate = now.strftime('%d/%m/%Y')
            attendance(name, str(crtime), str(crdate))

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
