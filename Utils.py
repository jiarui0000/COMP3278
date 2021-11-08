#!/usr/bin/env python
# coding: utf-8



import os
import mysql.connector as mysql


class my_cursor():
    def __init__(self,user="root",passwd="u3563782",host="localhost"):
        self.myconn=mysql.connect(host=host,user=user,passwd=passwd,auth_plugin='mysql_native_password')
        self.cursor=self.myconn.cursor()
        if not ((('COMP3278_G12',) in self.do("show databases")) or (('comp3278_g12',) in self.do('show databases'))):
            self.setup()
        self.do('use COMP3278_G12')
    def execute_file(self,filename):
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')
        for command in sqlCommands:
            try:
                if command.strip() != '':
                    self.cursor.execute(command)
            except IOError:
                print ("Command skipped: "+msg)
    def do(self,command):
        self.cursor.execute(command)
        try:
            return self.cursor.fetchall()
        except:
            return
    def setup(self):
        self.execute_file('SQL/table.sql')
        self.execute_file('SQL/test_data.sql')
def isAllPresent(str):
    special = ("^(?=.*[a-z])(?=." +"*[A-Z])(?=.*\\d)" +"(?=.*[-+_!@#$%^&*., ?]).+$")
    p = re.compile(special)
    if (str == None):
        print("No")
        return
    if(re.search(p, str)):
        return True
    else:
        return False

