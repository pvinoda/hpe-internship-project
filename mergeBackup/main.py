import os
import time
os.chdir('C:\\Users\\vbpr\\Desktop\\mergeTry')
dbNames = []
# collecting db Names
for f in os.listdir():
    if f.find("db") != -1:
        dbNames += [f]
# print(dbNames)
# creating clone of the first db
os.system('sqlite3 {}'.format(dbNames[0]))
time.sleep(3)
os.system('.clone connected.db')




