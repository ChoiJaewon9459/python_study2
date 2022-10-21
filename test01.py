from decimal import Decimal
import math as ma
#print("안녕")

num = 3 + 3
num2  = 3- 3
num3  = 3 * 3
num4  = 3 / 3

print(num)
print(num2)
print(num3)
print(num4)

num = 3 ** 3

print(num)
num = 2/3
print(num)
num = 1.1 + 0.1
print(num)
num = Decimal('1.1') + Decimal('0.1')
print(num)

name = "jaewon"
age = 10.5
print("내 이름은 "+name+"내 나이는"+str(age))
print(f"내 이름은 {name}내 나이는{age}")
#포맷은 재설정
#
print("내 이름은 %s 내 나이는 %d",(name,age))

#list 에 [1,2,3,4] 
# 0번쨰 변경할수 있음 이유 리스트는 가변이라서 

chage_string = string.replace('가','하')

print(id(string))
print(id(chage_string))