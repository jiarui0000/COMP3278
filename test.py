from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from demo import *
from Utils import *
import datetime
import sys
from PyQt5.QtGui import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("p_main.ui")
###
#default value
accountType = ""
edit = False
trans = False
poptype = "logout"

style_side = '''QPushButton{
	color: rgb(0, 0, 0);
	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(198, 213, 234, 255), stop:1 rgba(238, 242, 250, 255));
	border: 0px solid;
}
QPushButton:hover{
	background-color: rgb(238, 242, 250);
	border: 0px solid;
}
QPushButton#btn1{
	background-color: rgb(238, 242, 250);
	border: 0px solid;
}

'''

style_profile = '''QLineEdit{
border:0px solid gray;
border-radius:3px;

}
QLineEdit#edit1{
border:2px solid grey;
border-radius:3px;

}'''

style_profile2 = '''QPushButton{border:0px solid;
border-radius:5px;
background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(198, 213, 234, 255), stop:1 rgba(238, 242, 250, 255))
}
QPushButton#edit2{border:0px solid;
border-radius:5px;
background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(92, 184, 136, 255), stop:1 rgba(238, 242, 250, 255))
}'''
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

def loadContects():
    list=recentContect(customer_id)
    # list2 = 
    for row_count, Contect in enumerate(list):
        dlg.tableWidget_recentContect.insertRow(row_count)#row
        id = Contect[1]
        name = getSurname(id) +", "+ getFirstname(id)
        cell = QtWidgets.QTableWidgetItem(name)
        dlg.tableWidget_recentContect.setItem(row_count, 0, cell)
        cell = QtWidgets.QTableWidgetItem(str(id))
        dlg.tableWidget_recentContect.setItem(row_count, 1, cell)
        cell = QtWidgets.QTableWidgetItem(str(Contect[0]))
        dlg.tableWidget_recentContect.setItem(row_count, 2, cell)
    # for column_number, data in enumerate(Contect):
    #     cell = QtWidgets.QTableWidgetItem(str(data))#one cell
    #     dlg.tableWidget_recentContect.setItem(row_count, column_number, cell)
    

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

def loadLogin():
    list=loginHistory(customer_id)
    print(list)
    dlg.label_loginname.setText(getSurname(customer_id) + ", "+ getFirstname(customer_id))
    dlg.label_loginid.setText(customer_id)
    dlg.label_logintime.setText(str(list[0][0]).split(' ')[1])
    for row_count, history in enumerate(list):
        dlg.tableWidget_login.insertRow(row_count)
        history2 = str(history[0]).split(' ')
        cell = QtWidgets.QTableWidgetItem(str(history2[0]))
        dlg.tableWidget_login.setItem(row_count, 0, cell)
        cell = QtWidgets.QTableWidgetItem(str(history2[1]))
        dlg.tableWidget_login.setItem(row_count, 1, cell)

def clearData4():
    # print("clear")
    dlg.tableWidget_login.clearSelection()
    while(dlg.tableWidget_login.rowCount() > 0):
        dlg.tableWidget_login.removeRow(0)
        dlg.tableWidget_login.clearSelection()

def init_page_home():
    # print("init!")
    loadImage()
    dlg.pushButton_qt.setVisible(False)
    dlg.frame_maketransaction_2.setVisible(False)
    clearData3()
    loadContects()
    clearData4()
    loadLogin()

def init_page_profile():
    dlg.frame_pwd.setVisible(False)
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
    clearData2()
    dlg.label_viewinfo.setVisible(True)
    dlg.frame_maketransaction.setVisible(False)
    dlg.pushButton_make.setVisible(False)
    global accountType
    accountType = ""
    # print("balance:")
    # print(accountBalance(customer_id))

def setPage(page):
    dlg.stackedWidget.setCurrentIndex(page)
    dlg.pushButton_profile.setObjectName('btn')
    dlg.pushButton_home.setObjectName('btn')
    dlg.pushButton_wallet.setObjectName('btn')
    dlg.pushButton_transfer.setObjectName('btn')
    if page == 0:
        init_page_profile()
        dlg.pushButton_profile.setObjectName('btn1')
    elif page == 1:
        init_page_home()
        dlg.pushButton_home.setObjectName('btn1')
    elif page == 2:
        init_page_wallet()
        dlg.pushButton_wallet.setObjectName('btn1')
    elif page==3:
        init_page_transfer()
        dlg.pushButton_transfer.setObjectName('btn1')
    dlg.pushButton_qt.setVisible(False)
    dlg.pushButton_profile.setStyleSheet(style_side)
    dlg.pushButton_home.setStyleSheet(style_side)
    dlg.pushButton_wallet.setStyleSheet(style_side)
    dlg.pushButton_transfer.setStyleSheet(style_side)


