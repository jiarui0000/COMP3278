from Utils import *
passwd='20211030'
cursor=my_cursor(passwd=passwd)
if not ((('COMP3278_G12',) in cursor.do("show databases")) or (('comp3278_g12',) in cursor.do('show databases'))):
    cursor.setup()
    print('Setup Completed!')
    x=1

def remove_all():
    for i in ['COMP3289_G12','comp3278_g12']:
        try:
            cursor.do('drop database '+str(i))
            print('drop successfully')
        except:
            x=1

