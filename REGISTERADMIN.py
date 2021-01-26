import pymysql

con = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS LOGIN (USERNAME VARCHAR(255), PASSWORD VARCHAR(255))")
cur.execute("CREATE TABLE IF NOT EXISTS DEPARTMENT (DEPARTMENT_ID INTEGER, DEPARTMENT_NAME VARCHAR(255))")
cur.execute("INSERT INTO LOGIN VALUES('Admin', '1234')")
con.commit()
con.close()
