import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QMainWindow):
    conn = None

    def __init__(self):
        super().__init__()
        uic.loadUi('./test/busstop.ui', self)
        self.setWindowIcon(QIcon('./Parts1/ExamMySQL/bustop.png'))
        self.setWindowTitle('버스탑앱 실시간 위치정보 프로그램 v0.1')
        self.initDB()

    # 버튼시그널
        self.bus1Plus.clicked.connect(self.bus1PlusClicked)
        self.bus1Minus.clicked.connect(self.bus1MinusClicked)
        self.bus2Plus.clicked.connect(self.bus2PlusClicked)
        self.bus2Minus.clicked.connect(self.bus2MinusClicked)
        self.bus3Plus.clicked.connect(self.bus3PlusClicked)
        self.bus3Minus.clicked.connect(self.bus3MinusClicked)
##########################################################
    def bus1PlusClicked(self):
        self.count1 += 1 
        self.setting()
        if self.count1 >= 1: # 버튼을 누르고 값이 1이상일때
            QMessageBox.warning(self, '알림', '10번 버스 대기 예약에 성공했습니다.')
            self.bus1Plus.setDisabled(True)
            self.bus1Minus.setEnabled(True)
            return  # 함수를 빠져나감
        
    def bus2PlusClicked(self):
        self.count2 += 1 
        self.setting()
        if self.count1 >= 1: 
            QMessageBox.warning(self, '알림', '100-1번 버스 대기 예약에 성공했습니다.')
            self.bus2Plus.setDisabled(True)
            self.bus2Minus.setEnabled(True)

    def bus3PlusClicked(self):
        self.count3 += 1 
        self.setting()
        if self.count1 >= 1:
            QMessageBox.warning(self, '알림', '155번 버스 대기 예약에 성공했습니다.')
            self.bus3Plus.setDisabled(True)
            self.bus3Minus.setEnabled(True)
##########################################################
    def bus1MinusClicked(self):
        if self.count1 == 0:
            pass
        else:
            reply = QMessageBox.question(self, '알림', '정말로 취소하시겠습니까?', QMessageBox.Yes | QMessageBox.No, 
                                        QMessageBox.Yes)
            if reply == QMessageBox.No:
                return
            else:
                self.count1 -= 1 
                self.bus1Plus.setEnabled(True)
                self.bus1Minus.setDisabled(True)
                self.setting()

    def bus2MinusClicked(self):
        if self.count2 == 0:
            pass
        else:
            reply = QMessageBox.question(self, '알림', '정말로 취소하시겠습니까?', QMessageBox.Yes | QMessageBox.No, 
                                        QMessageBox.Yes)
            if reply == QMessageBox.No:
                return
            else:
                self.count2 -= 1 
                self.bus2Plus.setEnabled(True)
                self.bus2Minus.setDisabled(True)
            self.setting()
    
    def bus3MinusClicked(self):
        if self.count3 == 0:
            pass
        else:
            reply = QMessageBox.question(self, '알림', '정말로 취소하시겠습니까?', QMessageBox.Yes | QMessageBox.No, 
                                        QMessageBox.Yes)
            if reply == QMessageBox.No:
                return
            else:
                self.count3 -= 1 
                self.bus3Plus.setEnabled(True)
                self.bus3Minus.setDisabled(True) 
            self.setting()        
##########################################################
    def initDB(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query='''
        SELECT bus_cnt
          FROM bus_table
         WHERE bus_num = %s
        '''
        cur.execute(query,('100-1'))
        data=cur.fetchone()
        self.count1 = int(data[0])
        self.bus1Cnt.setText(str(data[0]))

        cur.execute(query,('155'))
        data=cur.fetchone()
        self.count2 = int(data[0])
        self.bus2Cnt.setText(str(data[0]))

        cur.execute(query,('10'))
        data=cur.fetchone()
        self.count3 = int(data[0])
        self.bus3Cnt.setText(str(data[0]))


##########################################################

    def setting(self):
        self.conn = pymysql.connect(host='210.119.12.69', user='root', password='12345', db='bus', charset='utf8')
        cur = self.conn.cursor()
        query = '''UPDATE bus_table
                      SET bus_cnt = %s
                    WHERE bus_num = %s '''
        
        self.bus1Cnt.setText(str(self.count1))
        self.bus2Cnt.setText(str(self.count2))
        self.bus3Cnt.setText(str(self.count3))
        cur.execute(query, (self.count1, '100-1'))
        cur.execute(query, (self.count2, '155'))
        cur.execute(query, (self.count3, '10'))

        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())