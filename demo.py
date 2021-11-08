import mysql.connector
from Utils import *
from datetime import datetime

def createCustomer():
    cursor = my_cursor()
    cursor.do()

def createAccount(account_id, customer_id, currenct_type):
    cursor = my_cursor()
    create_time = create_time = datetime.today().strftime("%Y-%m-%d")
    sql_command = "INSERT INTO Account (account_id, customer_id, create_time, currenct_type) VALUES ('"+account_id+"','"\
                  +customer_id+"','"+create_time+"','"+currenct_type+"');"
    cursor.do(sql_command)

def passwdLogin(customer_id, password):
    cursor = my_cursor()
    sql_command = "SELECT password FROM Customer WHERE customer_id='"+customer_id+"';"
    response = cursor.do(sql_command)
    if response[0][0] == password:
        return True
    else:
        return False

def passwdRetrieve(email_account):
    cursor = my_cursor()

def updateInfo(customer_id, update_type, update_value):
    cursor = my_cursor()
    sql_command = "UPDATE Customer SET "+update_type+" = '"+update_value+"' WHERE customer_id='"+customer_id+"';"
    try:
        cursor.do(sql_command)
        return True
    except:
        return False

# createAccount('015', '007', 'Pound')
# print(passwdLogin('001', 'iamjack'))
print(updateInfo('002', 'name', 'rose'))
