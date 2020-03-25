import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='root',database='DB1')
mybase=mydb.cursor()
sql="UPDATE details SET Age=24 WHERE First_Name='Phanindra'"
mybase.execute(sql)
mydb.commit()