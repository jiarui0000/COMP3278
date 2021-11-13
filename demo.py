from Utils import *
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

currency_constant = {'US Dollar': 1, 'HKD': 7.8, 'Pound': 0.75, 'Yuan': 6.4}
display_currency = 'HKD'


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


def createAccount(account_id, customer_id, currency_type, account_type, account_params):
    # check if exist
    response = cursor.do("SELECT account_id FROM Account;")
    exist_account = []
    for i in response:
        exist_account.append(i[0])
    if account_id in exist_account:
        return False

    # insert new
    variables = locals()
    create_time = datetime.today().strftime("%Y-%m-%d")
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
    sender = 'comp3278g12@gmail.com'
    sender_pass = 'comp3278comp3278'
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
    print('Mail Sent to ' + receiver)

    new_passwd = secret_key
    sql_command = "UPDATE Customer SET password='" + new_passwd + "' WHERE customer_id='" + customer_id + "';"
    cursor.do(sql_command)


def loadInfo(customer_id):
    sql_command = "SELECT * FROM Customer WHERE customer_id = '" + customer_id + "'"
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


def getFirstname(customer_id):
    sql_command = "SELECT firstname FROM Customer WHERE customer_id='" + customer_id + "';"
    response = cursor.do(sql_command)
    return response[0][0]


def accountList(customer_id):
    accounts = []
    for category in ['Investment', 'Saving', 'Credit']:
        sql_command = "SELECT * FROM " + category + "_account WHERE customer_id='" + customer_id + "';"
        response = cursor.do(sql_command)
        for ia in response:  # ia: account_id, customer_id, currency_type, create_time, total_value
            accounts.append((ia[0], category, ia[2], ia[3], ia[4]))
    return accounts


def accountBalance(account_id):
    for category in ['Investment', 'Saving', 'Credit']:
        sql_command = "SELECT * FROM " + category + "_account WHERE account_id='" + account_id + "';"
        response = cursor.do(sql_command)
        if len(response) != 0:
            rp = response[0]
            return [rp[0], rp[4], rp[2]]
    return []


def recentContect(customer_id):
    sql_command = "SELECT in_account_id, in_customer_id FROM ( \
                SELECT DISTINCT in_account_id, in_customer_id FROM Transaction WHERE out_customer_id='" \
                  + customer_id + "') T LIMIT 3;"
    return cursor.do(sql_command)


def transactionHistory(customer_id):
    history = []
    sql_command = "SELECT * FROM Transaction WHERE in_customer_id='" + customer_id + "';"
    history += cursor.do(sql_command)
    sql_command = "SELECT * FROM Transaction WHERE out_customer_id='" + customer_id + "';"
    history += cursor.do(sql_command)
    history.sort(key=lambda s: (s[7], s[8], s[0]))
    return history


def transactionHistory2(account_id):
    history = []
    sql_command = "SELECT transaction_id, in_account_id, out_account_id, amount, currency_type, timepoint_date FROM Transaction WHERE in_account_id='" + account_id + "';"
    history += cursor.do(sql_command)
    sql_command = "SELECT transaction_id, in_account_id, out_account_id, amount, currency_type, timepoint_date FROM Transaction WHERE out_account_id='" + account_id + "';"
    history += cursor.do(sql_command)
    history.sort(key=lambda s: (s[0]))
    return history


def getType(account_id):
    for category in ['Investment', 'Saving', 'Credit']:
        sql_command = "SELECT * FROM " + category + "_account WHERE account_id='" + account_id + "';"
        response = cursor.do(sql_command)
        if len(response) != 0:
            return category
    return ''


def makeTransaction(in_account_id, out_account_id, in_customer_id, out_customer_id, amount, currency_type):
    # currency conversion
    sql_command = "SELECT currency_type FROM Account WHERE account_id='" + in_account_id + "';"
    in_currency_constant = currency_constant[cursor.do(sql_command)[0][0]]
    sql_command = "SELECT currency_type FROM Account WHERE account_id='" + out_account_id + "';"
    out_currency_constant = currency_constant[cursor.do(sql_command)[0][0]]
    in_amount = int(round(amount / currency_constant[currency_type] * in_currency_constant))
    out_amount = int(round(amount / currency_constant[currency_type] * out_currency_constant))

    # verify
    valid = True
    valid = valid and (in_account_id != out_account_id)
    sql_command = "SELECT currency_type FROM Account WHERE account_id='" + out_account_id + "';"
    valid = valid and (currency_type == cursor.do(sql_command)[0][0])
    sql_command = "SELECT customer_id FROM Account WHERE account_id='" + in_account_id + "';"
    valid = valid and (in_customer_id == cursor.do(sql_command)[0][0])
    sql_command = "SELECT customer_id FROM Account WHERE account_id='" + out_account_id + "';"
    valid = valid and (out_customer_id == cursor.do(sql_command)[0][0])
    in_type = getType(in_account_id)
    out_type = getType(out_account_id)
    valid = valid and (in_type != 'Investment') and (out_type != 'Investment')
    if out_type == 'Saving':
        sql_command = "SELECT balance FROM Saving_account WHERE account_id='" + out_account_id + "';"
        valid = valid and (out_amount <= cursor.do(sql_command)[0][0])
    if not valid:
        return '', False

    # make transaction
    if in_type == 'Saving':
        sql_command = "SELECT balance FROM Saving_account WHERE account_id='" + in_account_id + "';"
        balance = cursor.do(sql_command)[0][0]
        balance += in_amount
        sql_command = "UPDATE Saving_account SET balance=" + str(balance) + " WHERE account_id='" + in_account_id + "';"
        cursor.do(sql_command)
    else:  # credit account
        sql_command = "SELECT total_debt FROM Credit_account WHERE account_id='" + in_account_id + "';"
        debt = cursor.do(sql_command)[0][0]
        debt -= in_amount
        sql_command = "UPDATE Credit_account SET total_debt=" + str(debt) + " WHERE account_id='" + in_account_id + "';"
        cursor.do(sql_command)
    if out_type == 'Saving':
        sql_command = "SELECT balance FROM Saving_account WHERE account_id='" + out_account_id + "';"
        balance = cursor.do(sql_command)[0][0]
        balance -= out_amount
        sql_command = "UPDATE Saving_account SET balance=" + str(
            balance) + " WHERE account_id='" + out_account_id + "';"
        cursor.do(sql_command)
    else:  # credit account
        sql_command = "SELECT total_debt FROM Credit_account WHERE account_id='" + out_account_id + "';"
        debt = cursor.do(sql_command)[0][0]
        debt += in_amount
        sql_command = "UPDATE Credit_account SET total_debt=" + str(
            debt) + " WHERE account_id='" + out_account_id + "';"
        cursor.do(sql_command)
    sql_command = "SELECT MAX(transaction_id) FROM Transaction;"
    trandactionID = str(int(cursor.do(sql_command)[0][0]) + 1).zfill(3)
    timepoint_date = datetime.today().strftime("%Y-%m-%d")
    timepoint_time = datetime.now().strftime("%H:%M:%S")
    sql_command = "INSERT INTO Transaction VALUES ('" + trandactionID + "','" + str(in_account_id) + "','" + str(
        out_account_id) + \
                  "','" + str(in_customer_id) + "','" + str(out_customer_id) + "'," + str(amount) + ",'" + str(
        currency_type) + \
                  "','" + str(timepoint_date) + "','" + str(timepoint_time) + "');"
    cursor.do(sql_command)
    return trandactionID, True


