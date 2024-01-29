import mysql.connector as mysql
import sqlalchemy as db

class Connect:
    def __init__(self,user,connection):
        self.user=user
        self.connection=connection
    def get_sel(self,*args):
        print(self.connection.execute(self.user.select()).fetchall())
        if args[0] and not args[1] and not args[2] and args[0].isdigit():
            add_1 = self.user.insert().values(num=3)
            self.connection.execute(add_1)
        elif args[0] and args[1] and not args[2] and args[1].isdigit():
            del_1 = self.user.delete().where(self.user.c.id ==1)
            self.connection.execute(del_1)
        elif args[2] and args[2].isdigit():
            sel = self.user.update().values(num=77).where(self.user.c.id == 3)
            rez = self.connection.execute(sel)

        self.connection.commit()
        print(self.connection.execute(self.user.select()).fetchall())

# connection=mysql.connect(host='localhost', user='root', password='python')
connection=mysql.connect(host='localhost', user='root', password='python', database='students')
cursor=connection.cursor()

# cursor.execute('CREATE DATABASE IF NOT EXISTS students')
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())

cursor.execute('CREATE TABLE IF NOT EXISTS points3(id INT AUTO_iNCREMENT PRIMARY KEY, num INT)')
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.close()
meta=db.MetaData()
user=db.Table('points3',meta,db.Column('id',db.Integer(),primary_key=True),db.Column('num',db.Integer(),nullable=True))
print(user.c)
engine=db.create_engine("mysql+mysqlconnector://root:python@localhost:3306/students")
meta.create_all(engine)
connection=engine.connect()
add_1=user.insert().values(num=0)
connection.execute(add_1)
add_1=user.insert().values(num=1)
connection.execute(add_1)
add_1=user.insert().values(num=2)
connection.execute(add_1)
connection.commit()

baz=Connect(user,connection)
baz.get_sel(input('введите что-нибудь или ничего ').strip(),input('введите что-нибудь или ничего ').strip(),input('введите что-нибудь или ничего ').strip())


