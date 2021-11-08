from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from demo import *
from Utils import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("p_main.ui")
###
#default value
edit = False


#functions
def init_page_profile():
    result = loadInfo(customer_id)[0]
    dlg.lineEdit_name.setText(result[1])
    dlg.lineEdit_gender.setText(result[2])
    dlg.lineEdit_birthday.setText(str(result[3]))
    dlg.lineEdit_id.setText(result[0])
    dlg.lineEdit_certi.setText(result[4])
    dlg.lineEdit_cid.setText(str(result[5]))
    # for i in range(dlg.groupBox)
    dlg.lineEdit_name.setReadOnly(True)
    dlg.lineEdit_gender.setReadOnly(True)
    dlg.lineEdit_birthday.setReadOnly(True)
    dlg.lineEdit_id.setReadOnly(True)
    dlg.lineEdit_certi.setReadOnly(True)
    dlg.lineEdit_cid.setReadOnly(True)
    


def setPage(page):
    dlg.stackedWidget.setCurrentIndex(page)
    if page == 0:
        init_page_profile()
    elif page == 1:
        print("hi")

def edit_profile():
    if edit == False:
        dlg.lineEdit_name.setReadOnly(False)
        dlg.lineEdit_gender.setReadOnly(False)
        dlg.lineEdit_birthday.setReadOnly(False)
        # dlg.lineEdit_id.setReadOnly(False)
        dlg.lineEdit_certi.setReadOnly(False)
        dlg.lineEdit_cid.setReadOnly(False)
        dlg.pushButton_edit_profile.setText("Update")
    else:
        name = dlg.lineEdit_name.text()
        #update database



#init

cursor = my_cursor()
customer_id = '007'
# print(cursor.do("SELECT * FROM Customer"))
print(loadInfo(customer_id))
dlg.lineEdit_4.setPlaceholderText("account id")
dlg.pushButton_profile.clicked.connect(lambda:setPage(0))
dlg.pushButton_home.clicked.connect(lambda:setPage(1))
dlg.pushButton_wallet.clicked.connect(lambda:setPage(2))
# dlg.pushButton_profile.clicked.connect(setPage())
dlg.pushButton_edit_profile.clicked.connect(edit_profile)



dlg.show()
app.exec()