def searchTransaction(customer_id, find_type, find_param):
    if find_type in ['timepoint_date', 'transaction_id']:
        sql_command = "SELECT transaction_id, in_account_id, out_account_id, amount, currency_type, timepoint_date FROM Transaction WHERE (in_customer_id='" + customer_id \
                      + "' OR out_customer_id='" + customer_id \
                      + "' )AND " + str(find_type) + "='" + str(find_param) + "';"
    elif find_type == 'account_id':
        sql_command = "SELECT transaction_id, in_account_id, out_account_id, amount, currency_type, timepoint_date FROM Transaction WHERE (in_customer_id='" + customer_id + "' OR out_customer_id='" \
                      + customer_id + "' ) AND (in_account_id='" + str(find_param) + "' OR out_account_id='" + str(
            find_param) + "');"
    elif find_type == 'time_period':
        sql_command = "SELECT transaction_id, in_account_id, out_account_id, amount, currency_type, timepoint_date FROM Transaction WHERE (in_customer_id='" + customer_id \
                      + "' OR out_customer_id='" + customer_id \
                      + "') AND (timepoint_date <= '" + str(find_param[1]) \
                      + "') AND (timepoint_date >= '" + str(find_param[0]) \
                      + "');"
    return cursor.do(sql_command)


def loginHistory(customer_id):
    sql_command = "SELECT timepoint FROM Login_history WHERE customer_id='" + str(customer_id) + "';"
    response = cursor.do(sql_command)
    return response


def updateHistory(customer_id):
    timepoint = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql_command = "INSERT INTO Login_history VALUES ('" + timepoint + "','" + str(customer_id) + "');"
    cursor.do(sql_command)


def balanceTrend(customer_id):
    current_month = datetime.today().strftime("%Y-%m")
    # get months for searching
    month_to_search = []
    for _ in range(12):
        month_to_search.append(current_month)
        y = int(current_month[:4])
        m = int(current_month[5:])
        if m == 1:
            y -= 1
            m = 12
        else:
            m -= 1
        current_month = str(y).zfill(4) + "-" + str(m).zfill(2)

    # calculate current balance
    category = {'Investment': 'total_value', 'Saving': 'balance', 'Credit': 'total_debt'}
    current_balance = 0
    for c in category:
        for currency in currency_constant:
            sql_command = "SELECT SUM(" + category[c] + ") FROM " + c + "_account WHERE (customer_id='" \
                          + customer_id + "') AND (currency_type='" + currency + "');"
            response = cursor.do(sql_command)[0][0]
            if response is None:
                current_balance += 0
            else:
                current_balance += int(float(response) * currency_constant[display_currency] / currency_constant[currency])
    print(current_balance)

    # calculate backward
    monthly_balance = [current_balance]
    monthly_increase = []
    for month in month_to_search:
        monthly_increase.append(0)
        for currency in currency_constant:
            sql_command = "SELECT SUM(amount) FROM Transaction WHERE (out_customer_id='" \
                          + customer_id + "') AND (currency_type='" + currency \
                          + "') AND (timepoint_date LIKE '" + month + "___');"
            response = cursor.do(sql_command)[0][0]
            if response is None:
                trans_out = 0
            else:
                trans_out = float(response)
            sql_command = "SELECT SUM(amount) FROM Transaction WHERE (in_customer_id='" \
                          + customer_id + "') AND (currency_type='" + currency \
                          + "') AND (timepoint_date LIKE '" + month + "___');"
            response = cursor.do(sql_command)[0][0]
            if response is None:
                trans_in = 0
            else:
                trans_in = round(float(response))
            increase = int(
                round((trans_in - trans_out) * currency_constant[display_currency] / currency_constant[currency]))
            monthly_increase[-1] += increase
        monthly_balance.append(monthly_balance[-1] - monthly_increase[-1])
    monthly_balance = monthly_balance[:-1]
    return month_to_search, monthly_increase, monthly_balance


cursor = my_cursor()
# print(balanceTrend('001'))
