import sqlalchemy as db
import mysql.connector as mysql
from random import randint
# connection=mysql.connect(host='localhost', user='root', password='python')
connection=mysql.connect(host='localhost', user='root', password='python', database='students')
cursor=connection.cursor()

# cursor.execute('CREATE DATABASE IF NOT EXISTS students')
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())

cursor.execute('CREATE TABLE IF NOT EXISTS points(id INT AUTO_iNCREMENT PRIMARY KEY, num1 INT, num2 INT)')
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.close()
meta=db.MetaData()
user=db.Table('points',meta,db.Column('id',db.Integer(),primary_key=True),db.Column('num1',db.Integer()),db.Column('num2',db.Integer()))
print(user.c)
engine=db.create_engine("mysql+mysqlconnector://root:python@localhost:3306/students")
meta.create_all(engine)
connection=engine.connect()

for i in range(int(input('Введите количество записей '))):
    add_1=user.insert().values(num1=randint(0,9),num2=randint(0,9))
    connection.execute(add_1)

connection.commit()
sel=db.select(user.c.num1,user.c.num2)
rez=connection.execute(sel).fetchall()

summ=sum([elem[0]+elem[1] for elem in rez])/len(rez)
print(summ,len(rez))
if summ>len(rez):
    delit=user.delete().where(user.c.id==4)