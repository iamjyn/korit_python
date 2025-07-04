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

#조건연산자(삼항연산자)
a = 10
b = 20
max_value = a if a > b else b

#위에 식을 풀어 쓰면 아래와 같음
if a > b:
    max_value = a
else:
    max_value = b

print(max_value)

#홀수 판별
num = 7
result = "짝수" if num % 2 == 0 else "홀수"
print(result)

#참일 때 반환값 if 조건, else 거짓일 때 반환값

