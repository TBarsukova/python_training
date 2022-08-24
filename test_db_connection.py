import pymysql
import pymysql.cursors

connection = pymysql.connect(
    host="127.0.0.1", 
    database="addressbook", 
    user="root", 
    password="",
    )

with connection:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM addressbook"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
