from unittest import result
import member_dao as dao


# 한 건 insert
def set_data():
    result = dao.insert_one(username="hong", password="1234")
    print(f"result:{result}")


# 전부 select
def get_datas():
    my_members_entity = dao.select_all()
    print(my_members_entity)


# 한 건 select
def get_data():
    my_member_entity = dao.select_one(id=1)  # id 집어넣기
    print(my_member_entity)


# 한 건 update
# Validation Check 필요
def update_data():
    result = dao.update_one(id=1, username="kkk", password="8989")
    print(f"result:{result}")


# 한 건 delete
def delete_data():
    result = dao.delete_one(id=1)
    print(f"result:{result}")


# delete_data()
