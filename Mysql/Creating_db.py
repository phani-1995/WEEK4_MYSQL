import pymysql
mydb=pymysql.connect(host="localhost",user='root',password='root')
mybase=mydb.cursor()
if(mydb):
    print("connection Sucessfull")
else:
    print("connection is UnsuccessFull")
mybase.execute("CREATE DATABASE DB1")