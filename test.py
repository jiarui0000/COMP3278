from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from demo import *
from Utils import *
import datetime

app = QtWidgets.QApplication([])
dlg = uic.loadUi("p_main.ui")
###
#default value
edit = False
poptype = "logout"


#functions
def show_message(title= "Message", message="text"):
    msg = QMessageBox()
    msg.information(None, title, message)

def timecheck():
    d_time = datetime.datetime.strptime(str(datetime.datetime.now().date())+'6:00', '%Y-%m-%d%H:%M')
    d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date())+'12:00', '%Y-%m-%d%H:%M')
    d_time2 = datetime.datetime.strptime(str(datetime.datetime.now().date())+'18:00', '%Y-%m-%d%H:%M')
    n_time = datetime.datetime.now()
    if n_time > d_time and n_time<d_time1:
        return 1
    elif n_time > d_time1 and n_time < d_time2:
        return 2
    else:
        return 3

def greeting():
    dlg.label_surname.setText(("Mr. " if checkGender(customer_id) == "male" else "Ms. ") + getSurname(customer_id))
    if timecheck() == 1:
        dlg.label.setText("Good morning,")
    elif timecheck() == 2:
        dlg.label.setText("Good afternoon,")
    else:
        dlg.label.setText("Good evening,")

def show_popup(title= "Test", message="message"):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(QMessageBox.Question)
    msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
    msg.buttonClicked.connect(popup_button)
    x = msg.exec_()

def popup_button(i):
    global poptype
    if poptype == "logout":
        if i.text() == "&Yes":
            print("excute logout")
    elif poptype == "delete1":
        print("not")

def loadAccounts():
    list=accountList(customer_id)
    print(accountList(customer_id))
    # users = helper.select("SELECT * FROM users")
    # print(users)
    for row_count, account in enumerate(list):
        dlg.tableWidget_accounts.insertRow(row_count)#row
        for column_number, data in enumerate(account):
            cell = QtWidgets.QTableWidgetItem(str(data))#one cell
            dlg.tableWidget_accounts.setItem(row_count, column_number, cell)

def init_page_profile():
    result = loadInfo(customer_id)[0]
    dlg.lineEdit_lastname.setText(result[1])
    dlg.lineEdit_firstname.setText(result[2])
    dlg.lineEdit_gender.setText(result[3])
    dlg.lineEdit_birthday.setText(str(result[4]))
    dlg.lineEdit_email.setText(result[5])
    dlg.lineEdit_phone.setText(result[6])
    dlg.lineEdit_id.setText(result[0])
    dlg.lineEdit_certi.setText(result[7])
    dlg.lineEdit_cid.setText(str(result[8]))
    # for i in range(dlg.groupBox)
    dlg.lineEdit_lastname.setReadOnly(True)
    dlg.lineEdit_firstname.setReadOnly(True)
    dlg.lineEdit_gender.setReadOnly(True)
    dlg.lineEdit_birthday.setReadOnly(True)
    dlg.lineEdit_email.setReadOnly(True)
    dlg.lineEdit_phone.setReadOnly(True)
    dlg.lineEdit_id.setReadOnly(True)
    dlg.lineEdit_certi.setReadOnly(True)
    dlg.lineEdit_cid.setReadOnly(True)

def init_page_wallet():
    refresh()
    print("balance:")
    print(accountBalance(customer_id))


def setPage(page):
    dlg.stackedWidget.setCurrentIndex(page)
    if page == 0:
        dlg.pushButton_profile.setProperty("class", "one")
        # dlg.pushButton_profile.setStyleSheet("background-color: rgb(212, 212, 212);")
        init_page_profile()
    elif page == 1:
        print("hi")
    elif page == 2:
        print("hrere")
        init_page_wallet()

def edit_profile():
    global edit
    if edit == False:
        dlg.lineEdit_lastname.setReadOnly(False)
        dlg.lineEdit_firstname.setReadOnly(False)
        dlg.lineEdit_gender.setReadOnly(False)
        dlg.lineEdit_birthday.setReadOnly(False)
        dlg.lineEdit_email.setReadOnly(False)
        dlg.lineEdit_phone.setReadOnly(False)
        # dlg.lineEdit_id.setReadOnly(False)
        # dlg.lineEdit_certi.setReadOnly(False)
        # dlg.lineEdit_cid.setReadOnly(False)
        dlg.pushButton_edit_profile.setText("Update")
        edit = True
    else:
        lastname = dlg.lineEdit_lastname.text()
        firstname = dlg.lineEdit_firstname.text()
        gender = dlg.lineEdit_gender.text()
        birthday = dlg.lineEdit_birthday.text().split('-')
        birthday2 = dlg.lineEdit_birthday.text()
        # for d in birthday:
        dateobj = datetime.date(int(birthday[0]),int(birthday[1]),int(birthday[2]))
        print()
        email = dlg.lineEdit_email.text()
        phone = dlg.lineEdit_phone.text()
        # if (lastname != "")
        user = (lastname, firstname, gender, birthday2, email, phone)
        cursor = my_cursor()
        cursor.edit("UPDATE Customer SET lastname=%s, firstname=%s, gender=%s, birthday=%s , email=%s, phone=%s WHERE customer_id="+customer_id, user)

        #update database
        dlg.pushButton_edit_profile.setText("Edit")
        edit = False
def clearData():
    dlg.tableWidget_accounts.clearSelection()
    while(dlg.tableWidget_accounts.rowCount() > 0):
        dlg.tableWidget_accounts.removeRow(0)
        dlg.tableWidget_accounts.clearSelection()

def createA():
    accountid = dlg.lineEdit_accountid.text()
    param = dlg.lineEdit_param.text()
    ctype = dlg.comboBox_ctype.currentText()
    atype = dlg.comboBox_atype.currentText()
    print(ctype)
    createAccount(accountid, customer_id, ctype, atype, param)
    
def refresh():
    clearData()
    loadAccounts()

# print(cursor.do("SELECT * FROM Customer"))


#side menu
# dlg.comboBox_ctype.setPlaceholderText("Account Type")
# dlg.lineEdit_accountid.setPlaceholderText("Account ID")
dlg.pushButton_profile.clicked.connect(lambda:setPage(0))
dlg.pushButton_home.clicked.connect(lambda:setPage(1))
dlg.pushButton_wallet.clicked.connect(lambda:setPage(2))
poptype="logout"
dlg.pushButton_logout.clicked.connect(lambda:show_popup("Message","Are you sure to log out?"))

# dlg.pushButton_profile.clicked.connect(setPage())
#profile page
dlg.pushButton_edit_profile.clicked.connect(edit_profile)

#wallet page
dlg.lineEdit_accountid.setPlaceholderText("Account ID")
dlg.pushButton_create.clicked.connect(createA)

#init
cursor = my_cursor()
customer_id = '002'
print(loadInfo(customer_id))
if isBirthday(customer_id):
    show_message("","Happy birthday! "+ ("Mr. " if checkGender(customer_id) == "male" else "Ms. ") + getSurname(customer_id))
greeting()
setPage(1)
# print(accountBalance(customer_id))

dlg.show()
app.exec()
