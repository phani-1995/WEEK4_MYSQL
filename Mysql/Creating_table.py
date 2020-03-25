import pymysql
mydb = pymysql.connect(
  host='localhost',
  user='root',
  passwd='root',
  database='DB1'
)
mybase = mydb.cursor()
mybase.execute("Create table Details(First_Name varchar(50), Last_Name varchar(50), Age int, Gender varchar(10))")


