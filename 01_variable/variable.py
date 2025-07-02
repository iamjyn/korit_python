# 주석 처리 (컨트롤 + / ) 혹은 앞뒤로 쌍따옴표 3개
from calendar import firstweekday

# 변수
# => 어떠한 값들을 상자에 담아 이름을 붙이는 것

#변수 => 문자열 (문자를 기입할 때 따옴표 or 쌍따옴표 안에 작성)
last_name = "정"
print("제 성은 " + last_name)
first_name = "유나"
name = last_name + first_name #문자열과 문자열은 더할 수 있다.
print(name)
#a = name - last_name #문자열에서 뺄셈은 할 수 없다.
b = name * 3 #문자열을 곱할 수 있다. 단, 나누기는 할 수 없다.
print(b)

#변수 => 정수
age = 27

#변수 => 실수
pie = 3.141592

#변수 => 여러줄을 문자열로 쓸때 (따옴표 or 쌍따옴표 앞뒤로 3개씩)
str1 = """
안녕하세요.
반갑습니다.
"""

str2 = '''
안녕하세요.
반갑습니다.
'''

print(str1)

num1 = 2.1
num2 = 4.2
print(num1 + num2)
"""
컴퓨터는 이진수만 저장하게 되는데 소수는 정확하게 떨어지는 이진법으로 저장이 불가능하다.
그래서 근사값을 저장하고 연산을 하게 되면서 실제의 값보다 아주 조금 더 크게 나온다.
"""

#boolean
"""
참과 거짓의 변수는 is 또는 has 또는 can 등을 앞에 붙여주는 게 좋다
부정은 보통 쓰지 않는다
"""

is_mz = True
is_empty = False
str3 = "python" #True
str4 = "" #False

#실습
#내 정보 출력해보기

my_name = "정유나"
my_age = 20 + 9
my_weight = 20.5
is_woman = True
is_student = False

print("제 이름은 " + my_name)
print("제 나이는", my_age) #문자열과 숫자 더할 시에 콤마 사용 (콤마는 공백 한칸 포함됨)
print("제 몸무게는", my_weight)
print("여자인가요? :", is_woman)

print(f"제 이름은 {my_name}, 제 나이는 {my_age}살 입니다.\n제 몸무게는 {my_weight}입니다. 여자 인가요? : {is_woman}")

#"안녕하세요" => 문자열로 쌍따옴표 입력시 (역슬래쉬+쌍따옴표)
str5 = "\"안녕\t하세요\"" #tap키=스페이스4번=(역슬래쉬+t)
print(str5)

num3 = 10
num4 = 20
print(f"num1 + num2 = {num3 + num4}")