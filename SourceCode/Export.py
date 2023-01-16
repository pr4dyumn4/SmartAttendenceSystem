
import mysql.connector as mc
import pandas as pd
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox
class Excel:
    def __init__(self):
        super().__init__()
        con = mc.connect(host='localhost',database='college',user='root',password='1864',port='3306')
        cursor = con.cursor()
        query = ("SELECT * FROM CLASSROOM;")
        cursor.execute(query)
        self.a = cursor.fetchall()
        self.all_Sid = []
        self.all_name = []
        self.all_Department = []
        self.all_year = []
        self.all_attendence = []
    def Load(self):
        for sid,name,dep,year,attendence in self.a:
            self.all_Sid.append(sid)
            self.all_name.append(name)
            self.all_Department.append(dep)
            self.all_year.append(year)
            self.all_attendence.append(attendence)
    def AddCSV(self):
       
            dic = {'StudentID':self.all_Sid,'Name':self.all_name,'Department':self.all_Department,'year':self.all_year,'attendence':self.all_attendence}
            df = pd.DataFrame(dic)
            print(df)
            df_csv = df.to_csv('outfile.csv',index=False)
            self.showDialog()
    def showDialog(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Exported Successfully It is in CSV file")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def msgButtonClick(self,i):
      print("Button clicked is:",i.text())

if __name__ == '__main__':
    CS = Excel()
    CS.Load()
    CS.AddCSV()