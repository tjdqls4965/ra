import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("login.ui")[0]
class log(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.setWindowTitle('로그인하기')
        self.join_btn.clicked.connect(self.join)
        self.move_login.clicked.connect(self.login_stack)
        self.join_page.clicked.connect(self.join_stack)
        self.login_action.clicked.connect(self.login)
        self.main_btn.clicked.connect(self.go_main)
        self.member = False
        # DB 연결

    def login_stack(self):
        self.stackedWidget.setCurrentIndex(1)
    def join_stack(self):
        self.stackedWidget.setCurrentIndex(0)
    def go_main(self):
        self.parent().setCurrentIndex(0)


    def login(self):
        print("2222")
        self.conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='ssb', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT ID,비밀번호 FROM student')
        self.id_data=self.cursor.fetchall()
        # self.cursor.execute('SELECT 비밀번호 FROM student')
        # self.ps_data=self.cursor.fetchall()
        # print(self.id_data)
        self.login_id=self.id_2.text()
        # print(self.login_id)
        self.login_ps=self.ps_2.text()



        for i in self.id_data:
            if self.login_id == i[0] and self.login_ps == i[1]:

                return self.login_id











    def join(self):
        self.conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='ssb', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM student')
        self.b = self.cursor.fetchall()
        self.id=self.id_join.text()
        self.ps=self.ps_join.text()
        self.ps_look=self.ps_look.text()
        self.name=self.name_join.text()
        self.id_list=[]


        for i in range(0,len(self.b)):
            self.id_list.append(self.b[i][1])
        print(self.id_list)


        if self.id != '' and self.ps != '' and self.ps_look != '' and self.name != '':
            QMessageBox.information(self, '요건충족', 'dsadsa')
            if self.id in self.id_list:
                QMessageBox.warning(self, '아이디 중복', '중복 아이디 오류')
                print("중복!!!!!!!")
            else:
                QMessageBox.information(self, '통과 아이디', '중복확인 성공')
                print("아이디 통과 @@@@")
                if self.ps != self.ps_look:
                    QMessageBox.warning(self, '비밀번호 오류', '오류 비밀번호')
                else:
                    QMessageBox.information(self, '회원가입 완료', '맞음 비밀번호')
                    self.cursor.execute("set SQL_SAFE_UPDATES = 0")
                    self.cursor.execute(f'update student set ID="{self.id}",비밀번호="{self.ps}" WHERE 이름="{self.name}"')
                    #
                    # self.cursor.execute("set SQL_SAFE_UPDATES = 1")
                    self.conn.commit()
                    self.conn.close()





        else:
            QMessageBox.warning(self, '필수요소', 'sdasdsa')  # 이거나옴







if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = log()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
