import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="Ishani@123",database="test")
if mycon.is_connected():
    print("Successful")