def changepwd():
    dlg.frame_pwd.setVisible(True)


def init_page_transfer():
    dlg.stackedWidget_2.setCurrentIndex(0)
    dlg.radioButton.setChecked(False)
    dlg.radioButton_2.setChecked(False)
    clearData5()
    # print("yes")

def confirmchangepwd():
    old = dlg.lineEdit_p1.text()
    new1 = dlg.lineEdit_p2.text()
    new2 = dlg.lineEdit_p3.text()
    if (new1 != new2):
        show_message(title= "Message", message="The confirm password is not the same as new password!")
    else:
        if (updatePassword(customer_id, old, new1) == False):
            show_message(title= "Message", message="The old password is incorrect!")
        else:
            show_message(title= "Message", message="Updated password successfully!")
            
def loadImage():
    dlg.label_image.setPixmap(QPixmap("balance trend\example.png"))

def cancelchangepwd():
    dlg.lineEdit_p1.setText("")
    dlg.lineEdit_p2.setText("")
    dlg.lineEdit_p3.setText("")
    dlg.frame_pwd.setVisible(False)

def edit_profile():
    global edit
    if edit == False:
        dlg.lineEdit_lastname.setReadOnly(False)
        dlg.lineEdit_firstname.setReadOnly(False)
        dlg.lineEdit_gender.setReadOnly(False)
        dlg.lineEdit_birthday.setReadOnly(False)
        dlg.lineEdit_email.setReadOnly(False)
        dlg.lineEdit_phone.setReadOnly(False)

        dlg.lineEdit_lastname.setObjectName('edit1')
        dlg.lineEdit_firstname.setObjectName('edit1')
        dlg.lineEdit_gender.setObjectName('edit1')
        dlg.lineEdit_birthday.setObjectName('edit1')
        dlg.lineEdit_email.setObjectName('edit1')
        dlg.lineEdit_phone.setObjectName('edit1')
        # dlg.lineEdit_id.setReadOnly(False)
        # dlg.lineEdit_certi.setReadOnly(False)
        # dlg.lineEdit_cid.setReadOnly(False)
        dlg.pushButton_edit_profile.setText("Update Profile")
        dlg.pushButton_edit_profile.setObjectName('edit2')
        edit = True
    else:
        lastname = dlg.lineEdit_lastname.text()
        firstname = dlg.lineEdit_firstname.text()
        gender = dlg.lineEdit_gender.text()
        # birthday = dlg.lineEdit_birthday.text().split('-')
        birthday2 = dlg.lineEdit_birthday.text()
        # for d in birthday:
        # dateobj = datetime.date(int(birthday[0]),int(birthday[1]),int(birthday[2]))
        print()
        email = dlg.lineEdit_email.text()
        phone = dlg.lineEdit_phone.text()
        # if (lastname != "")
        if lastname.strip(" ") != "" and firstname.strip(" ") != "" and gender.strip(" ") != "" and birthday2.strip(" ") != "" and email.strip(" ") != "" and phone.strip(" ") != "":
            user = (lastname, firstname, gender, birthday2, email, phone)
            cursor = my_cursor()
            cursor.edit("UPDATE Customer SET lastname=%s, firstname=%s, gender=%s, birthday=%s , email=%s, phone=%s WHERE customer_id="+customer_id, user)
            dlg.lineEdit_lastname.setReadOnly(True)
            dlg.lineEdit_firstname.setReadOnly(True)
            dlg.lineEdit_gender.setReadOnly(True)
            dlg.lineEdit_birthday.setReadOnly(True)
            dlg.lineEdit_email.setReadOnly(True)
            dlg.lineEdit_phone.setReadOnly(True)
            #update database
            dlg.pushButton_edit_profile.setText("Edit Profile")
            edit = False
            dlg.lineEdit_lastname.setObjectName('edit0')
            dlg.lineEdit_firstname.setObjectName('edit0')
            dlg.lineEdit_gender.setObjectName('edit0')
            dlg.lineEdit_birthday.setObjectName('edit0')
            dlg.lineEdit_email.setObjectName('edit0')
            dlg.lineEdit_phone.setObjectName('edit0')
            dlg.pushButton_edit_profile.setObjectName('edit0')
        else:
            show_message("Error", "Please fill in all the blanks!")
    dlg.lineEdit_lastname.setStyleSheet(style_profile)
    dlg.lineEdit_firstname.setStyleSheet(style_profile)
    dlg.lineEdit_gender.setStyleSheet(style_profile)
    dlg.lineEdit_birthday.setStyleSheet(style_profile)
    dlg.lineEdit_email.setStyleSheet(style_profile)
    dlg.lineEdit_phone.setStyleSheet(style_profile)
    dlg.pushButton_edit_profile.setStyleSheet(style_profile2)

