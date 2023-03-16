import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql

# class QPushButton(QPushButton):
#     def __init__(self, parent = None):
#         super().__init__(parent)
#         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

# class QLabel(QLabel):
#     def __init__(self, parent = None):
#         super().__init__(parent)
#         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

# class QRadioButton(QRadioButton):
#     def __init__(self, parent = None):
#         super().__init__(parent)
#         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)



class qtApp(QMainWindow):
    conn = None

    def __init__(self):
        super().__init__()
        uic.loadUi('./test/busstop5.ui', self)
        self.setWindowIcon(QIcon('./test/busstop.png'))
        self.setWindowTitle('BusStop v0.1')
        self.date = QDate.currentDate()
        self.datetime = QDateTime.currentDateTime()
        
        self.initDB()
        # self.btnBus1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.btnBus2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.btnBus3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.busPlus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.busMinus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btnBus1.setStyleSheet('background-color:rgb(100,100,255)')


        # 버튼시그널
        self.busPlus.clicked.connect(self.busPlusClicked)
        self.busMinus.clicked.connect(self.busMinusClicked)
        self.btnBus1.clicked.connect(self.btnBus1Clicked)
        self.btnBus2.clicked.connect(self.btnBus2Clicked)
        self.btnBus3.clicked.connect(self.btnBus3Clicked)
        self.btnBus1.released.connect(self.btnBusRelease)
        self.btnBus2.released.connect(self.btnBusRelease)
        self.btnBus3.released.connect(self.btnBusRelease)
    
    def btnBusRelease(self):
        self.btnBus1.setEnabled(True)
        self.btnBus2.setEnabled(True)
        self.btnBus3.setEnabled(True)

    def btnBus1Clicked(self):
        if self.btnBus1.isChecked():
            self.btnBus2.setEnabled(False)
            self.btnBus3.setEnabled(False)
            if self.busPlus.isChecked():
                self.busPlusClicked()

            elif self.busMinus.isChecked():
                self.busMinusClicked()

    def btnBus2Clicked(self):
        if self.btnBus2.isChecked():
            self.btnBus1.setEnabled(False)
            self.btnBus3.setEnabled(False)
            if self.busPlus.isChecked():
                self.busPlusClicked()

            elif self.busMinus.isChecked():
                self.busMinusClicked()

    def btnBus3Clicked(self):
        if self.btnBus3.isChecked():
            self.btnBus2.setEnabled(False)
            self.btnBus1.setEnabled(False)
            if self.busPlus.isChecked():
                self.busPlusClicked()

            elif self.busMinus.isChecked():
                self.busMinusClicked()

    def busPlusClicked(self):
        if self.btnBus1.isChecked():
            self.count1 += 1 
            self.setting1()

        elif self.btnBus2.isChecked():
            self.count2 += 1 
            self.setting2()

        elif self.btnBus3.isChecked():
            self.count3 += 1 
            self.setting3()

    def busMinusClicked(self):
        if self.btnBus1.isChecked():
            if self.count1 == 0:
                pass
            else:
                self.count1 -= 1 
                self.setting1()

        elif self.btnBus2.isChecked():
            if self.count2 == 0:
                pass
            else:
                self.count2 -= 1 
                self.setting2()

        elif self.btnBus3.isChecked():
            if self.count3 == 0:
                pass
            else:
                self.count3 -= 1 
                self.setting3()
            
    def initDB(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query='''
        SELECT bus_cnt
          FROM bus_table
         WHERE bus_num = %s
        '''
        self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleLongDate))
        cur.execute(query,('10'))
        data=cur.fetchone()
        self.count1 = int(data[0])
        self.bus1Cnt.setText(str(data[0]))

        cur.execute(query,('100-1'))
        data=cur.fetchone()
        self.count2 = int(data[0])
        self.bus2Cnt.setText(str(data[0]))

        cur.execute(query,('155'))
        data=cur.fetchone()
        self.count3 = int(data[0])
        self.bus3Cnt.setText(str(data[0]))


    def setting1(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''UPDATE bus_table
                      SET bus_cnt = %s
                    WHERE bus_num = %s '''
        
        self.bus1Cnt.setText(str(self.count1))
        cur.execute(query, (self.count1, '10'))
        self.conn.commit()
        self.conn.close()

    def setting2(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''UPDATE bus_table
                      SET bus_cnt = %s
                    WHERE bus_num = %s '''
        

        self.bus2Cnt.setText(str(self.count2))
        cur.execute(query, (self.count2, '100-1'))
        self.conn.commit()
        self.conn.close()
    
    def setting3(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''UPDATE bus_table
                      SET bus_cnt = %s
                    WHERE bus_num = %s '''

        self.bus3Cnt.setText(str(self.count3))
        cur.execute(query, (self.count3, '155'))
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())