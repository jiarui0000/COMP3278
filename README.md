# COMP3278-Readme


#Setup Facial Environment: 
* Install MySQL on local machine
* Create virtual environment using Anaconda by: 

conda create -n face python=3.7

conda actiavate face

pip install -r requirements.txt


#Setup GUI Enironment: 
please first change the passwd variable in Setup.py to your local Mysql DataBase password. 
The default username is 'root' and authentication method is 'mysql_native_password'. You may change this in Utils.py if it's different. 

Please install all fonts in the ./fonts folder to ensure the font requirements are met and better visual presentation effect is achieved. 
You may select them and open them all by pressing ctrl+O/command+O depending on your system. 

Then run: 
pip install -r requirements_GUI.txt
python3 Setup.py

to setup package and database in local machine. 


#Run Main Program: 

python3 GUI-main.py

#To remove existing database and reinitialize: 

Please delete all files in ./data or execute: 

rm -rf data

mkdir data

python3 -c "from Setup import *; remove_all()"

