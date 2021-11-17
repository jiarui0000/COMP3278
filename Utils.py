#!/usr/bin/env python
# coding: utf-8



import os
import mysql.connector as mysql
from PIL import Image, ImageDraw
import numpy as np


class my_cursor():
    def __init__(self,user="root",passwd="20211030",host="localhost"):
        self.myconn=mysql.connect(host=host,user=user,passwd=passwd,auth_plugin='mysql_native_password')
        self.cursor=self.myconn.cursor()
        if not ((('COMP3278_G12',) in self.do("show databases")) or (('comp3278_g12',) in self.do('show databases'))):
            self.setup()
            x=1
        self.do('use COMP3278_G12')
    def execute_file(self,filename):
            fd = open(filename, 'r')
            sqlFile = fd.read()
            fd.close()
            sqlCommands = sqlFile.split(';')
            for command in sqlCommands:
                try:
                    if command.strip() != '':
                        self.cursor.execute(command+";")
                        # self.myconn.commit()
                except Exception as e:
                    logger.error('The following is the error message '+ str(e))

    def do(self,command):
        self.cursor.execute(command)
        response = []
        try:
            response = self.cursor.fetchall()
        except:
            return
        self.myconn.commit()
        return response

    def edit(self,command, updates):
        self.cursor.execute(command, updates)
        self.myconn.commit()
        return

    def setup(self):
        self.execute_file('SQL/table.sql')
        self.execute_file('SQL/test_data.sql')
        print('Setup Completed!')
    def close(self):
        self.cursor.close()
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
def crop(name):
    # Open the input image as numpy array, convert to RGB
    img=Image.open(name).convert("RGB")
    npImage=np.array(img)
    h,w=img.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,min(h,w),min(h,w)],0,360,fill=255)

    # Convert alpha Image to numpy array
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save(name[:-4]+'_photo.png')
    im = Image.open(name[:-4] + '_photo.png')

    a = min(im.size)
    im = im.crop((0, 0, a, a))
    im.save(name[:-4] + '_photo.png')
def cropping(customer_id):
    try:
        crop("./user-photo/"+str(customer_id)+'.jpg')
    except:
        x=1
    try:
        crop("./user-photo/"+str(customer_id)+'.png')
    except:
        x=1
    try:
        crop("./user-photo/"+str(customer_id)+'.jpeg')
    except:
        x=1
