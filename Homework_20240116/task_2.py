import sqlalchemy as db
import mysql.connector as mysql
from random import randint
# connection=mysql.connect(host='localhost', user='root', password='python')
connection=mysql.connect(host='localhost', user='root', password='python', database='students')
cursor=connection.cursor()

# cursor.execute('CREATE DATABASE IF NOT EXISTS students')
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())

cursor.execute('CREATE TABLE IF NOT EXISTS points1(id INT AUTO_iNCREMENT PRIMARY KEY, num1 INT, num2 INT)')
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.close()
meta=db.MetaData()
user=db.Table('points1',meta,db.Column('id',db.Integer(),primary_key=True),db.Column('num1',db.Integer()),db.Column('num2',db.Integer()))
print(user.c)
engine=db.create_engine("mysql+mysqlconnector://root:python@localhost:3306/students")
meta.create_all(engine)
connection=engine.connect()
kol=int(input('Введите количество записей '))
for i in range(kol):
    add_1=user.insert().values(num1=randint(0,9),num2=randint(0,9))
    connection.execute(add_1)

connection.commit()

print(connection.execute(user.select()).fetchall())
sel_id=randint(1,kol+1)
sel=db.select(user.c.num1,user.c.num2).where(user.c.id==sel_id)
rez=connection.execute(sel).fetchall()
print(rez)
if rez[0][0]%2==0 and rez[0][1]%2==0:
    sel=user.delete().where(user.c.id==sel_id)
    rez = connection.execute(sel)
elif rez[0][0]%2!=0 and rez[0][1]%2!=0:
    sel=user.update().values(num1=2,num2=2).where(user.c.id==sel_id)
    rez = connection.execute(sel)
connection.commit()
print(connection.execute(user.select()).fetchall())