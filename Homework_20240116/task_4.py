import sqlalchemy as db
import mysql.connector as mysql
import csv

# connection=mysql.connect(host='localhost', user='root', password='python')
connection=mysql.connect(host='localhost', user='root', password='python', database='students')
cursor=connection.cursor()

# cursor.execute('CREATE DATABASE IF NOT EXISTS students')
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())

cursor.execute('CREATE TABLE IF NOT EXISTS points4(id INT AUTO_iNCREMENT PRIMARY KEY, name VARCHAR(20), comment VARCHAR(150))')
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.close()
meta=db.MetaData()
user=db.Table('points4',meta,db.Column('id',db.Integer(),primary_key=True),db.Column('name',db.Text(),nullable=True),db.Column('comment',db.Text(),nullable=True))
print(user.c)
engine=db.create_engine("mysql+mysqlconnector://root:python@localhost:3306/students")
meta.create_all(engine)
connection=engine.connect()
add_1=user.insert().values(name='статья 1',comment='абракатабра')
connection.execute(add_1)
add_1=user.insert().values(name='статья 2',comment='не знаю что писать')
connection.execute(add_1)
add_1=user.insert().values(name='статья 3',comment='закончилось. уф')
connection.execute(add_1)
connection.commit()

sel=user.delete().where(user.c.id==2)
rez = connection.execute(sel)

sel=user.update().values(comment='Hello word').where(user.c.id==3)
rez = connection.execute(sel)
connection.commit()

rez=connection.execute(user.select()).fetchall()

with open('stat.csv','w', encoding='windows-1251',newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(rez)