#accounts page
def clearData():
    dlg.tableWidget_accounts.clearSelection()
    while(dlg.tableWidget_accounts.rowCount() > 0):
        dlg.tableWidget_accounts.removeRow(0)
        dlg.tableWidget_accounts.clearSelection()

def clearData3():
    dlg.tableWidget_recentContect.clearSelection()
    while(dlg.tableWidget_recentContect.rowCount() > 0):
        dlg.tableWidget_recentContect.removeRow(0)
        dlg.tableWidget_recentContect.clearSelection()

# def createA():
#     accountid = dlg.lineEdit_accountid.text()
#     param = dlg.lineEdit_param.text()
#     ctype = dlg.comboBox_ctype.currentText()
#     atype = dlg.comboBox_atype.currentText()
#     print(ctype)
#     createAccount(accountid, customer_id, ctype, atype, param)
    
def refresh():
    clearData()
    loadAccounts()
    # print(dlg.tableWidget_accounts.item(dlg.tableWidget_accounts.currentRow(), 0).text())

# def refresh2():
#     clearData()
#     loadAccounts()

def getSelectedRowId():
    return dlg.tableWidget_accounts.currentRow()
def getSelectedAccountId():
    # print(dlg.tableWidget_accounts.item(1,1))
    return dlg.tableWidget_accounts.item(dlg.tableWidget_accounts.currentRow(), 0).text()
def getSelectedAccountType():
    return dlg.tableWidget_accounts.item(dlg.tableWidget_accounts.currentRow(), 1).text()

def getSelectedRowId2():
    return dlg.tableWidget_recentContect.currentRow()
def getSelectedAccountId2():
    # print(dlg.tableWidget_accounts.item(1,1))
    return dlg.tableWidget_recentContect.item(dlg.tableWidget_recentContect.currentRow(), 2).text()
def getSelectedCustomerId():
    return dlg.tableWidget_recentContect.item(dlg.tableWidget_recentContect.currentRow(), 1).text()

def loadHistory(account_id):
    list=transactionHistory2(account_id)
    # print(accountList(customer_id))
    # users = helper.select("SELECT * FROM users")
    # print(users)
    for row_count, t in enumerate(list):
        dlg.tableWidget_transactions.insertRow(row_count)#row
        for column_number, data in enumerate(t):
            cell = QtWidgets.QTableWidgetItem(str(data))#one cell
            dlg.tableWidget_transactions.setItem(row_count, column_number, cell)

def clearData2():
    dlg.tableWidget_transactions.clearSelection()
    while(dlg.tableWidget_transactions.rowCount() > 0):
        dlg.tableWidget_transactions.removeRow(0)
        dlg.tableWidget_transactions.clearSelection()

def clearData5():
    dlg.tableWidget_transactions_2.clearSelection()
    while(dlg.tableWidget_transactions_2.rowCount() > 0):
        dlg.tableWidget_transactions_2.removeRow(0)
        dlg.tableWidget_transactions_2.clearSelection()

def selectionChange2():
    # print(getSelectedUserId())
    # selected_row = getSelectedRowId()
    dlg.pushButton_qt.setVisible(True)
    # account_id = getSelectedAccountId()


 

