# python -m pip install pymysql
from db import connect as db

insert_sql = "INSERT INTO my_member(username, password) VALUES(%s, %s)"
db.cursor.execute(insert_sql, ["love", "1234"])

db.conn.commit()


# num = 0

# try:
#     cursor.execute(insert_sql, ["love", "1234"])
# except Exception as e:
#     num = num + 1
#     print("터짐")
# try:
#     cursor.execute(insert_sql, ["love", "1234"])
# except Exception as e:
#     num = num + 1
#     print("터짐")
# try:
#     cursor.execute(insert_sql, ["love", "1234"])
# except Exception as e:
#     num = num + 1
#     print("터짐")

# if num == 0:
#     conn.commit()
# else:
#     conn.rollback()
