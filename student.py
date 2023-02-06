import pymysql as p
import requests
import xmltodict
import json
import sys

from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5 import uic


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


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

        # 소켓 생성
        # self.initialize_socket()

        # 학생 문의하기
        self.qna_send.clicked.connect(self.qnalist)

        # 학생 학습하기
        self.studylistWidget.itemClicked.connect(self.learning)
        self.studylistWidget.itemDoubleClicked.connect(self.learning)
        self.exam_test.clicked.connect(self.test)

        # 학생 상담하기
        self.chatsend_btn.clicked.connect(self.sendchat)

    # def initialize_socket(self):
    #     ip = input("서버 IP를 입력해주세요(default=10.10.21.118): ")
    #     if ip == '':
    #         ip = '10.10.21.118'
    #     port = 7979
    #
    #     # TCP socket을 생성하고 server와 연결
    #     self.client_socket = socket(AF_INET, SOCK_STREAM)
    #     self.client_socket.connect((ip, port))

    def login_stack(self):
        self.stackedWidget.setCurrentIndex(3)
        self.id_2.clear()
        self.ps_2.clear()

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
                self.name_label.setText(f"{self.d[0][0]}님 반갑습니다")
                return self.login_id

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
            QMessageBox.information(self, ' ','확인중')
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
                    self.c.execute(f'insert into ap.student values("{self.id}","{self.ps}","{self.name}","{self.div}")')
                    self.c.commit()
                    self.conn.close()

        else:
            QMessageBox.warning(self, ' ','회원가입 성공')  # 이거나옴

        # 회원가입 성공시 초기화
        self.id_join.clear()
        self.ps_join.clear()
        # self.ps_look.clear()
        self.name_join.clear()
        self.div_join.clear()

    def qna(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.open_db()
        self.c.execute("SELECT * FROM ap.qnaboard")
        self.questionlist = self.c.fetchall()

        if self.questionlist:
            self.qnalistWidget.setRowCount(len(self.questionlist))
            self.qnalistWidget.setColumnCount(len(self.questionlist[0]))
            self.qnalistWidget.setHorizontalHeaderLabels(['이름','질문내용', '답변여부'])
            for i in range(len(self.questionlist)):
                for j in range(len(self.questionlist[i])):
                    self.qnalistWidget.setItem(i, j, QTableWidgetItem(str(self.questionlist[i][j])))
            self.qnalistWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # 학생용 문의하기 게시판 전송버튼 클릭시 실행되는 메서드
    def qnalist(self):
        qnaname = self.d[0][0]
        qnamessage = self.qna_line.text()

        # qnasend_List = ['문의하기', qnaname, qnamessage]
        # qnalist = json.dumps(qnasend_List)  # json.dumps로 리스트의 값들 바이트형으로 바꿔줌
        # print(qnasend_List)
        # self.client_socket.send(qnalist.encode())  # 연결된 소켓(서버)에 채팅 로그 데이터 보내줌

        self.open_db()
        self.c.execute(f"INSERT INTO ap.qnaboard (ID,message) VALUES ('{self.d[0][0]}','{qnamessage}');")
        self.conn.commit()
        self.conn.close()
        self.qna()

        # 작성후 문의사항 초기화
        self.qna_line.clear()

    def study(self):
        self.studylistWidget.clear()
        self.stackedWidget_2.setCurrentIndex(1)

        # 인증키 저장
        key = "4Y1VQ%2BFCILQgfBdtfbv2AGShcA9czXwJPhSXne622ujf7MWF8FHODnOX%2B7QWvUxzm2e81Njv464DtuNT4OKygQ%3D%3D"
        # 인증키 정보가 들어간 url 저장
        url = f"http://openapi.nature.go.kr/openapi/service/rest/InsectService/isctPrtctList?serviceKey={key}"

        content = requests.get(url).content                     # request 모듈을 이용해서 정보 가져오기(byte형태로 가져와지는듯)
        dict = xmltodict.parse(content)                         # xmltodict 모듈을 이용해서 딕셔너리화 & 한글화
        jsonString = json.dumps(dict, ensure_ascii=False)       # json.dumps를 이용해서 문자열화(데이터를 보낼때 이렇게 바꿔주면 될듯)
        jsonObj = json.loads(jsonString)                        # 데이터 불러올 때(딕셔너리 형태로 받아옴)

        for item in jsonObj['response']['body']['items']['item']:
            self.studylistWidget.addItem(item['insctofnmkrlngnm'])
            print(item['insctFamilyNm'])

            # print(item['imgUrl'], item['insctFamilyNm'], item['insctOfnmScnm'],
            #       item['insctPcmtt'], item['insctPilbkNo'], item['insctofnmkrlngnm'])

        # 스크롤 하단 고정
        self.studylistWidget.scrollToBottom()

    def learning(self):
        self.detaillist.clear()
        # 리스트위젯에서 선택한 곤충의 이름 표시하기
        a = self.studylistWidget.currentItem().text()
        self.studyname_line.setText(a)
        print(a)
        self.open_db()
        # 선택한 곤충에 따른 이미지 송출을 위한 쿼리문
        self.c.execute(f"select image from ap.learn where name = '{a}'")
        self.image = self.c.fetchall()


        for i in range(len(self.image)):
            print(self.image)
            self.detaillist.addItem(f"[{self.image[i][0]}]")
            self.detaillist.scrollToBottom()


    # 문제풀이 시작
    def test(self):

        self.open_db()
        self.c.execute("select qu from ap.exam")
        self.exam = self.c.fetchall()
        print(self.exam)

        for i in range(len(self.exam)):
            print(self.exam)
            self.examlist.addItem(f"[{self.exam[i][0]}]")
            self.examlist.scrollToBottom()

    def chat(self):
        self.stackedWidget_2.setCurrentIndex(2)

    def sendchat(self):
        message = self.chatline.text()
        message_datetime = datetime.now().strftime("%D %T")
        self.chatlistWidget.addItem(f"{self.d[0][0]} {[message_datetime]}\n >>> {message}")

        print(message)

    def mypage(self):
        self.stackedWidget_2.setCurrentIndex(3)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = log()
    myWindow.show()
    app.exec_()
