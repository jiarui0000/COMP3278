# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trial1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import random


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.setWindowTitle('RTM Bank')
        MainWindow.setWindowTitle('RTM Bank')
        self.setStyleSheet("background-color: rgb(145,152,189);")
        # Setting up main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 877)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # add mainFrame

        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setGeometry(QtCore.QRect(210, 40, 1161, 771))
        self.mainframe.setAutoFillBackground(False)
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("frame")
        self.mainframe.setStyleSheet("background-color:white;border-radius:23px;")
        shadow_main = QGraphicsDropShadowEffect()
        shadow_main.setBlurRadius(10)
        shadow_main.setOffset(5)
        self.mainframe.setGraphicsEffect(shadow_main)

        # add sidebar
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 80, 300, 681))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color:rgb(247,248,253);border-radius:23px;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(5)
        self.frame.setGraphicsEffect(shadow)
        font1 = QtGui.QFont()
        font1.setFamily("Aqua Grotesque")
        font1.setBold(True)

        # add bank title
        title = QLabel(self.frame)
        title.setWindowFlag(Qt.FramelessWindowHint)
        title.setAttribute(Qt.WA_NoSystemBackground)
        title.setAttribute(Qt.WA_TranslucentBackground)
        title.setGeometry(QtCore.QRect(50, 30, 200, 80))
        title.setText('RTMBANK')
        title.setStyleSheet("font-size:30px;qproperty-alignment:AlignCenter;font-weight:bold;color:rgb(0,80,245);")
        title.setFont(font1)

        # add sidebar buttons
        def setup_sidebuttonbackground(index, text):
            btn1 = QLabel(self.frame)
            btn1.setGeometry(QtCore.QRect(30, 150 + index * 60, 240, 40))
            style = '''
                    #btn1 {border-radius:7px;font-size:15pt;font-weight: bold;color:black;
                        qproperty-alignment: 'AlignVCenter | AlignLeft';qproperty-wordWrap: true;background-color: rgb(247,248,253);}
                    #btn1:hover {font-size:15pt;border-radius:7px;font-weight: bold;color:rgb(42,110,245);qproperty-alignment: AlignLeft;background-color:rgb(235,239,253);}  
                '''
            font1 = QtGui.QFont()
            font1.setFamily("Avenir")
            font1.setBold(False)
            font1.setWeight(50)
            btn1.setStyleSheet(style)
            btn1.setText('                       ' + text)
            btn1.setObjectName('btn1')
            btn1.setFont(font1)
            icon = QtWidgets.QLabel(self.frame)
            icon.setGeometry(QtCore.QRect(60, 150 + 60 * index, 40, 40))
            icon.setScaledContents(True)
            icon.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            if index == 0:
                icon_name = 'home'
            elif index == 1:
                icon_name = 'Accounts'
            elif index == 2:
                icon_name = 'Transactions'
            elif index == 3:
                icon_name = 'Investment'
            else:
                icon_name = 'logout'
            self.im = QPixmap("./icons/" + icon_name + ".png")
            icon.setPixmap(self.im.scaled(160, 160, Qt.IgnoreAspectRatio))
            icon.setWindowFlag(Qt.FramelessWindowHint)
            icon.setAttribute(Qt.WA_NoSystemBackground)
            icon.setAttribute(Qt.WA_TranslucentBackground)
            return btn1, icon

        self.btn1, self.icon1 = setup_sidebuttonbackground(0, 'Home')
        self.btn2 = setup_sidebuttonbackground(1, 'Accounts')
        self.btn3 = setup_sidebuttonbackground(2, 'Transactions')
        self.btn4 = setup_sidebuttonbackground(3, 'Investment')
        self.btn5 = setup_sidebuttonbackground(7, 'Logout')

        # add wallet elements
        def init_text(name,text,geo,style="font-size:20pt;",font=font1,frame=self.mainframe):
            object = QLabel(frame)
            object.setGeometry(QtCore.QRect(geo[0],geo[1],geo[2],geo[3]))
            object.setObjectName(name)
            object.setStyleSheet(style)
            object.setText(text)
            object.setFont(font)
            object.setWindowFlag(Qt.FramelessWindowHint)
            object.setAttribute(Qt.WA_NoSystemBackground)
            object.setAttribute(Qt.WA_TranslucentBackground)
            return object
        def set_wallet_frame(index):
            wallet = QFrame(self.mainframe)
            wallet.setGeometry(QtCore.QRect(220 + 180 * index, 140, 170, 132))
            wallet.setObjectName('wallet')
            style_wallet_frame = '''
                QFrame {border-radius:7px;background-color:white;border:3px solid rgb(46,169,223);}
                QFrame:hover {background-color:white;border: 5px solid rgb(46,169,223);}
            '''
            wallet.setStyleSheet(style_wallet_frame)
            if index == 0:
                account_type = 'CURRENT\nACCOUNT'
            elif index == 1:
                account_type = 'CREDIT\nACCOUNT'
            else:
                account_type = 'DEBIT\nACCOUNT'
            acc_type=init_text('acc_type',account_type,[10,5,150,80],"font-size:17pt",frame=wallet)

            balance_text="$"+"{:,}".format((int(random.random() * 1000000)))
            balance=init_text('balance',balance_text,[10,70,111,51],'font-size:16pt;color:black;',frame=wallet)
            # balance = QLabel(wallet)
            # balance.setGeometry(QtCore.QRect(10, 70, 111, 51))
            # balance.setStyleSheet('font-size:20pt;border:0px,color:black;')
            return wallet
        self.wallet_frame1 = set_wallet_frame(0)
        self.wallet_frame2 = set_wallet_frame(1)
        wallet_frame3 = set_wallet_frame(2)

        self.wallet_title=init_text('wallet_title','Accounts',[220,50,300,100],"font-size:30pt")
        self.balance_trend_title=init_text('balance_trend_title','Balance Trend',[220,300,400,30],"font-size:30pt")

        # include user photo
        userphoto = QtWidgets.QLabel(self.mainframe)
        userphoto.setGeometry(QtCore.QRect(875, 50, 200, 300))
        userphoto.setScaledContents(True)
        userphoto.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.im = QPixmap("./images/001_result.png")
        userphoto.setPixmap(self.im)

        # greeting user
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        greeting_height = 150
        if now.hour>=18:
            greeting_text='Good Evening'
        elif now.hour>=12:
            greeting_text='Good Afternoon'
        elif now.hour>=4:
            greeting_text='Good Morning'
        else:
            greeting_text='Good Night'

        self.greetings=init_text('greetings',greeting_text+', ',[850,int(greeting_height),400,400],"font-size:30pt;")
        self.customer_name = init_text('customer_name','Elon Musk!',[850,greeting_height+50,400,400],"font-size:35pt;")
        self.lastlogintime=init_text('last_logintime','Last Login Time: '+current_time,[850,280,400,400])
        self.loginhistory=init_text('login_history_symbol','Latest Login History: ',[850,310,400,400],"font-size:15pt")
        # login history

        from matplotlib import pyplot
        balance_trend_image = QtWidgets.QLabel(self.mainframe)
        balance_trend_image.setGeometry(QtCore.QRect(200, 330, 600, 400))
        balance_trend_image.setScaledContents(True)
        balance_trend_image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.im = QPixmap("./icons/Gold Cumulative Return")
        balance_trend_image.setPixmap(self.im)
        balance_trend_image.setPixmap(self.im.scaled(3600, 2400, Qt.IgnoreAspectRatio))
        balance_trend_image.setWindowFlag(Qt.FramelessWindowHint)
        balance_trend_image.setAttribute(Qt.WA_NoSystemBackground)
        balance_trend_image.setAttribute(Qt.WA_TranslucentBackground)

        #finish home page elements construction
        home_page_elements=self.mainframe.children()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def hide_mainframe(self):
            for i in range(len(self.mainframe.children())):
                self.mainframe.children()[i].setHidden(True)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def linkHovered(self):
        print(1)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
