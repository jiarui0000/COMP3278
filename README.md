# COMP3278-Readme
*******


## Setup Facial Environment: 
* Install MySQL on local machine
* Create virtual environment using Anaconda by: 
```
conda create -n face python=3.7
conda actiavate face
pip install -r requirements.txt
```

##Setup GUI Enironment: 
please first change the passwd variable in Setup.py to your local Mysql DataBase password. 
The default username is 'root' and authentication method is 'mysql_native_password'. You may change this in Utils.py if it's different. 

Please install all fonts in the ./fonts folder to ensure the font requirements are met and better visual presentation effect is achieved. 
You may select them and open them all by pressing ctrl+O/command+O depending on your system. 

Then run: 
```
pip install -r requirements_GUI.txt
python3 Setup.py
```
to setup package and database in local machine. 


## Run Main Program: 
```
python3 GUI-main.py
```
You may register your own account by facial recognition system. 

You may also view demo customers by logging in our demo account through the following password: 

userID: 002
password: 123

userID: 001
password: 123

userID: 003
password: password1



## Functions on each page: 

Home: 
* Click on each account tab to view the full transaction history of each account. (Investment Accounts are designed to be unable to make transactions, since investment account reflects the amount of investment in the stock market/funds.etc, and can not be transferred.)
* View Total Balance Trend of all of your account. (different currencies are changed to HKD)
* View your latest login history in the right hand side of the interface. 
* Customized Greeting based on time. 

Profile Personalization: 
* Click on the image on home page to proceed to profile page, where you can update your info and password. 
* Upload your personalized image by clicking on the profile image on your profile page. Acceptable types are jpg, jpeg and png. 


Account Page: 
* Click on each account tab to view the full transaction history of each account. (Investment Accounts are unable to make transactions, as mentioned above)
* Click on the right/left arrow to navigate the full list of accounts(only if you have more than 4 accounts)
* Each Accounts are designed to carry one type of balance only. 
* View Account Created Date and Recent Transactions are displayed in the account page directly for convenient checking. 

Transactions: 
* Left hand side displays your recent contacts, their accounts and their profile image. You may click on their profile image to conveniently carry out a transaction with them. If you've carried out transactions with different accounts of the same person, their account will be displayed separately and their profile image may appear multiple times corresponding to each different account. 
* Right hand side displays the Transaction and Transaction Search Frame. You may make transactions or search transaction history related to you here. 

Analysis: 
* On Analysis page you may view a deep analysis of your balance and transactions, including monthly change of each account, annual net flow of each account, and balance weight of each account in yout total asset. 




## To remove existing database and reinitialize: 

To remove facial data, please delete all files in ./data or execute: 
```
rm -rf data
mkdir data
```
Then you may remove SQL data through: 
```
python3 -c "from Setup import *; remove_all()"
```