def selectionChange():
    # print(getSelectedUserId())
    # selected_row = getSelectedRowId()
    dlg.label_viewinfo.setVisible(False)
    dlg.pushButton_make.setVisible(True)
    account_id = getSelectedAccountId()

    # name = dlg.tableWidget.item(selected_row, 1).text()
    # date = dlg.tableWidget.item(selected_row, 2).text()
    # admin = dlg.tableWidget.item(selected_row, 3).text()

    # dlg.lineEdit_4.setText(name)
    # dlg.lineEdit_5.setText(date)
    clearData2()
    loadHistory(account_id)

def makeTT():
    # selected_row = getSelectedRowId()
    toa = getSelectedAccountId2()
    toc = getSelectedCustomerId()
    # name = dlg.tableWidget.item(selected_row, 1).text()
    dlg.lineEdit_To_account_4.setText(toa)
    dlg.lineEdit_To_account_4.setReadOnly(True)
    dlg.lineEdit_To_customer_4.setText(toc)
    dlg.lineEdit_To_customer_4.setReadOnly(True)
    dlg.frame_maketransaction_2.setVisible(True)
# print(cursor.do("SELECT * FROM Customer"))
def makeTT2():#false的error提示
    froma = dlg.lineEdit_From_account_4.text()
    toa = dlg.lineEdit_To_account_4.text()
    toc = dlg.lineEdit_To_customer_4.text()
    amount = dlg.lineEdit_amount_4.text()
    ttype = dlg.comboBox_ttype_4.currentText()
    # makeTransaction(in_account_id, out_account_id, in_customer_id, out_customer_id, amount, currency_type)
    # print((toa, froma, toc, customer_id, int(amount), ttype))
    # print(makeTransaction(toa, froma, toc, customer_id, int(amount), ttype))
    # if accountType == "Investment":
    #     show_message("Error", "Sorry, you cannot use an investment account to make transactions.")
    if froma.strip(" ") != "" and toa.strip(" ") != "" and toc.strip(" ") != "" and amount.strip(" ") != "" and ttype.strip(" ") != "":
        print(str(toa)+ froma+ toc+ customer_id+ amount+ttype)
        if (makeTransaction(toa, froma, toc, customer_id, int(amount), ttype)[1]==False):
            show_message("Error","Transaction failed!")
        else: 
            show_message("Success","Transaction succeeded!")
            init_page_wallet()
    else:
        show_message("Error", "Please fill in all the blanks!")


def closeTT():
    dlg.lineEdit_From_account_4.setText("")
    dlg.lineEdit_To_account_4.setText("")
    dlg.lineEdit_To_customer_4.setText("")
    dlg.lineEdit_amount_4.setText("")
    dlg.frame_maketransaction_2.setVisible(False)
    # 所有text归零

def makeT():
    # selected_row = getSelectedRowId()
    account_id = getSelectedAccountId()
    global accountType
    accountType = getSelectedAccountType()
    # name = dlg.tableWidget.item(selected_row, 1).text()
    dlg.lineEdit_From_account.setText(account_id)
    dlg.lineEdit_From_account.setReadOnly(True)
    dlg.frame_maketransaction.setVisible(True)
# print(cursor.do("SELECT * FROM Customer"))
def makeT2():#false的error提示
    froma = dlg.lineEdit_From_account.text()
    toa = dlg.lineEdit_To_account.text()
    toc = dlg.lineEdit_To_customer.text()
    amount = dlg.lineEdit_amount.text()
    ttype = dlg.comboBox_ttype.currentText()
    # makeTransaction(in_account_id, out_account_id, in_customer_id, out_customer_id, amount, currency_type)
    # print((toa, froma, toc, customer_id, int(amount), ttype))
    # print(makeTransaction(toa, froma, toc, customer_id, int(amount), ttype))
    if accountType == "Investment":
        show_message("Error", "Sorry, you cannot use an investment account to make transactions.")
    elif froma.strip(" ") != "" and toa.strip(" ") != "" and toc.strip(" ") != "" and amount.strip(" ") != "" and ttype.strip(" ") != "":
        if (makeTransaction(toa, froma, toc, customer_id, int(amount), ttype)[1]==False):
            show_message("Error","Transaction failed!")
        else: 
            show_message("Success","Transaction succeeded!")
            init_page_wallet()
    else:
        show_message("Error", "Please fill in all the blanks!")


