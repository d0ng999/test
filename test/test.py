import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * # QIcon은 여기 있음
import pymysql

class qtApp(QMainWindow):
    conn = None
    cnt = 0
    curIdx = 0 #현재 데이터 PK

    def __init__(self):
        super().__init__()
        uic.loadUi('./test/busstop.ui', self)
        # self.setWindowIcon(QIcon('./studyPyQt/address-book.png'))
        self.setWindowTitle('BusStop v0.5')

        self.initDB()

        self.bus1Minus.clicked.connect(self.bus1MinusClicked)
        self.bus1Plus.clicked.connect(self.bus1PlusClicked)
        # self.tblBusCnt.clicked.connect(self.tblBusCntClicked)


    # def tblBusCntClicked(self):
    #     rowIndex = self.tblBusCnt.currentRow()
    #     self.curIdx = int(self.tblBusCnt.item(rowIndex, 1).text())
    #     print(self.curIdx)

    def bus1MinusClicked(self):
        # self.cntIdx -= 1
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345',
                                        db='bus', charset='utf8')
        query = 'UPDATE bus.bus_talbe SET bus_cnt = bus_cnt - 1;'
        cur = self.conn.cursor()
        cur.execute(query, (self.curIdx))

        self.conn.commit()
        self.conn.close()
        self.initDB()
 

    def bus1PlusClicked(self):
        # self.cntIdx += 1
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345',
                                        db='bus', charset='utf8')
        query = 'UPDATE bus.bus_table SET bus_cnt = bus_cnt + 1;'
        cur = self.conn.cursor()
        cur.execute(query, (self.curIdx))
    
    def initDB(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345',
                                        db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''SELECT bus_cnt
                     FROM bus.bus_table'''
        cur.execute(query)
        rows = cur.fetchall()

        self.makeTable(rows)
        self.conn.close()
    
    # def makeTable(self, row):
    #     self.tblBusCnt.setColumnCount(1)
    #     self.tblBusCnt.setRowCount(1)
    #     self.tblBusCnt.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # count = row[0]
        # self.tblBusCnt.setItem(0, 1, QTableWidgetItem(count))

# UPDATE bus.bus_table SET bus_cnt = bus_cnt + 1;

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())