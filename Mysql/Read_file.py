import pymysql

mydb = pymysql.connect(host='localhost', user='root', password='root', database='DB1')

mybase = mydb.cursor()
mybase.execute("select * from details")
myresult = mybase.fetchall()
for row in myresult:
    print(row)