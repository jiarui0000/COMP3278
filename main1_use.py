# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main1 import Ui_Main


from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from demo import *
from Utils import *
import datetime
import sys
from PyQt5.QtGui import *

# app = QtWidgets.QApplication([])
# dlg = uic.loadUi("p_main.ui")
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
cursor = my_cursor()
customer_id = '002'
# GUI class
class MyMainForm(QMainWindow, Ui_Main):
    
    
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)


        # print(loadInfo(customer_id))
        # if isBirthday(customer_id):
        #     show_message("","Happy birthday! "+ ("Mr. " if checkGender(customer_id) == "male" else "Ms. ") + getSurname(customer_id))
        self.greeting()
        self.setPage(1)
        #side menu
        # self.comboBox_ctype.setPlaceholderText("Account Type")
        # self.lineEdit_accountid.setPlaceholderText("Account ID")
        self.pushButton_profile.clicked.connect(lambda:self.setPage(0))
        self.pushButton_home.clicked.connect(lambda:self.setPage(1))
        self.pushButton_wallet.clicked.connect(lambda:self.setPage(2))
        self.pushButton_transfer.clicked.connect(lambda:self.setPage(3))
        poptype="logout"
        self.pushButton_logout.clicked.connect(lambda:self.show_popup("Message","Are you sure to log out?"))

        # self.pushButton_profile.clicked.connect(setPage())
        #profile page
        self.pushButton_edit_profile.clicked.connect(self.edit_profile)
        self.pushButton_changepwd.clicked.connect(self.changepwd)
        self.pushButton_cancelpwd.clicked.connect(self.cancelchangepwd)
        self.pushButton_confirmpwd.clicked.connect(self.confirmchangepwd)
        # self.pushButton_history.clicked.connect(getSelectedAccountId())

        #home page
        self.pushButton_qt.clicked.connect(self.makeTT)
        self.pushButton_make2_4.clicked.connect(self.makeTT2)
        self.pushButton_cancel_4.clicked.connect(self.closeTT)
        self.tableWidget_recentContect.itemSelectionChanged.connect(self.selectionChange2)
        #accounts page
        # self.lineEdit_accountid.setPlaceholderText("Account ID")
        # self.pushButton_create.clicked.connect(createA)
        self.tableWidget_accounts.itemSelectionChanged.connect(self.selectionChange)
        self.pushButton_make.clicked.connect(self.makeT)
        self.pushButton_cancel.clicked.connect(self.closeT)
        self.pushButton_make2.clicked.connect(self.makeT2)
        #transaction page
        self.radioButton_2.clicked.connect(lambda:self.changeSearch(1))
        self.radioButton.clicked.connect(lambda:self.changeSearch(2))
        self.pushButton_searchtime.clicked.connect(self.search1)
        self.pushButton_searchtype.clicked.connect(self.search2)

    #     self.pushButton.clicked.connect(self.display)
    
    # def display(self):
    #     username = self.lineEdit.text()
    #     password = self.lineEdit_2.text()

    #     self.textBrowser.setText('Log in successfully!\n Username is %s\n Password is %s' % (username, password))
        #functions
    def show_message(self, title= "Message", message="text"):
        msg = QMessageBox()
        msg.information(None, title, message)

    def timecheck(self):
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

    def greeting(self):
        self.label_surname.setText(("Mr. " if checkGender(customer_id) == "male" else "Ms. ") + getSurname(customer_id))
        if self.timecheck() == 1:
            self.label.setText("Good morning,")
        elif self.timecheck() == 2:
            self.label.setText("Good afternoon,")
        else:
            self.label.setText("Good evening,")

    def show_popup(self, title= "Test", message="message"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self, i):
        global poptype
        if poptype == "logout":
            if i.text() == "&Yes":
                print("excute logout")
        elif poptype == "delete1":
            print("not")

    def loadContects(self):
        list=recentContect(customer_id)
        # list2 = 
        for row_count, Contect in enumerate(list):
            self.tableWidget_recentContect.insertRow(row_count)#row
            id = Contect[1]
            name = getSurname(id) +", "+ getFirstname(id)
            cell = QtWidgets.QTableWidgetItem(name)
            self.tableWidget_recentContect.setItem(row_count, 0, cell)
            cell = QtWidgets.QTableWidgetItem(str(id))
            self.tableWidget_recentContect.setItem(row_count, 1, cell)
            cell = QtWidgets.QTableWidgetItem(str(Contect[0]))
            self.tableWidget_recentContect.setItem(row_count, 2, cell)
        # for column_number, data in enumerate(Contect):
        #     cell = QtWidgets.QTableWidgetItem(str(data))#one cell
        #     self.tableWidget_recentContect.setItem(row_count, column_number, cell)
        

    def loadAccounts(self):
        list=accountList(customer_id)
        print(accountList(customer_id))
        # users = helper.select("SELECT * FROM users")
        # print(users)
        for row_count, account in enumerate(list):
            self.tableWidget_accounts.insertRow(row_count)#row
            for column_number, data in enumerate(account):
                cell = QtWidgets.QTableWidgetItem(str(data))#one cell
                self.tableWidget_accounts.setItem(row_count, column_number, cell)

    def loadLogin(self):
        list=loginHistory(customer_id)
        print(list)
        self.label_loginname.setText(getSurname(customer_id) + ", "+ getFirstname(customer_id))
        self.label_loginid.setText(customer_id)
        self.label_logintime.setText(str(list[0][0]).split(' ')[1])
        for row_count, history in enumerate(list):
            self.tableWidget_login.insertRow(row_count)
            history2 = str(history[0]).split(' ')
            cell = QtWidgets.QTableWidgetItem(str(history2[0]))
            self.tableWidget_login.setItem(row_count, 0, cell)
            cell = QtWidgets.QTableWidgetItem(str(history2[1]))
            self.tableWidget_login.setItem(row_count, 1, cell)

    def clearData4(self):
        # print("clear")
        self.tableWidget_login.clearSelection()
        while(self.tableWidget_login.rowCount() > 0):
            self.tableWidget_login.removeRow(0)
            self.tableWidget_login.clearSelection()

    def init_page_home(self):
        # print("init!")
        self.loadImage()
        self.pushButton_qt.setVisible(False)
        self.frame_maketransaction_2.setVisible(False)
        self.clearData3()
        self.loadContects()
        self.clearData4()
        self.loadLogin()

    def init_page_profile(self):
        self.frame_pwd.setVisible(False)
        result = loadInfo(customer_id)[0]
        self.lineEdit_lastname.setText(result[1])
        self.lineEdit_firstname.setText(result[2])
        self.lineEdit_gender.setText(result[3])
        self.lineEdit_birthday.setText(str(result[4]))
        self.lineEdit_email.setText(result[5])
        self.lineEdit_phone.setText(result[6])
        self.lineEdit_id.setText(result[0])
        self.lineEdit_certi.setText(result[7])
        self.lineEdit_cid.setText(str(result[8]))
        # for i in range(self.groupBox)
        self.lineEdit_lastname.setReadOnly(True)
        self.lineEdit_firstname.setReadOnly(True)
        self.lineEdit_gender.setReadOnly(True)
        self.lineEdit_birthday.setReadOnly(True)
        self.lineEdit_email.setReadOnly(True)
        self.lineEdit_phone.setReadOnly(True)
        self.lineEdit_id.setReadOnly(True)
        self.lineEdit_certi.setReadOnly(True)
        self.lineEdit_cid.setReadOnly(True)

    def init_page_wallet(self):
        self.refresh()
        self.clearData2()
        self.label_viewinfo.setVisible(True)
        self.frame_maketransaction.setVisible(False)
        self.pushButton_make.setVisible(False)
        global accountType
        accountType = ""
        # print("balance:")
        # print(accountBalance(customer_id))

    def setPage(self,page):
        self.stackedWidget.setCurrentIndex(page)
        self.pushButton_profile.setObjectName('btn')
        self.pushButton_home.setObjectName('btn')
        self.pushButton_wallet.setObjectName('btn')
        self.pushButton_transfer.setObjectName('btn')
        if page == 0:
            self.init_page_profile()
            self.pushButton_profile.setObjectName('btn1')
        elif page == 1:
            self.init_page_home()
            self.pushButton_home.setObjectName('btn1')
        elif page == 2:
            self.init_page_wallet()
            self.pushButton_wallet.setObjectName('btn1')
        elif page==3:
            self.init_page_transfer()
            self.pushButton_transfer.setObjectName('btn1')
        self.pushButton_qt.setVisible(False)
        self.pushButton_profile.setStyleSheet(style_side)
        self.pushButton_home.setStyleSheet(style_side)
        self.pushButton_wallet.setStyleSheet(style_side)
        self.pushButton_transfer.setStyleSheet(style_side)


    def changepwd(self):
        self.frame_pwd.setVisible(True)


    def init_page_transfer(self):
        self.stackedWidget_2.setCurrentIndex(0)
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.clearData5()
        # print("yes")

    def confirmchangepwd(self):
        old = self.lineEdit_p1.text()
        new1 = self.lineEdit_p2.text()
        new2 = self.lineEdit_p3.text()
        if (new1 != new2):
            self.show_message(title= "Message", message="The confirm password is not the same as new password!")
        else:
            if (updatePassword(customer_id, old, new1) == False):
                self.show_message(title= "Message", message="The old password is incorrect!")
            else:
                self.show_message(title= "Message", message="Updated password successfully!")
                
    def loadImage(self):
        self.label_image.setPixmap(QPixmap("balance trend\example.png"))

    def cancelchangepwd(self):
        self.lineEdit_p1.setText("")
        self.lineEdit_p2.setText("")
        self.lineEdit_p3.setText("")
        self.frame_pwd.setVisible(False)

    def edit_profile(self):
        global edit
        if edit == False:
            self.lineEdit_lastname.setReadOnly(False)
            self.lineEdit_firstname.setReadOnly(False)
            self.lineEdit_gender.setReadOnly(False)
            self.lineEdit_birthday.setReadOnly(False)
            self.lineEdit_email.setReadOnly(False)
            self.lineEdit_phone.setReadOnly(False)

            self.lineEdit_lastname.setObjectName('edit1')
            self.lineEdit_firstname.setObjectName('edit1')
            self.lineEdit_gender.setObjectName('edit1')
            self.lineEdit_birthday.setObjectName('edit1')
            self.lineEdit_email.setObjectName('edit1')
            self.lineEdit_phone.setObjectName('edit1')
            # self.lineEdit_id.setReadOnly(False)
            # self.lineEdit_certi.setReadOnly(False)
            # self.lineEdit_cid.setReadOnly(False)
            self.pushButton_edit_profile.setText("Update Profile")
            self.pushButton_edit_profile.setObjectName('edit2')
            edit = True
        else:
            lastname = self.lineEdit_lastname.text()
            firstname = self.lineEdit_firstname.text()
            gender = self.lineEdit_gender.text()
            # birthday = self.lineEdit_birthday.text().split('-')
            birthday2 = self.lineEdit_birthday.text()
            # for d in birthday:
            # dateobj = datetime.date(int(birthday[0]),int(birthday[1]),int(birthday[2]))
            print()
            email = self.lineEdit_email.text()
            phone = self.lineEdit_phone.text()
            # if (lastname != "")
            if lastname.strip(" ") != "" and firstname.strip(" ") != "" and gender.strip(" ") != "" and birthday2.strip(" ") != "" and email.strip(" ") != "" and phone.strip(" ") != "":
                user = (lastname, firstname, gender, birthday2, email, phone)
                cursor = my_cursor()
                cursor.edit("UPDATE Customer SET lastname=%s, firstname=%s, gender=%s, birthday=%s , email=%s, phone=%s WHERE customer_id="+customer_id, user)
                self.lineEdit_lastname.setReadOnly(True)
                self.lineEdit_firstname.setReadOnly(True)
                self.lineEdit_gender.setReadOnly(True)
                self.lineEdit_birthday.setReadOnly(True)
                self.lineEdit_email.setReadOnly(True)
                self.lineEdit_phone.setReadOnly(True)
                #update database
                self.pushButton_edit_profile.setText("Edit Profile")
                edit = False
                self.lineEdit_lastname.setObjectName('edit0')
                self.lineEdit_firstname.setObjectName('edit0')
                self.lineEdit_gender.setObjectName('edit0')
                self.lineEdit_birthday.setObjectName('edit0')
                self.lineEdit_email.setObjectName('edit0')
                self.lineEdit_phone.setObjectName('edit0')
                self.pushButton_edit_profile.setObjectName('edit0')
            else:
                self.show_message("Error", "Please fill in all the blanks!")
        self.lineEdit_lastname.setStyleSheet(style_profile)
        self.lineEdit_firstname.setStyleSheet(style_profile)
        self.lineEdit_gender.setStyleSheet(style_profile)
        self.lineEdit_birthday.setStyleSheet(style_profile)
        self.lineEdit_email.setStyleSheet(style_profile)
        self.lineEdit_phone.setStyleSheet(style_profile)
        self.pushButton_edit_profile.setStyleSheet(style_profile2)

    #accounts page
    def clearData(self):
        self.tableWidget_accounts.clearSelection()
        while(self.tableWidget_accounts.rowCount() > 0):
            self.tableWidget_accounts.removeRow(0)
            self.tableWidget_accounts.clearSelection()

    def clearData3(self):
        self.tableWidget_recentContect.clearSelection()
        while(self.tableWidget_recentContect.rowCount() > 0):
            self.tableWidget_recentContect.removeRow(0)
            self.tableWidget_recentContect.clearSelection()

    # def createA(self):
    #     accountid = self.lineEdit_accountid.text()
    #     param = self.lineEdit_param.text()
    #     ctype = self.comboBox_ctype.currentText()
    #     atype = self.comboBox_atype.currentText()
    #     print(ctype)
    #     createAccount(accountid, customer_id, ctype, atype, param)
        
    def refresh(self):
        self.clearData()
        self.loadAccounts()
        # print(self.tableWidget_accounts.item(self.tableWidget_accounts.currentRow(), 0).text())

    # def refresh2():
    #     clearData()
    #     loadAccounts()

    def getSelectedRowId(self):
        return self.tableWidget_accounts.currentRow()
    def getSelectedAccountId(self):
        # print(self.tableWidget_accounts.item(1,1))
        return self.tableWidget_accounts.item(self.tableWidget_accounts.currentRow(), 0).text()
    def getSelectedAccountType(self):
        return self.tableWidget_accounts.item(self.tableWidget_accounts.currentRow(), 1).text()

    def getSelectedRowId2(self):
        return self.tableWidget_recentContect.currentRow()
    def getSelectedAccountId2(self):
        # print(self.tableWidget_accounts.item(1,1))
        return self.tableWidget_recentContect.item(self.tableWidget_recentContect.currentRow(), 2).text()
    def getSelectedCustomerId(self):
        return self.tableWidget_recentContect.item(self.tableWidget_recentContect.currentRow(), 1).text()

    def loadHistory(self, account_id):
        list=transactionHistory2(account_id)
        # print(accountList(customer_id))
        # users = helper.select("SELECT * FROM users")
        # print(users)
        for row_count, t in enumerate(list):
            self.tableWidget_transactions.insertRow(row_count)#row
            for column_number, data in enumerate(t):
                cell = QtWidgets.QTableWidgetItem(str(data))#one cell
                self.tableWidget_transactions.setItem(row_count, column_number, cell)

    def clearData2(self):
        self.tableWidget_transactions.clearSelection()
        while(self.tableWidget_transactions.rowCount() > 0):
            self.tableWidget_transactions.removeRow(0)
            self.tableWidget_transactions.clearSelection()

    def clearData5(self):
        self.tableWidget_transactions_2.clearSelection()
        while(self.tableWidget_transactions_2.rowCount() > 0):
            self.tableWidget_transactions_2.removeRow(0)
            self.tableWidget_transactions_2.clearSelection()

    def selectionChange2(self):
        # print(getSelectedUserId())
        # selected_row = getSelectedRowId()
        self.pushButton_qt.setVisible(True)
        # account_id = getSelectedAccountId()


    

    def selectionChange(self):
        # print(getSelectedUserId())
        # selected_row = getSelectedRowId()
        self.label_viewinfo.setVisible(False)
        self.pushButton_make.setVisible(True)
        account_id = self.getSelectedAccountId()

        # name = self.tableWidget.item(selected_row, 1).text()
        # date = self.tableWidget.item(selected_row, 2).text()
        # admin = self.tableWidget.item(selected_row, 3).text()

        # self.lineEdit_4.setText(name)
        # self.lineEdit_5.setText(date)
        self.clearData2()
        self.loadHistory(account_id)

    def makeTT(self):
        # selected_row = getSelectedRowId()
        toa = self.getSelectedAccountId2()
        toc = self.getSelectedCustomerId()
        # name = self.tableWidget.item(selected_row, 1).text()
        self.lineEdit_To_account_4.setText(toa)
        self.lineEdit_To_account_4.setReadOnly(True)
        self.lineEdit_To_customer_4.setText(toc)
        self.lineEdit_To_customer_4.setReadOnly(True)
        self.frame_maketransaction_2.setVisible(True)
    # print(cursor.do("SELECT * FROM Customer"))
    def makeTT2(self):#false的error提示
        froma = self.lineEdit_From_account_4.text()
        toa = self.lineEdit_To_account_4.text()
        toc = self.lineEdit_To_customer_4.text()
        amount = self.lineEdit_amount_4.text()
        ttype = self.comboBox_ttype_4.currentText()
        # makeTransaction(in_account_id, out_account_id, in_customer_id, out_customer_id, amount, currency_type)
        # print((toa, froma, toc, customer_id, int(amount), ttype))
        # print(makeTransaction(toa, froma, toc, customer_id, int(amount), ttype))
        # if accountType == "Investment":
        #     show_message("Error", "Sorry, you cannot use an investment account to make transactions.")
        if froma.strip(" ") != "" and toa.strip(" ") != "" and toc.strip(" ") != "" and amount.strip(" ") != "" and ttype.strip(" ") != "":
            print(str(toa)+ froma+ toc+ customer_id+ amount+ttype)
            if (makeTransaction(toa, froma, toc, customer_id, int(amount), ttype)[1]==False):
                self.show_message("Error","Transaction failed!")
            else: 
                self.show_message("Success","Transaction succeeded!")
                self.init_page_wallet()
        else:
            self.show_message("Error", "Please fill in all the blanks!")


    def closeTT(self):
        self.lineEdit_From_account_4.setText("")
        self.lineEdit_To_account_4.setText("")
        self.lineEdit_To_customer_4.setText("")
        self.lineEdit_amount_4.setText("")
        self.frame_maketransaction_2.setVisible(False)
        # 所有text归零

    def makeT(self):
        # selected_row = getSelectedRowId()
        account_id = self.getSelectedAccountId()
        global accountType
        accountType = self.getSelectedAccountType()
        # name = self.tableWidget.item(selected_row, 1).text()
        self.lineEdit_From_account.setText(account_id)
        self.lineEdit_From_account.setReadOnly(True)
        self.frame_maketransaction.setVisible(True)
    # print(cursor.do("SELECT * FROM Customer"))
    def makeT2(self):#false的error提示
        froma = self.lineEdit_From_account.text()
        toa = self.lineEdit_To_account.text()
        toc = self.lineEdit_To_customer.text()
        amount = self.lineEdit_amount.text()
        ttype = self.comboBox_ttype.currentText()
        # makeTransaction(in_account_id, out_account_id, in_customer_id, out_customer_id, amount, currency_type)
        # print((toa, froma, toc, customer_id, int(amount), ttype))
        # print(makeTransaction(toa, froma, toc, customer_id, int(amount), ttype))
        if accountType == "Investment":
            self.show_message("Error", "Sorry, you cannot use an investment account to make transactions.")
        elif froma.strip(" ") != "" and toa.strip(" ") != "" and toc.strip(" ") != "" and amount.strip(" ") != "" and ttype.strip(" ") != "":
            if (makeTransaction(toa, froma, toc, customer_id, int(amount), ttype)[1]==False):
                self.show_message("Error","Transaction failed!")
            else: 
                self.show_message("Success","Transaction succeeded!")
                self.init_page_wallet()
        else:
            self.show_message("Error", "Please fill in all the blanks!")


    def closeT(self):
        self.lineEdit_From_account.setText("")
        self.lineEdit_To_account.setText("")
        self.lineEdit_To_customer.setText("")
        self.lineEdit_amount.setText("")
        self.frame_maketransaction.setVisible(False)

    def loadT2(self, find_type, t):
        list=searchTransaction(customer_id, find_type, t)
        # print(accountList((customer_id))
        # users = helper.select("SELECT * FROM users")
        # print(users)
        for row_count, tt in enumerate(list):
            self.tableWidget_transactions_2.insertRow(row_count)#row
            for column_number, data in enumerate(tt):
                cell = QtWidgets.QTableWidgetItem(str(data))#one cell
                self.tableWidget_transactions_2.setItem(row_count, column_number, cell)
    #page_transaction
    def search1(self):
        fromt = self.lineEdit_fromt.text()
        tot =self.lineEdit_tot.text()
        t = (fromt,tot)
        find_type = 'time_period'
        if fromt.strip(" ") != "" and tot.strip(" ") != "" and len(tot)==10 and len(fromt)==10:
            self.clearData5()
            self.loadT2(find_type, t)
        else:
            self.show_message("Error","Please enter the information in the correct format!")
        # print(searchTransaction(find_type, t))
    def search2(self):
        find_type = self.comboBox_stype.currentText()
        t = self.lineEdit_param2.text()
        if t.strip(" ") != "":
            self.clearData5()
            self.loadT2(find_type, t)
        else:
            self.show_message("Error","Please fill in all the blanks!")
    def changeSearch(self, index):
        self.clearData5()
        self.stackedWidget_2.setCurrentIndex(index)

# main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    
    # cursor = my_cursor()
    # customer_id = '002'
    # print(loadInfo(customer_id))
    # if isBirthday(customer_id):
    #     show_message("","Happy birthday! "+ ("Mr. " if checkGender(customer_id) == "male" else "Ms. ") + getSurname(customer_id))
    # greeting(self)
    # setPage(1)
    # print(recentContect(customer_id))
    # print(loginHistory(customer_id))


    myWin.show()
    sys.exit(app.exec_())