import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QMainWindow):
    bus1_cnt=0 # 버스 1 카운팅

    def __init__(self):
        super().__init__()
        uic.loadUi('./test/busstop.ui',self)

        self.initDB()

        # 버튼 시그널 작성
        #self.bus1Plus.clicked.connect(self.bus1PlusClicked)

    #def bus1PlusClicked(self):
        

    def initDB(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='12345',
                                  db='bus',charset='utf8')#host='210.119.12.69' 으로 바꿔야함
        
        cur=self.conn.cursor() #커서
        query='''
        SELECT bus_cnt
          FROM bus_table 
         WHERE bus_num = '100-1'
        '''

        cur.execute(query)
        data=cur.fetchone()
        self.bus1Cnt.setText(str(data[0]))
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=qtApp()
    ex.show()
    sys.exit(app.exec_())