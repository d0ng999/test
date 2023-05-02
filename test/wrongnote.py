# 주소록 GUI 프로그램 - MySQL 연동
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * # QIcon은 여기 있음
import pymysql

class qtApp(QMainWindow):
    conn = None
    curIdx = 0 #현재 데이터 PK

    def __init__(self):
        super().__init__()
        uic.loadUi('./wrongnote.ui', self)
        # self.setWindowIcon(QIcon('./studyPyQt/address-book.png'))
        self.setWindowTitle('오답노트 v0.5')

        self.initDB() # DB초기화

        # 버튼 시그널/슬롯함수 지정
        # self.btnHide.clicked.connect(self.btnHideAns)
        # self.btnSave.clicked.connect(self.btnShowAns)
        self.btnHideAns.clicked.connect(self.btnHideAnsClicked)
        self.btnShowAns.clicked.connect(self.btnShowAnsClicked)
        self.btnOpenPro.clicked.connect(self.btnOpenProClicked)
        self.btnRandPro.clicked.connect(self.btnRandProClicked)
    
    def btnShowAnsClicked(self, rows):

        self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                        db='wrongnote', charset='utf8')
        cur = self.conn.cursor()
        query = '''ALTER TABLE wrongnote
                  MODIFY COLUMN Answer NVARCHAR(100) VISIBLE''' # 멀티라인 문자열 편함!
        cur.execute(query)
        self.initDB()

    def btnHideAnsClicked(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                        db='wrongnote', charset='utf8')
        cur = self.conn.cursor()
        query = '''ALTER TABLE wrongnote
                  MODIFY COLUMN Answer NVARCHAR(100) INVISIBLE''' # 멀티라인 문자열 편함!
        cur.execute(query)
        self.initDB()



    def btnOpenProClicked(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                        db='wrongnote', charset='utf8')
        cur = self.conn.cursor()
        query = '''SELECT *
                     FROM wrongnote''' # 멀티라인 문자열 편함!
        cur.execute(query)
        rows = cur.fetchall()

            # print(rows)
        self.makeTable(rows)
        self.initDB()

    def btnRandProClicked(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                        db='wrongnote', charset='utf8')
        cur = self.conn.cursor()
        query = '''SELECT idx,
                          Contents,   
                          Answer                          
                     FROM wrongnote
                    ORDER BY RAND() LIMIT 1''' # 멀티라인 문자열 편함!
        cur.execute(query)
        rows = cur.fetchall()

            # print(rows)
        self.makeTable(rows)
        self.initDB()

    # def btnDelClicked(self):
    #     if self.curIdx == 0:
    #         QMessageBox.warning(self, '경고', '삭제할 데이터를 선택하세요.')
    #         return # 함수를 빠져나감
    #     else:
    #         reply = QMessageBox.question(self, '확인', '정말로 삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No, 
    #                                      QMessageBox.Yes)
    #         if reply == QMessageBox.No:
    #             return # 함수 빠져나감

    #         self.conn = pymysql.connect(host='localhost', user='root', password='12345',
    #                                     db='wrongnote', charset='utf8')
    #         query = 'DELETE FROM addressbook WHERE Idx = %s'
    #         cur = self.conn.cursor()
    #         cur.execute(query, (self.curIdx))

    #         self.conn.commit()
    #         self.conn.close()

    #         QMessageBox.about(self, '성공', '데이터를 삭제했습니다.')

    #         self.initDB()
    #         self.btnNewClicked()

    # def btnNewClicked(self): # 신규버튼 누르면
    #     # 라인에디트 내용 삭제 후 이름에 포커스
    #     self.txtName.setText('')
    #     self.txtPhone.setText('')
    #     self.txtEmail.setText('')
    #     self.txtAddress.setText('')
    #     self.txtName.setFocus()
    #     self.curIdx = 0 # 0은 진짜 신규!
    #     print(self.curIdx)

    # def tblcontDoubleClicked(self): #
    #     rowIndex = self.tblcont.currentRow()
    #     self.txtName.setText(self.tblcont.item(rowIndex, 1).text())
    #     self.txtPhone.setText(self.tblcont.item(rowIndex, 2).text())
    #     self.curIdx = int(self.tblcont.item(rowIndex, 0).text()) 
    #     print(self.curIdx)

    # def btnSaveClicked(self): # 저장 
    #     fullName = self.txtName.text()
    #     phoneNum = self.txtPhone.text()
    #     email = self.txtEmail.text()
    #     address = self.txtAddress.text()

    #     # print(fullName, phoneNum, email, address)
    #     # 이름과 전화번호를 입력하지 않으면 알람
    #     if fullName == '' or phoneNum == '':
    #         QMessageBox.warning(self, '주의', '이름과 핸드폰번호를 입력하세요!')
    #         return # 진행불가
    #     else:
    #         self.conn = pymysql.connect(host='localhost', user='root', password='12345',
    #                                     db='wrongnote', charset='utf8')
    #         if self.curIdx == 0: # 신규 네개 변수값 받아서 INSERT 쿼리문 만들기
    #             query = '''INSERT INTO addressbook (FullName, PhoneNum, Email, Address)
    #                             VALUES (%s, %s, %s, %s)'''
    #         else:
    #             query = '''UPDATE addressbook
    #                           SET FullName = %s
    #                             , PhoneNum = %s
    #                             , Email = %s
    #                             , Address = %s
    #                         WHERE Idx = %s'''

    #         cur = self.conn.cursor()
    #         if self.curIdx == 0:
    #             cur.execute(query, (fullName, phoneNum, email, address))
    #         else: # 업데이트
    #             cur.execute(query, (fullName, phoneNum, email, address, self.curIdx))

    #         self.conn.commit() 
    #         self.conn.close()
            
    #         if self.curIdx == 0:   # 저장성공 메시지
    #             QMessageBox.about(self, '성공', '저장 성공했습니다!')
    #         else:
    #             QMessageBox.about(self, '성공', '변경 성공했습니다!')

    #         self.initDB()  # QTableWidget 새 데이터가 출력되도록
    #         self.btnNewClicked() # 입력창 내용 없어져

    def initDB(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                    db='wrongnote', charset='utf8')
        # cur = self.conn.cursor()
        # query = '''SELECT idx,
        #                   Answer,
        #                   Contents
        #              FROM wrongnote
        #             ORDER BY RAND() LIMIT 1''' # 멀티라인 문자열 편함!
        # cur.execute(query)
        # rows = cur.fetchall()

        # # print(rows)
        # self.makeTable(rows)
        self.conn.close() # 프로그램 종료할 때 
    
    def makeTable(self, rows):
        self.tblcont.setColumnCount(3) # 0. 열갯수
        self.tblcont.setRowCount(len(rows)) # 0. 행갯수
        self.tblcont.setSelectionMode(QAbstractItemView.SingleSelection) # 1. 단일선택
        self.tblcont.setHorizontalHeaderLabels(['번호','문제내용','정답']) # 1. 열제목
        self.tblcont.setColumnWidth(0, 0) # 1. 번호는 숨김
        self.tblcont.setColumnWidth(1, 100) # 이름 열 70
        self.tblcont.setColumnWidth(2, 500) # 핸드폰 열 105
        
        self.tblcont.setEditTriggers(QAbstractItemView.NoEditTriggers) # 1. 컬럼수정금지

        for i, row in enumerate(rows):
            # row[0] ~ row[4]
            idx = row[0]
            Answer = row[2]
            Contents = row[1]

            self.tblcont.setItem(i, 0, QTableWidgetItem(str(idx)))
            self.tblcont.setItem(i, 2, QTableWidgetItem(Answer))
            self.tblcont.setItem(i, 1, QTableWidgetItem(Contents))
            

        self.stbCurrent.showMessage(f'전체 문제 수 :{len(rows)}개')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())