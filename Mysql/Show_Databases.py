import pymysql
mydb = pymysql.connect(
  host='localhost',
  user='root',
  passwd='root',
  database='DB1'
)
mybase=mydb.cursor()
mybase.execute("SHOW DATABASES")
for i in mybase:
    print(i)