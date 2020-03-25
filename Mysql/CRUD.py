import pymysql

database = pymysql.connect(host="localhost", user='root', password='root', database='DB1')
sample = database.cursor()


# Step 1: Created a DataBase
def CreateDataBase():
    sample.execute("Create DataBase Sample")


# Step 2: Created a Table in data Base
def CreateTable():
    sample.execute("Create Table sample(id int Not Null,name varchar(50),age int(10),DOB DATE)")
    print("Created Table : ")


# Step 3: Inserting values in Table
def InsertTable():
    SqlValues = 'Insert into sample(id, name, age, DOB) values(%s, %s, %s, %s)'
    value = [(1, 'Phanindra', 23, 19950601), (2, 'Abhilash', 24, 19941220), (3, 'Karthik', 23, 19930803),
             (4, 'KIM', 27, 19920511)]
    sample.executemany(SqlValues, value)
    print("Inserted SuccessFully : ")
    database.commit()


# Step 4: Read data in Table
def ReadTable():
    sample.execute('Select * FROM sample')
    value = sample.fetchall()
    for data in value:
        print(data)


# Step 5: Update Table
def UpdateTable():
    value = "Update sample set age=26,DateOfBorth =19941212,name='shiva' where id=4"
    sample.execute(value)
    database.commit()


# Step 6: Deleteing Table Values
def DeleteTable():
    value = 'Delete from sample where DateOfBorth=19940401'
    sample.execute(value)
    database.commit()


val = input("Enter a Value Between 0 to 6 For 0: Create DataBase \n \
                                            1: Create Table \n \
                                            2: Show Table \n \
                                            3: Insert New Values \n \
                                            4: Read the data of Table \n \
                                            5: Updata Value of perticular row \n \
                                            6: Delete Value of row \n \
           Selected value is : ")

if (val == '0'):
    CreateDataBase()

elif (val == '1'):
    CreateTable()

elif (val == '2'):
    sample.execute("Show Tables")
    for data in sample:
        print(data)

elif (val == '3'):
    InsertTable()

elif (val == '4'):
    ReadTable()

elif (val == '5'):
    UpdateTable()
elif (val == '6'):
    DeleteTable()
else:
    print('Entered Value is out of ranged please enter between 0 to 1 ')