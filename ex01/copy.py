# 얕은 복사
list1 = [1,2,3] 
list2 = list1 # 같은 id : 안의 값을 전부 비교

print(id(list1))
print(id(list2))

# 깊은 복사 : 변경 요청이 있을 때 복사
list3 = list1.copy() 
print(id(list3)) # 다른 id
print(list1 is list3) # 주소만 비교