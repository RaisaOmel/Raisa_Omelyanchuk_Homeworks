import mysql.connector as mysql
# connection=mysql.connect(host='localhost', user='root', password='python')
connection=mysql.connect(host='localhost', user='root', password='python', database='magazin')
cursor=connection.cursor()
# cursor.execute('CREATE DATABASE IF NOT EXISTS magazin')
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())
cursor.execute('CREATE TABLE IF NOT EXISTS vitalur(id INT AUTO_iNCREMENT PRIMARY KEY, name_product VARCHAR(150), price DECIMAL(8,2), count INT(5))')
cursor.execute('CREATE TABLE IF NOT EXISTS santa(id INT AUTO_iNCREMENT PRIMARY KEY, name_product VARCHAR(150), price DECIMAL(8,2), count INT(5))')
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.execute("INSERT INTO vitalur (name_product, price, count) VALUES ('Крупа гречневая 0.5кг',3.2, 200),('Крупа перловая 0.5кг',1.52, 100),('Крупа пшенная 0.5кг',0.82, 150)")
connection.commit()
cursor.execute("INSERT INTO santa (name_product, price, count) VALUES ('Яйцо упаковка 10шт',3.2, 50),('Икра банклажанная 0.45кг',5.52, 40),('Икра кабачковая 0.45кг',4.12, 40)")
connection.commit()
formula='SELECT name_product FROM vitalur UNION SELECT name_product FROM santa ORDER BY name_product'
cursor.execute(formula)
print(cursor.fetchall())
formula='SELECT *  FROM vitalur WHERE price=10'
cursor.execute(formula)
print(cursor.fetchall())
formula='SELECT *  FROM santa WHERE count<5 OR count>15'
cursor.execute(formula)
print(cursor.fetchall())
formula='SELECT name_product FROM vitalur WHERE name_product LIKE "m%" UNION SELECT name_product FROM santa WHERE name_product LIKE "m%"'
cursor.execute(formula)
print(cursor.fetchall())
connection.close()