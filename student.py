import pymysql as p
import sys
from PyQt5.QtWidgets import *

import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("login.ui")[0]
class log(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # ui 첫페이지 고정
        self.stackedWidget.setCurrentIndex(3)
        self.setWindowTitle('박보영과 함께하는 곤충농장')
        # 로그인에 필요한 이동
        self.join_btn.clicked.connect(self.join)
        self.move_login.clicked.connect(self.login_stack)
        self.join_page.clicked.connect(self.join_stack)
        self.login_action.clicked.connect(self.login)
        self.logout_btn.clicked.connect(self.login_stack)
        self.member = False

        # 학생페이지 버튼실행함수
        self.qna_btn.clicked.connect(self.qna)
        self.study_btn.clicked.connect(self.study)
        self.chat_btn.clicked.connect(self.chat)
        self.mypage_btn.clicked.connect(self.mypage)


    def login_stack(self):
        self.stackedWidget.setCurrentIndex(3)
    def join_stack(self):
        self.stackedWidget.setCurrentIndex(0)

    # DB 연결
    def open_db(self):
        self.conn = p.connect(host='10.10.21.125', port=3306, user='root', password='1234',
                              db='ap', charset='utf8')
        self.c = self.conn.cursor()

    def login(self):
        # 로그인후 마이페이지로 고정
        self.stackedWidget_2.setCurrentIndex(3)
        self.open_db()
        self.c.execute('SELECT ID,PS FROM student')

        self.id_data = self.c.fetchall()
        self.login_id = self.id_2.text()
        self.login_ps = self.ps_2.text()

        for i in self.id_data:
            if self.login_id == i[0] and self.login_ps == i[1]:
                print(self.login_id)
                self.stackedWidget.setCurrentIndex(1)
                self.c.execute(f"select name from student where ID ='{self.login_id}'")
                self.d = self.c.fetchall()
                print(self.d[0][0])
                self.name_label.setText(f"{self.d[0][0]}님 안녕하세요")
                return self.login_id

        self.id_2.clear()
        self.ps_2.clear()

    def join(self):
        self.open_db()
        self.c.execute('SELECT * FROM student')
        self.b = self.c.fetchall()
        self.id = self.id_join.text()
        self.ps = self.ps_join.text()
        self.ps_look = self.ps_look.text()
        self.name = self.name_join.text()
        self.div = self.div_join.text()
        self.id_list = []

        for i in range(0,len(self.b)):
            self.id_list.append(self.b[i][0])
        print(self.id_list)

        if self.id != '' and self.ps != '' and self.ps_look != '' and self.name != '':
            QMessageBox.information(self, '요건충족','확인중')
            if self.id in self.id_list:
                QMessageBox.warning(self, '아이디 중복', '중복 아이디 오류')
                print("중복입니다")
            else:
                QMessageBox.information(self, '통과 아이디', '중복확인 성공')
                print("아이디 통과")
                if self.ps != self.ps_look:
                    QMessageBox.warning(self, '비밀번호 오류', '오류 비밀번호')
                else:
                    QMessageBox.information(self, '회원가입 완료', '맞음 비밀번호')
                    self.c.execute("set SQL_SAFE_UPDATES = 0")
                    self.c.execute(f'insert into student values("{self.id}","{self.ps}","{self.name}","{self.div}")')
                    self.c.commit()
                    self.conn.close()

        else:
            QMessageBox.warning(self, '필수요소','회원가입 성공')  # 이거나옴

        # 회원가입 성공시 초기화
        self.id_join.clear()
        self.ps_join.clear()
        # self.ps_look.clear()
        self.name_join.clear()
        self.div_join.clear()



    def qna(self):
        self.stackedWidget_2.setCurrentIndex(0)

    def study(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def chat(self):
        self.stackedWidget_2.setCurrentIndex(2)

    def mypage(self):
        self.stackedWidget_2.setCurrentIndex(3)




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = log()
    myWindow.show()
    app.exec_()
