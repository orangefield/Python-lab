from pymysql import connect, cursors

conn = connect(
    host="localhost",
    user="green",
    password="green1234",
    db="greendb",
    charset="utf8"  # pymysql은 utf-8 작대기 없이
)

cursor = conn.cursor(cursors.DictCursor)  # 기본은 tuple
