import pymysql
mydb=pymysql.connect(host="localhost",user='root',password='root',database='DB1')
mybase=mydb.cursor()
sqlForm="Insert into details(First_Name, Last_Name, Age, Gender) values(%s,%s,%s,%s)"
rawData=[('Phanindra','Jallavaram',23,"Male"),('Karthik','Tallapally',24,"Male"),('Lokesh','Goud',25,"Male"),
         ('Abhilash','guddipati',24,"Male"),]
mybase.executemany(sqlForm,rawData)
mydb.commit()