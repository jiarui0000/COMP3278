from Utils import *
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
currency_constant={'US Dollar':1, 'Hong Kong Dollar':7.8, 'Pound':0.75, 'China Yuan':6.4}

def newCustomerID():
    sql_command = "SELECT MAX(customer_id) FROM Customer;"
    return str(int(cursor.do(sql_command)[0][0]) + 1).zfill(3)


def createCustomer(customer_id, lastname, firstname, gender, birthday, email, phone, certification_type, id_number,
                   password):
    variables = locals()
    sql_command = "INSERT INTO Customer VALUES ('"
    for i in variables.keys():
        sql_command = sql_command + str(variables[i]) + "','"
    sql_command = sql_command[:-2]
    sql_command = sql_command + ");"
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
    variables = locals()
    create_time = create_time = datetime.today().strftime("%Y-%m-%d")
    sql_command = "INSERT INTO Account (account_id, customer_id, create_time, currency_type) VALUES ('" + account_id + "','" \
                  + customer_id + "','" + create_time + "','" + currency_type + "');"
    cursor.do(sql_command)
    account_type = account_type.capitalize()
    sql_command = "INSERT INTO " + account_type + "_account VALUES ('"
    sql_command += account_id + "','" + customer_id + "','" + currency_type + "','" + create_time + "','" + account_params + "');"
    try:
        cursor.do(sql_command)
        return True
    except:
        return False


def passwdLogin(customer_id, password):
    sql_command = "SELECT password FROM Customer WHERE customer_id='" + customer_id + "';"
    response = cursor.do(sql_command)
    if response[0][0] == password:
        return True
    else:
        return False


def updatePassword(customer_id, old_passwd, new_passwd):
    sql_command = "SELECT password FROM Customer WHERE customer_id='" + customer_id + "';"
    response = cursor.do(sql_command)
    if response[0][0] == old_passwd:
        sql_command = "UPDATE Customer SET password='" + new_passwd + "' WHERE customer_id='" + customer_id + "';"
        try:
            cursor.do(sql_command)
            return True
        except:
            return False
    else:
        return False


