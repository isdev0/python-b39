import pymysql


connection = pymysql.connect(host="localhost", port=3306, database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
