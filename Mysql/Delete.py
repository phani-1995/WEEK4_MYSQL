import pymysql
mydb=pymysql.connect(host="localhost",user='root',password='root',database='DB1')
mybase=mydb.cursor()
sql="DELETE From details WHERE Last_Name='Goud'"
mybase.execute(sql)
mydb.commit()