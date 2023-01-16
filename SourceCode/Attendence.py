import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox,QApplication,QWidget,QPushButton
from PyQt5 import QtWidgets
import os
import sys
class Mark:
   def __init__(self):      
      self.fob=open('attendence.txt','r')
      names = self.fob.read().split('\n')
      self.a = [x for x in names if x]
      print(self.a)
   def showDialog(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Your Attendence have been marked")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
   def msgButtonClick(self,i):
      print("Button clicked is:",i.text())
   def markattendence(self):
      try:
         conn = mysql.connector.connect(host='localhost',database='college',user='root',password='1864',port='3306')
         if conn.is_connected():
               print('Connected to MySQL database')
               mycursor = conn.cursor()
               mycursor.execute("select name from classroom;")
               myresults = mycursor.fetchall()
               hot = {39:None,40:None,41:None,44:None,93:None,91:None}
               andy = str(myresults).translate(hot)
               bunty = andy.split(' ')
               print(bunty)
         for g in bunty:
               if g in self.a:
                  get = ("update classroom set attendence=%s where name=%s;")
                  i = ("Present",g)
                  mycursor.execute(get,i)
                  conn.commit()
                  print(get)
                  print(g," is Present")
               else:
                  got = ("update classroom set attendence=%s where name=%s;")
                  j = ("Absent",g)
                  mycursor.execute(got,j)
                  conn.commit()
                  print(got)
                  print(g," is absent")
      except Error as e:
         conn.rollback()
         print(e)
      finally:
         self.showDialog()
         mycursor.close()
         conn.close()
         self.fob.close()
if __name__=='__main__':
   mk = Mark()
   mk.markattendence()
'''
def window():
   app = QApplication(sys.argv)
   win = QWidget()
   button1 = QPushButton(win)
   button1.setText("Show dialog!")
   button1.move(50,50)
   button1.clicked.connect(markattendence)
   win.setWindowTitle("Click button")
   win.show()
   sys.exit(app.exec_())
'''

'''
if __name__ == '__main__': 
   window()
   '''
'''
def window():
   app = QApplication(sys.argv)
   win = QWidget()
   button1 = QPushButton(win)
   button1.setText("Show dialog!")
   button1.move(50,50)
   button1.clicked.connect(showDialog)
   win.setWindowTitle("Click button")
   win.show()
   sys.exit(app.exec_())
	
def showDialog():
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("Message box pop up window")
   msgBox.setWindowTitle("QMessageBox Example")
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
   
def msgButtonClick(i):
   print("Button clicked is:",i.text())
	
if __name__ == '__main__': 
   window()
'''
