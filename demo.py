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
    print(sql_command)
    cursor.do(sql_command)

createAccount('015', '007', 'Pound')