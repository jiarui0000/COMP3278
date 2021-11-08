# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ikyc_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class IKYC_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_right_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_right_pic.setGeometry(QtCore.QRect(260, 0, 700, 600))
        self.label_right_pic.setText("")
        self.label_right_pic.setPixmap(QtGui.QPixmap("GUI_Login_Page_Pic/right_background.png"))
        self.label_right_pic.setScaledContents(True)
        self.label_right_pic.setObjectName("label_right_pic")

        self.login_frame_label = QtWidgets.QLabel(self.centralwidget)
        self.login_frame_label.setGeometry(QtCore.QRect(70, 120, 561, 351))
        self.login_frame_label.setText("")
        self.login_frame_label.setPixmap(QtGui.QPixmap("GUI_Login_Page_Pic/rounded_rectangle.png"))
        self.login_frame_label.setScaledContents(True)
        self.login_frame_label.setObjectName("login_frame_label")

        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 241, 101))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("GUI_Login_Page_Pic/ikyc_logo_transparent.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")

        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(-10, -10, 971, 611))
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("GUI_Login_Page_Pic/solidwhite.png"))
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")

        self.label_loginText = QtWidgets.QLabel(self.centralwidget)
        self.label_loginText.setGeometry(QtCore.QRect(140, 180, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_loginText.setFont(font)
        self.label_loginText.setTextFormat(QtCore.Qt.PlainText)
        self.label_loginText.setObjectName("label_loginText")

        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(140, 260, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")

        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(140, 320, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")

        self.commandlink_loginbutton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandlink_loginbutton.setGeometry(QtCore.QRect(150, 380, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.commandlink_loginbutton.setFont(font)
        self.commandlink_loginbutton.setIconSize(QtCore.QSize(30, 30))
        self.commandlink_loginbutton.setObjectName("commandlink_loginbutton")
        #self.commandlink_loginbutton.clicked.connect(self.loginButtonClicked)

        self.commandlink_loginWithFaceID = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandlink_loginWithFaceID.setGeometry(QtCore.QRect(360, 380, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.commandlink_loginWithFaceID.setFont(font)
        self.commandlink_loginWithFaceID.setIconSize(QtCore.QSize(30, 30))
        self.commandlink_loginWithFaceID.setObjectName("commandlink_loginWithFaceID")
        #self.commandlink_loginWithFaceID.clicked.connect(self.loginWithFaceIDClicked)

        self.commandlink_signUp = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandlink_signUp.setGeometry(QtCore.QRect(20, 530, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.commandlink_signUp.setFont(font)
        self.commandlink_signUp.setIconSize(QtCore.QSize(30, 30))
        self.commandlink_signUp.setObjectName("commandlink_signUp")

        self.lineedit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_username.setGeometry(QtCore.QRect(260, 260, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.lineedit_username.setFont(font)
        self.lineedit_username.setObjectName("linedit_username")

        self.lineedit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_password.setGeometry(QtCore.QRect(260, 320, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.lineedit_password.setFont(font)
        self.lineedit_password.setObjectName("lineedit_password")
        self.lineedit_password.setEchoMode(QtWidgets.QLineEdit.Password) #Mask the password.

        self.label_background.raise_()
        self.label_right_pic.raise_()
        self.login_frame_label.raise_()
        self.label_logo.raise_()
        self.label_loginText.raise_()
        self.label_username.raise_()
        self.label_password.raise_()
        self.commandlink_loginbutton.raise_()
        self.commandlink_loginWithFaceID.raise_()
        self.commandlink_signUp.raise_()
        self.lineedit_username.raise_()
        self.lineedit_password.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iKYC Login"))
        self.label_loginText.setText(_translate("MainWindow", "Welcome to the iKYC system!"))
        self.label_username.setText(_translate("MainWindow", "CustomerID"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.commandlink_loginbutton.setText(_translate("MainWindow", "Login"))
        self.commandlink_loginWithFaceID.setText(_translate("MainWindow", "Login with FaceID"))
        self.commandlink_signUp.setText(_translate("MainWindow", "Create a new account!"))
    

    def showErrorPopUpWindow(self, messageText: str):
        popUp = QMessageBox()
        popUp.setWindowTitle("Error...")
        popUp.setText(messageText)
        popUp.show()
        popUp.setIcon(QMessageBox.Critical)
        popUp.setStandardButtons(QMessageBox.Ok)
        popUp.exec_()

    def showFaceRecognizingWindow(self):
        self.faceRecogPopUp = QMessageBox()
        self.faceRecogPopUp.setWindowTitle("Recognizing your face...")
        self.faceRecogPopUp.setText("Recognizing your face...")
        self.faceRecogPopUp.show()
        self.faceRecogPopUp.setIcon(QMessageBox.Information)
        self.faceRecogPopUp.setStandardButtons(None)
        self.faceRecogPopUp.exec_()

    def closeFaceRecognizingWindow(self):
        self.faceRecogPopUp.done(1)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = IKYC_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
