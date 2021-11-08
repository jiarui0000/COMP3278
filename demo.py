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

# createAccount('015', '007', 'Pound')
print(passwdLogin('001', 'iamjack'))
print(passwdLogin('002', 'iamjack'))