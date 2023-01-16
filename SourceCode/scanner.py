import time
import cv2
from cv2 import VideoWriter_fourcc
import pyzbar.pyzbar as pb
from PIL import Image
import numpy as np
import mysql.connector
from mysql.connector import Error
from Attendence import Mark
from PyQt5.QtWidgets import QMessageBox
# url = 'http://192.168.1.6:8080/video'

class Camera(): 
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Prepare the camera...
         
        self.video = cv2.VideoWriter('video/webcam.avi', VideoWriter_fourcc(*'MP42'), 25.0, (640,480))
        cv2.getWindowProperty('Demo', cv2.WND_PROP_VISIBLE)
        conn = mysql.connector.connect(host='localhost',database='college',user='root',password='1864',port='3306')
        self.names = []
        if conn.is_connected():
            print('Connected to MySQL database')
            mycursor = conn.cursor()
            mycursor.execute("select name from classroom;")
            myresults = mycursor.fetchall()
            hot = {39:None,40:None,41:None,44:None,93:None,91:None}
            andy = str(myresults).translate(hot)
            self.bunty = andy.split(' ')
        print("Camera warming up ...")
    def open_markAttnded(self):
        self.mark = Mark()
        self.mark.markattendence()
    def enterData(self,z):
        if z in self.names:
                pass
        elif z in self.bunty:
            self.names.append(z)
            z=''.join(str(z))
            with open('attendence.txt', 'a') as fob:
                fob.write(z+'\n')
            return self.names
        else:
            pass
        print('Reading...')
        
    def checkData(self,data):    
        data1 = str(data)
        if data1 in self.names:
            print('Already Present')
        else:
            print('\n'+str(len(self.names)+1)+'\n'+data1)
            self.enterData(data1)
    def release_camera(self):
        self.cap.release()
        self.video.release()
        
    def showDialog(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Scanned Successfully")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def msgButtonClick(self,i):
      print("Button clicked is:",i.text())    
    def main(self):
        with open('attendence.txt', 'w') as fob:
            fob.write("")
        try:
            while True:
                _,frame = self.cap.read()
                decodedObjects = pb.decode(frame)
                for obj in decodedObjects:
                    mydata = obj.data.decode('utf-8')
                    self.checkData(mydata)
                    pts = np.array([obj.polygon],np.int32)
                    pts = pts.reshape((-1,1,2))  
                    cv2.polylines(frame,[pts],True,(255,0,255),5)  
                    pts2 = obj.rect
                    cv2.putText(frame,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_DUPLEX,0.9,(255,0,255),2)
                    time.sleep(1)  
                if _ is not None:     
                    cv2.imshow("cap", frame)
                self.video.write(frame)
                
                if cv2.waitKey(1)& 0xFF == ord('s') or cv2.getWindowProperty('cap', cv2.WND_PROP_VISIBLE) <1:   
                    cv2.destroyAllWindows()
                    break 
        except Error as e:
            print(e)
        finally:
            self.release_camera()
            self.open_markAttnded()
            self.showDialog()
            print('Scanned Successfully')
            
       
    

if __name__ == '__main__':
    cam = Camera()
    cam.main()