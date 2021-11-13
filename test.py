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
trans = False
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

def loadContects():
    list=recentContect(customer_id)
    # list2 = 
    for row_count, Contect in enumerate(list):
        dlg.tableWidget_recentContect.insertRow(row_count)#row
        id = Contect[1]
        name = getSurname(id) +", "+ getFirstname(id)
        cell = QtWidgets.QTableWidgetItem(name)
        dlg.tableWidget_recentContect.setItem(row_count, 0, cell)
        cell = QtWidgets.QTableWidgetItem(str(Contect[0]))
        dlg.tableWidget_recentContect.setItem(row_count, 1, cell)
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
    for row_count, history in enumerate(list):
        dlg.tableWidget_login.insertRow(row_count)
        print(row_count)
        print(str(history[0]))
        cell = QtWidgets.QTableWidgetItem(str(history[0]))
        dlg.tableWidget_login.setItem(row_count, 0, cell)

def clearData4():
    # print("clear")
    dlg.tableWidget_login.clearSelection()
    while(dlg.tableWidget_login.rowCount() > 0):
        dlg.tableWidget_login.removeRow(0)
        dlg.tableWidget_login.clearSelection()

def init_page_home():
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
    print("balance:")
    print(accountBalance(customer_id))

def setPage(page):
    dlg.stackedWidget.setCurrentIndex(page)
    if page == 0:
        # dlg.pushButton_profile.setProperty("class", "one")
        # dlg.pushButton_profile.setStyleSheet("background-color: rgb(212, 212, 212);")
        init_page_profile()
    elif page == 1:
        init_page_home()
        print("hi")
        dlg.pushButton_home.setObjectName('btn1')
        # dlg.pushButton_home.setProperty('level', '1')
        # self.btn1.setObjectName('btn1')
        # dlg.pushButton_home.setStyleSheet('QPushButton#btn1{color: yellow; font-size: 20px;}')
    elif page == 2:
        print("hrere")
        init_page_wallet()
    elif page==3:
        init_page_transfer()


def changepwd():
    dlg.frame_pwd.setVisible(True)

def init_page_transfer():
    dlg.stackedWidget_2.setCurrentIndex(0)
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


def cancelchangepwd():
    dlg.lineEdit_p1.setText = ""
    dlg.lineEdit_p2.setText = ""
    dlg.lineEdit_p3.setText = ""
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
    # print(dlg.tableWidget_accounts.item(dlg.tableWidget_accounts.currentRow(), 0).text())

# def refresh2():
#     clearData()
#     loadAccounts()

def getSelectedRowId():
    return dlg.tableWidget_accounts.currentRow()
def getSelectedAccountId():
    # print(dlg.tableWidget_accounts.item(1,1))
    return dlg.tableWidget_accounts.item(dlg.tableWidget_accounts.currentRow(), 0).text()

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

def makeT():
    # selected_row = getSelectedRowId()
    account_id = getSelectedAccountId()
    # name = dlg.tableWidget.item(selected_row, 1).text()
    dlg.lineEdit_From_account.setText(account_id)
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
    if (makeTransaction(toa, froma, toc, customer_id, int(amount), ttype)=='', False):
        show_message("Error","Transaction failed!")
    else: 
        show_message("Success","Transaction succeeded!")

def closeT():
    dlg.frame_maketransaction.setVisible(False)
    # 所有text归零

def loadT2(find_type, t):
    list=searchTransaction(customer_id, find_type, t)
    # print(accountList(customer_id))
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
    print(len(tot))
    clearData5()
    loadT2(find_type, t)
    # print(searchTransaction(find_type, t))
def search2():
    find_type = dlg.comboBox_stype.currentText()
    t = dlg.lineEdit_param2.text()
    clearData5()
    loadT2(find_type, t)




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
#accounts page
dlg.lineEdit_accountid.setPlaceholderText("Account ID")
dlg.pushButton_create.clicked.connect(createA)
dlg.tableWidget_accounts.itemSelectionChanged.connect(selectionChange)
dlg.pushButton_make.clicked.connect(makeT)
dlg.pushButton_cancel.clicked.connect(closeT)
dlg.pushButton_make2.clicked.connect(makeT2)
#transaction page
dlg.radioButton_2.clicked.connect(lambda:dlg.stackedWidget_2.setCurrentIndex(1))
dlg.radioButton.clicked.connect(lambda:dlg.stackedWidget_2.setCurrentIndex(2))
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
