import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ikyc_login import IKYC_Login
from ikyc_signup import IKYC_SignUp
import autoSignIn #Initiating auto sign-in sys.


###IMPORTANT###
###The "username" variable in the UI System refers to the user id###

class UIKernel(QtWidgets.QMainWindow):
    #Potential Variables
    #self.loginUI: The GUI of login window.
    #self.username: The username of the customer.
    #self.signUpUsername: The username prompted by the customer in order to sign up
    #self.signUpPassword: The password provided by the customer to sign up


    def __init__(self):
        super().__init__()
        self.loginUI = IKYC_Login()
        self.signupUI = IKYC_SignUp()
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

    def loginUI_toRegisterPage(self):
        print("UI kernel: change to register page.")
        self.signupUI.setupUi(self)
        self.signupUI_connectionInit()
        self.show()

    ############################################################################
    #Logic functions related to signup page
    ############################################################################
    def signupUI_connectionInit(self):
        self.signupUI.commandlink_signUpButton.clicked.connect(self.signupUI_onClickSignUpButton)
        self.signupUI.commandlink_backButton.clicked.connect(self.signupUI_toLoginPage)

    def signupUI_onClickSignUpButton(self):
        self.signupUI_captureUsernameAndPassword()


    def signupUI_captureUsernameAndPassword(self):
        self.signUpUsername = self.signupUI.lineedit_username.text()
        self.signUpPassword = self.signupUI.lineedit_password.text()
        print("UIKernel: captured signup username: " + self.signUpUsername)
        print("UIKernel: captured signup password: " + self.signUpPassword)

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


    

