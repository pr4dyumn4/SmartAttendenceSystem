import qrcode as pq
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox
def showDialog():
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("Your QR have been Genrated")
   msgBox.setWindowTitle("QMessageBox Example")
   msgBox.setStandardButtons(QMessageBox.Ok )
   msgBox.buttonClicked.connect(msgButtonClick)
   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
   
def msgButtonClick(i):
   print("Button clicked is:",i.text())
def GenrateQR():
    try:
        conn = mysql.connector.connect(host='localhost',database='college',user='root',password='1864',port='3306')
        if conn.is_connected():
            print('Connected to MySQL database')
            mycursor = conn.cursor()
            mycursor.execute("select name from classroom;")
            myresults = mycursor.fetchall()
            h = {39:None,40:None,41:None,44:None,93:None,91:None}
            a = str(myresults).translate(h)
            b = a.split(' ')
            conn.commit()
            print(b)
            for i in b:
                 image = pq.make(i)
                 image.save(f'QRCodes\{i}.png')
                 print(i)
    except Error as e:
        print(e)
    finally:
        showDialog()
        mycursor.close()
        conn.close()
 
