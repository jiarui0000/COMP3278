import mysql.connector
from Utils import *
from datetime import datetime

def createCustomer(customer_id,name,gender,password,birthday,certification_type,id_number,email,telephone,address,accept_promo):
    variables=locals()
    cursor = my_cursor(passwd='20211030')
    sql_command = "INSERT INTO Customer VALUES ('"
    for i in variables.keys():
        sql_command=sql_command+str(variables[i])+"','"
    sql_command=sql_command[:-2]
    sql_command=sql_command+");"
    cursor.do(sql_command)

def createAccount(account_id, customer_id, currency_type):
    cursor = my_cursor()
    create_time = create_time = datetime.today().strftime("%Y-%m-%d")
    sql_command = "INSERT INTO Account (account_id, customer_id, create_time, currency_type) VALUES ('"+account_id+"','"\
                  +customer_id+"','"+create_time+"','"+currency_type+"');"
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

def loadInfo(customer_id):
    cursor = my_cursor()
    sql_command = "SELECT * FROM Customer WHERE customer_id = '"+ customer_id + "'"
    print(sql_command)
    return cursor.do(sql_command)

def updateInfo(customer_id, update_type, update_value):
    cursor = my_cursor()
    sql_command = "UPDATE Customer SET "+update_type+" = '"+update_value+"' WHERE customer_id='"+customer_id+"';"
    try:
        cursor.do(sql_command)
        return True
    except:
        return False

def checkGender(customer_id):
    cursor = my_cursor()
    sql_command = "SELECT gender FROM Customer WHERE customer_id='"+customer_id+"';"
    response = cursor.do(sql_command)
    return response[0][0]

# createAccount('015', '007', 'Pound')
# print(passwdLogin('001', 'iamjack'))
# print(updateInfo('002', 'name', 'rosy'))
# print(checkGender('002'))

