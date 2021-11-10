import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ikyc_login import IKYC_Login
#from ikyc_signup import IKYC_SignUp
from ikyc_signup_v2 import IKYC_SignUp_v2
from UserInfo import UserInfo
import autoSignIn #Initiating auto sign-in sys.


###IMPORTANT###
###The "username" variable in the UI System refers to the user id###

class UIKernel(QtWidgets.QMainWindow):
    #Potential Variables
    #self.loginUI: The GUI of login window.
    #self.username: The username of the customer.
    #self.regInfo: The information the customer inputs to register an account.


    def __init__(self):
        super().__init__()
        self.loginUI = IKYC_Login()
        self.signupUI = IKYC_SignUp_v2()
        self.regInfo = UserInfo()
        self.loginUI.setupUi(self)
        self.loginUI_connectionInit()
        self.show()

    ###########################################################################
    #Logic functions related to login UI. Functions related to login UI starts with "loginUI_"
    ###########################################################################
    def loginUI_connectionInit(self):
        self.loginUI.commandlink_loginbutton.clicked.connect(self.loginUI_onClickLogin)
        self.loginUI.commandlink_loginWithFaceID.clicked.connect(self.loginUI_initiateFaceID)
        self.loginUI.commandlink_signUp.clicked.connect(self.loginUI_toRegisterPage)
        self.loginUI.commandlink_forgotPwd.clicked.connect(self.loginUI_forgotPwdSequence)

    def loginUI_onClickLogin(self):
        u = self.loginUI.lineedit_username.text()
        p = self.loginUI.lineedit_password.text()
        print("UIKernel: captured username: " + u)
        print("UIKernel: captured password: " + p)
        if (len(u) == 0 or len(p) == 0):
            self.loginUI.showErrorPopUpWindow("Please input your user id or password!")
            return
        checkingResult = self.loginUI_checkUsernameAndPassword(u, p)
        if (checkingResult == True):
            self.username = u
            print("UIKernel: Successfully login with user id: " + self.username)
        elif(checkingResult == False):
            self.loginUI.showErrorPopUpWindow("Your user id or password is incorrect, try again!")
        


    def loginUI_onClickLoginWithFaceID(self):
        self.loginUI_initiateFaceID()



    def loginUI_checkUsernameAndPassword(self, username: str, password: str) -> bool:
        return autoSignIn.signIn_idAndpwd(username, password)

    def loginUI_initiateFaceID(self):
        print("UI Kernel: Initiating FaceID program...")
        self.loginUI.showFaceRecognizingWindow()
        #Sequences for initiating face ID recognition
        faceRecognitionResult = autoSignIn.autoSignIn()
        self.loginUI.closeFaceRecognizingWindow()
        if (faceRecognitionResult == True):
            self.username = autoSignIn.customer_id
            print("UIKernel: Face recognition successful, user login as: " + self.username)
        elif (faceRecognitionResult == False):
            self.loginUI.showErrorPopUpWindow("Face ID login failed, try again!")

    def loginUI_forgotPwdSequence(self):
        customer_id = self.loginUI.lineedit_username.text()
        if(len(customer_id) == 0):
            self.loginUI.showErrorPopUpWindow("Please enter your Customer ID for password recovery!")
            return
        print("UIKernel: Initiating password find-back sequence for user_id " + customer_id + " ...")




    def loginUI_toRegisterPage(self):
        print("UI kernel: change to register page.")
        self.signupUI.setupUi(self)
        self.signupUI_connectionInit()
        self.show()

    ############################################################################
    #Logic functions related to signup page
    ############################################################################
    def signupUI_connectionInit(self):
        self.signupUI.commandLinkButton_signupAndCaptureFaceID.clicked.connect(self.signupUI_onClickSignUpButton)
        self.signupUI.commandLinkButton_back.clicked.connect(self.signupUI_toLoginPage)

    def signupUI_onClickSignUpButton(self):
        self.signupUI_captureInfo()


    def signupUI_captureInfo(self):
        self.regInfo.firstName = self.signupUI.lineEdit_firstName.text()
        self.regInfo.lastName = self.signupUI.lineEdit_lastName.text()
        self.regInfo.gender = self.signupUI.comboBox_gender.currentText()

        #Handle birthday
        raw_QDate_birthday = self.signupUI.dateEdit_birthday.date() #QDate-Type return
        self.regInfo.birthday = raw_QDate_birthday.toString(QtCore.Qt.ISODate)

        self.regInfo.certification_type = self.signupUI.comboBox_personalIDType.currentText()
        self.regInfo.id_number = self.signupUI.lineEdit_idNumber.text()

        #Handle password
        if(self.signupUI.lineEdit_password.text() != self.signupUI.lineEdit_password_confirm.text()):
            self.signupUI.showErrorPopUpWindow("The confirming password is different from the password you input for the first time, try again!")
        else:
            self.regInfo.password = self.signupUI.lineEdit_password.text()

        self.regInfo.email = self.signupUI.lineEdit_email.text()
        self.regInfo.phoneNumber = self.signupUI.lineEdit_phone_num.text()
        
        print("UIKernel: Captured reg info:\n")
        print(self.regInfo.firstName + "\n")
        print(self.regInfo.lastName + "\n")
        print(self.regInfo.gender + "\n")
        print(self.regInfo.birthday + "\n")
        print(self.regInfo.certification_type + "\n")
        print(self.regInfo.id_number + "\n")
        print(self.regInfo.password + "\n")
        print(self.regInfo.email + "\n")
        print(self.regInfo.phoneNumber + "\n")



    def signupUI_toLoginPage(self):
        print("UI kernel: change to login page.")
        self.loginUI.setupUi(self)
        self.loginUI_connectionInit()
        self.show()










#Init the app and get running.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    UIKernelWindow = UIKernel()
    sys.exit(app.exec_())


    

