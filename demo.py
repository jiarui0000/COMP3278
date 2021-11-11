import mysql.connector
from Utils import *
from datetime import datetime

def createCustomer(customer_id,lastname,firstname,gender,birthday,email,phone,certification_type,id_number,password):
    variables=locals()
    sql_command = "INSERT INTO Customer VALUES ('"
    for i in variables.keys():
        sql_command=sql_command+str(variables[i])+"','"
    sql_command=sql_command[:-2]
    sql_command=sql_command+");"
    cursor.do(sql_command)

def createAccount(account_id, customer_id, currency_type, account_type, create_time, account_params):
    # check if exist
    response = cursor.do("SELECT account_id FROM Account;")
    exist_account = []
    for i in response:
        exist_account.append(i[0])
    if account_id in exist_account:
        return False

    # insert new
    variables=locals()
    create_time = create_time = datetime.today().strftime("%Y-%m-%d")
    sql_command = "INSERT INTO Account (account_id, customer_id, create_time, currency_type) VALUES ('"+account_id+"','"\
                  +customer_id+"','"+create_time+"','"+currency_type+"');"
    cursor.do(sql_command)
    account_type = account_type.capitalize()
    sql_command = "INSERT INTO "+account_type+"_account VALUES ('"
    sql_command += account_id+"','"+customer_id+"','"+currency_type+"','"+create_time+"','"+account_params+"');"
    try:
        cursor.do(sql_command)
        return True
    except:
        return False

def passwdLogin(customer_id, password):
    sql_command = "SELECT password FROM Customer WHERE customer_id='"+customer_id+"';"
    response = cursor.do(sql_command)
    if response[0][0] == password:
        return True
    else:
        return False

def passwdRetrieve(email_account):
    cursor = my_cursor()

def loadInfo(customer_id):
    sql_command = "SELECT * FROM Customer WHERE customer_id = '"+ customer_id + "'"
    print(sql_command)
    return cursor.do(sql_command)

def updateInfo(customer_id, update_type, update_value):
    sql_command = "UPDATE Customer SET "+update_type+" = '"+update_value+"' WHERE customer_id='"+customer_id+"';"
    try:
        cursor.do(sql_command)
        return True
    except:
        return False

def checkGender(customer_id):
    sql_command = "SELECT gender FROM Customer WHERE customer_id='"+customer_id+"';"
    response = cursor.do(sql_command)
    return response[0][0]

def getSurname(customer_id):
    sql_command = "SELECT lastname FROM Customer WHERE customer_id='"+customer_id+"';"
    response = cursor.do(sql_command)
    return response[0][0]

cursor = my_cursor()
# createCustomer('009','Ma','Jack','male','2020-11-01','@gmail.com','12345678','student card',11111,'iamjack')
print(createAccount('018', '007', 'Pound', 'saving', '2021-11-11', '62000'))
# print(passwdLogin('001', 'iamjack'))
# print(updateInfo('002', 'name', 'rosy'))
# print(checkGender('002'))
print(cursor.do("SELECT * FROM Account;"))
print(cursor.do("SELECT * FROM Saving_account;"))