def passwdRetrieve(customer_id):  # set new password and send by email
    sender = 'jiaruiz@connect.hku.hk'
    sender_pass = ''  # 在这里写你的邮箱密码和邮箱
    receiver = cursor.do("SELECT email FROM Customer WHERE customer_id = '" + customer_id + "';")[0][0]
    customer_name = cursor.do("SELECT firstname FROM Customer WHERE customer_id = '" + customer_id + "';")[0][0]
    title = '[COMP3278G12] Password Retrieve'
    # secret key generate
    secret_key = ""
    for _ in range(8):
        secret_key += chr(random.randint(97, 122))

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = title  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText('Dear ' + customer_name + ',\n\n' + \
                            'You are retrieving your password. \nYour new password is: ' + secret_key + '\n\nNow you can use it to log in. \n\nDevelop Team G12\n', \
                            'plain', 'utf-8'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent with title ' + title)

    new_passwd = secret_key
    sql_command = "UPDATE Customer SET password='" + new_passwd + "' WHERE customer_id='" + customer_id + "';"
    cursor.do(sql_command)


def loadInfo(customer_id):
    sql_command = "SELECT * FROM Customer WHERE customer_id = '" + customer_id + "'"
    print(sql_command)
    return cursor.do(sql_command)


def isBirthday(customer_id):
    date = datetime.today().strftime("%m-%d")
    sql_command = "SELECT birthday FROM Customer WHERE customer_id = '" + customer_id + "';"
    birthday = cursor.do(sql_command)[0][0]
    return date == birthday.strftime("%m-%d")


def updateInfo(customer_id, update_type, update_value):
    sql_command = "UPDATE Customer SET " + update_type + " = '" + update_value + "' WHERE customer_id='" + customer_id + "';"
    try:
        cursor.do(sql_command)
        return True
    except:
        return False


def checkGender(customer_id):
    sql_command = "SELECT gender FROM Customer WHERE customer_id='" + customer_id + "';"
    response = cursor.do(sql_command)
    return response[0][0]


def getSurname(customer_id):
    sql_command = "SELECT lastname FROM Customer WHERE customer_id='" + customer_id + "';"
    response = cursor.do(sql_command)
    return response[0][0]


def accountList(customer_id):
    accounts = []
    for category in ['Investment', 'Saving', 'Credit']:
        sql_command = "SELECT * FROM "+category+"_account WHERE customer_id='" + customer_id + "';"
        response = cursor.do(sql_command)
        for ia in response:  # ia: account_id, customer_id, currency_type, create_time, total_value
            accounts.append((ia[0], category, ia[2], ia[3], ia[4]))
    return accounts


def accountBalance(account_id):
    for category in ['Investment', 'Saving', 'Credit']:
        sql_command = "SELECT * FROM "+category+"_account WHERE account_id='" + account_id + "';"
        response = cursor.do(sql_command)
        if len(response)!=0:
            rp=response[0]
            return [rp[0], rp[4], rp[2]]
    return []


def recentContect(customer_id):
    sql_command=""


def getType(account_id):
    for category in ['Investment', 'Saving', 'Credit']:
        sql_command = "SELECT * FROM " + category + "_account WHERE account_id='" + account_id + "';"
        response = cursor.do(sql_command)
        if len(response) != 0:
            return category
    return ''


def makeTransaction(in_account_id, out_account_id, in_customer_id, out_customer_id, amount, currency_type):
    # currency conversion
    sql_command="SELECT currency_type FROM Account WHERE account_id='"+in_account_id+"';"
    in_currency_constant = currency_constant[cursor.do(sql_command)[0][0]]
    sql_command = "SELECT currency_type FROM Account WHERE account_id='" + out_account_id + "';"
    out_currency_constant = currency_constant[cursor.do(sql_command)[0][0]]
    in_amount = int(round(amount / currency_constant[currency_type] * in_currency_constant))
    out_amount = int(round(amount / currency_constant[currency_type] * out_currency_constant))

    # verify
    valid = True
    sql_command = "SELECT currency_type FROM Account WHERE account_id='" + out_account_id + "';"
    valid = valid and (currency_type==cursor.do(sql_command)[0][0])
    sql_command = "SELECT customer_id FROM Account WHERE account_id='" + in_account_id + "';"
    valid = valid and (in_customer_id == cursor.do(sql_command)[0][0])
    sql_command = "SELECT customer_id FROM Account WHERE account_id='" + out_account_id + "';"
    valid = valid and (out_customer_id == cursor.do(sql_command)[0][0])
    in_type=getType(in_account_id)
    out_type=getType(out_account_id)
    valid = valid and (in_type != 'Investment') and (out_type != 'Investment')
    if out_type=='Saving':
        sql_command= "SELECT balance FROM Saving_account WHERE account_id='"+out_account_id+"';"
        valid = valid and (out_amount <= cursor.do(sql_command)[0][0])
    if not valid:
        return '', False

    # make transaction
    if in_type=='Saving':
        sql_command = "SELECT balance FROM Saving_account WHERE account_id='" + in_account_id + "';"
        balance = cursor.do(sql_command)[0][0]
        balance += in_amount
        sql_command = "UPDATE Saving_account SET balance="+str(balance)+" WHERE account_id='"+in_account_id+"';"
        cursor.do(sql_command)
    else: # credit account
        sql_command = "SELECT total_debt FROM Credit_account WHERE account_id='" + in_account_id + "';"
        debt = cursor.do(sql_command)[0][0]
        debt -= in_amount
        sql_command = "UPDATE Credit_account SET total_debt=" + str(debt) + " WHERE account_id='" + in_account_id + "';"
        cursor.do(sql_command)
    if out_type=='Saving':
        sql_command = "SELECT balance FROM Saving_account WHERE account_id='" + out_account_id + "';"
        balance = cursor.do(sql_command)[0][0]
        balance -= out_amount
        sql_command = "UPDATE Saving_account SET balance=" + str(balance) + " WHERE account_id='" + out_account_id + "';"
        cursor.do(sql_command)
    else: # credit account
        sql_command = "SELECT total_debt FROM Credit_account WHERE account_id='" + out_account_id + "';"
        debt = cursor.do(sql_command)[0][0]
        debt += in_amount
        sql_command = "UPDATE Credit_account SET total_debt=" + str(debt) + " WHERE account_id='" + out_account_id + "';"
        cursor.do(sql_command)
    sql_command="SELECT MAX(transaction_id) FROM Transaction;"
    trandactionID=str(int(cursor.do(sql_command)[0][0]) + 1).zfill(3)
    timepoint_date=datetime.today().strftime("%Y-%m-%d")
    timepoint_time=datetime.now().strftime("%H:%M:%S")
    sql_command="INSERT INTO Transaction VALUES ('"+trandactionID+"','"+str(in_account_id)+"','"+str(out_account_id)+ \
                "','"+str(in_customer_id)+"','"+str(out_customer_id)+"',"+str(amount)+",'"+str(currency_type)+ \
                "','"+str(timepoint_date)+"','"+str(timepoint_time)+"');"
    print(sql_command)
    cursor.do(sql_command)
    return trandactionID


cursor = my_cursor()
# print(makeTransaction('004','001','002','001',370,'Pound'))
