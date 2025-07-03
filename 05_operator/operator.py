#산술연산자
num1 = 30
num2 = 12
print(f"num1 + num2 = {num1 + num2}") #덧셈
print(f"num1 - num2 = {num1 - num2}") #뺄셈
print(f"num1 * num2 = {num1 * num2}") #곱셈
print(f"num1 / num2 = {num1 / num2}") #나눗셈 (실수 몫을 반환) => 정처기 시험문제 유의
print(f"num1 // num2 = {num1 // num2}") #나눗셈 (정수 몫을 반환) => 정처기 시험문제 유의
print(f"num1 % num2 = {num1 % num2}") #나눗셈 (나누고 남은 나머지 반환) => 정처기 시험문제 유의

#대입연산자
x = 10
x += 5 # x = x + 5 => 15
x *= 2 # x = x * 2 => 30 (위에서 15가 되었으니)
# x /= 5 # x= x / 5 => 6.0 (실수 몫)
x //= 5 # = x / 5 => 6 (정수 몫)

#비교연산자
x = 10
y = 20
z = 10
print(x == z) #True
print(x > y) #False
print(x == y) #False
print(x != z) #False
print(x <= y) #True
print(x >= z) #True

#논리연산자
a = True
b = False
print(not a and b) #False
print(a or b) #True
print(not b) #True

