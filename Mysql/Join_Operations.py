
import pymysql as mc
data=mc.connect(host='localhost', user='root',password='root',database='DB1')
database=data.cursor()

# Inner Join OPeration
def InnerJoin():
    sql= "select sample.name as name, sample.age as age, sampledatabase.address as address, " \
         "sampledatabase.Gender as Gender From sample INNER JOIN sampledatabase ON sample.id=sampledatabase.id"
    database.execute(sql)
    myresult=database.fetchall()
    for dat in myresult:
        print(dat)
# Left Join Operation
def LeftJoin():
    LeftSql="select sample.name as name, sample.Age as Age, sampledatabase.address as address, " \
            "sampledatabase.Gender as Gender From sample INNER JOIN sampledatabase ON sampledatabase.id=sample.id"
    database.execute(LeftSql)
    LeftResult=database.fetchall()
    for dat in LeftResult:
        print(dat)
def RightJoin():
    sql= "select sample.name as name, sample.Age as Age, sampledatabase.address as address, " \
         "sampledatabase.Gender as Gender From sample Right JOIN sampledatabase ON sample.id=sampledatabase.id"
    database.execute(sql)
    myresult=database.fetchall()
    for dat in myresult:
        print(dat)
def OuterJoin():
    sql= "select * From sample FULL Outer JOIN sampledatabase ON sample.id=sampledatabase.id"
    database.execute(sql)
    myresult=database.fetchall()
    for dat in myresult:
        print(dat)
def Join():
    sql= "select * From sample JOIN sampledatabase ON sampledatabase.id=sample.id"
    database.execute(sql)
    myresult=database.fetchall()
    for dat in myresult:
        print(dat)
value=input('Enter a value between 0 to  \n \
                                          0: Inner Join : \n \
                                          1: LeftJoin : \n \
                                          2: RightJoin : \n \
                                          3: OuterJoin : \n \
                                          4: Join : \n \
             Select Option From above : ')
if(value=='0'):
    InnerJoin()
elif(value=='1'):
    LeftJoin()
elif(value=='2'):
    RightJoin()
elif(value=='3'):
    OuterJoin()
elif(value=='4'):
    Join()
else:
    print("WARNING :OUT of Range SELECT number between 0 to 3 ")