def closeT():
    dlg.lineEdit_From_account.setText("")
    dlg.lineEdit_To_account.setText("")
    dlg.lineEdit_To_customer.setText("")
    dlg.lineEdit_amount.setText("")
    dlg.frame_maketransaction.setVisible(False)

def loadT2(find_type, t):
    list=searchTransaction(customer_id, find_type, t)
    # print(accountList((customer_id))
    # users = helper.select("SELECT * FROM users")
    # print(users)
    for row_count, tt in enumerate(list):
        dlg.tableWidget_transactions_2.insertRow(row_count)#row
        for column_number, data in enumerate(tt):
            cell = QtWidgets.QTableWidgetItem(str(data))#one cell
            dlg.tableWidget_transactions_2.setItem(row_count, column_number, cell)
#page_transaction
def search1():
    fromt = dlg.lineEdit_fromt.text()
    tot =dlg.lineEdit_tot.text()
    t = (fromt,tot)
    find_type = 'time_period'
    if fromt.strip(" ") != "" and tot.strip(" ") != "" and len(tot)==10 and len(fromt)==10:
        clearData5()
        loadT2(find_type, t)
    else:
        show_message("Error","Please enter the information in the correct format!")
    # print(searchTransaction(find_type, t))
def search2():
    find_type = dlg.comboBox_stype.currentText()
    t = dlg.lineEdit_param2.text()
    if t.strip(" ") != "":
        clearData5()
        loadT2(find_type, t)
    else:
        show_message("Error","Please fill in all the blanks!")
def changeSearch(index):
    clearData5()
    dlg.stackedWidget_2.setCurrentIndex(index)



#side menu
# dlg.comboBox_ctype.setPlaceholderText("Account Type")
# dlg.lineEdit_accountid.setPlaceholderText("Account ID")
dlg.pushButton_profile.clicked.connect(lambda:setPage(0))
dlg.pushButton_home.clicked.connect(lambda:setPage(1))
dlg.pushButton_wallet.clicked.connect(lambda:setPage(2))
dlg.pushButton_transfer.clicked.connect(lambda:setPage(3))
poptype="logout"
dlg.pushButton_logout.clicked.connect(lambda:show_popup("Message","Are you sure to log out?"))

# dlg.pushButton_profile.clicked.connect(setPage())
#profile page
dlg.pushButton_edit_profile.clicked.connect(edit_profile)
dlg.pushButton_changepwd.clicked.connect(changepwd)
dlg.pushButton_cancelpwd.clicked.connect(cancelchangepwd)
dlg.pushButton_confirmpwd.clicked.connect(confirmchangepwd)
# dlg.pushButton_history.clicked.connect(getSelectedAccountId())

#home page
dlg.pushButton_qt.clicked.connect(makeTT)
dlg.pushButton_make2_4.clicked.connect(makeTT2)
dlg.pushButton_cancel_4.clicked.connect(closeTT)
dlg.tableWidget_recentContect.itemSelectionChanged.connect(selectionChange2)
#accounts page
# dlg.lineEdit_accountid.setPlaceholderText("Account ID")
# dlg.pushButton_create.clicked.connect(createA)
dlg.tableWidget_accounts.itemSelectionChanged.connect(selectionChange)
dlg.pushButton_make.clicked.connect(makeT)
dlg.pushButton_cancel.clicked.connect(closeT)
dlg.pushButton_make2.clicked.connect(makeT2)
#transaction page
dlg.radioButton_2.clicked.connect(lambda:changeSearch(1))
dlg.radioButton.clicked.connect(lambda:changeSearch(2))
dlg.pushButton_searchtime.clicked.connect(search1)
dlg.pushButton_searchtype.clicked.connect(search2)
#init
cursor = my_cursor()
customer_id = '002'
print(loadInfo(customer_id))
if isBirthday(customer_id):
    show_message("","Happy birthday! "+ ("Mr. " if checkGender(customer_id) == "male" else "Ms. ") + getSurname(customer_id))
greeting()
setPage(1)
print(recentContect(customer_id))
print(loginHistory(customer_id))
# print(accountBalance(customer_id))
# print(transactionHistory2(getSelectedAccountId()))
dlg.show()
app.exec()
