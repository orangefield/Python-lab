# DAO : Data Access Object

from db import connect as db


# insert_one(username="ssar", password="1234")
def insert_one(**data):  # {"username":"ssar", "password":"1234"}
    sql = "INSERT INTO my_member(username, password) VALUES(%(username)s, %(password)s)"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1


def select_all():
    sql = "SELECT * FROM my_member"
    db.cursor.execute(sql)  # 날릴 게 없으니까 두 번째 인자X
    rows = db.cursor.fetchall()  # 결과
    return rows


def select_one(**data):
    sql = "SELECT * FROM my_member WHERE id = %(id)s"
    db.cursor.execute(sql, data)
    row = db.cursor.fetchone()  # 결과
    return row


def update_one(**data):  # 실제로는 WHERE절에 받는 id는 따로 받아야 한다
    sql = "UPDATE my_member SET username=%(username)s, password=%(password)s WHERE id=%(id)s"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1


def delete_one(**data):
    sql = "DELETE FROM my_member WHERE id=%(id)s"
    try:
        db.cursor.execute(sql, data)
    except Exception as e:
        db.conn.rollback()
        return -1
    db.conn.commit()
    return 1
