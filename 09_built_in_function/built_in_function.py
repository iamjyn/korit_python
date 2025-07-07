#내장함수
#파이썬에서 기본적으로 지원하는 함수(Built-in-Function)
from tkinter.font import names

#abs()
#숫자의 절댓값을 리턴하는 함수
print(abs(-10))
print(abs(-1.2))


#all()
#all(x)는 반복 가능한 데이터 x를 입력값으로 받으면
#이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다.
#모든 요소가 참인가? 를 물어보는 함수
num_list = [1, 2, 0, 4] #0이 불리언으로 따졌을 때 False임
print(bool(0)) #False
print(all(num_list)) #False

#빈 리스트 같은 경우, 안에 어떤 요소도 존재하지 않는다.
#따라서 "거짓인 요소가 하나라도 있는가?"
#거짓인 요소거 없기 때문에 모든 요소가 참이라는 조건이 위배되지 않는다. => 공허한 진실
num_list = []
print(bool(num_list)) #False
print(all(num_list)) #True


#any()
#any(x)는 반복 가능한 데이터 x를 입력 값으로 받으면
#이 x의 요소가 하나라도 참이면 True, 요소가 모두 거짓이면 False를 리턴한다.
num_list = [1, 2, 0, 4]
print(any(num_list)) #True

num_list = [0, 0, 0, 0]
print(any(num_list)) #False


#chr() => 잘안씀
#chr(i)는 유니코드를 넣으면 해당 문자로 리턴하는 함수
print(chr(97)) #a
print(chr(44032)) #가


#ord() <=> chr() 과 반대의 개념
#문자의 유니코드 숫자 값을 리턴하는 함수
print(ord("가"))
print(ord("a"))


#dir() => 잘안씀
#객체가 지닌 변수나 함수를 보여주는 함수
name = "python"
# print(dir(name))


#divmod()
#2개의 숫자 a, b를 입력받고, a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴
print(divmod(7, 3))


#enumerate()
#순서가 있는 데이터(리스트, 튜플, 문자열) 입력받아서
#인덱스 값을 포함하는 enumerate객체를 리턴
#인덱스와 값을 두개의 변수로 언팩
a_list = ["name", "age", "birth"]

for i, value in enumerate(a_list):
    print(f"{i + 1}. {value}")


#eval() => 웹개발 측면에서는 보안상 위협이 될 수 있음(참고 - 파이썬, 자바스크립트에서 가능한 함수)
#문자열로 구성되어 있는데 해당 문자열을 싫행한 값이 필요할 때 사용
a_str = "1 + 2"
print(eval(a_str))
print(eval("divmod(7,2)"))


#filter()
#첫 번째 인수로 함수, 두 번째 인수로 반복 가능한 데이터
#그리고 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때
#리턴값이 참인 것만 묶어서 리턴

def positive(x):
    return  x > 0

print(list(filter(positive, [1, -2, 5, -3, 8])))


#hex() => 잘안씀
#정수를 입력받아 16진수 문자열로 변환하여 리턴하는 함수
print(hex(234))
print(hex(12))


#oct() => 잘안씀
#정수를 입력받아 8진수 문자열로 변환하여 리턴하는 함수
print(oct(34))


#id() => 잘안씀
#객체를 입력받아서 고유 주솟값(레퍼런스)를 리턴하는 함수
a = 3
print(id(a))


#map()
#map은 입력받은 데이터의 각 요소에 함수를 적용한 결과를 리턴하는 함수
def two_time(x):
    return x * 2

print(list(map(two_time, [1, 2, 3, 4])))


#max()
#반복 가능한 데이터 중에서 최댓값을 리턴
num_list = [1, 2, 13, 15, 23, 18, 55, 17, 46]
print(max(num_list))


#min()
#반복 가능한 데이터 중에서 최솟값을 리턴
num_list = [1, 2, 13, 15, 23, 18, 55, 17, 46]
print(min(num_list))


#open()
#open(파일이름, 모드)은 파일이름과 모드를 입력받아 파일 객체를 리턴하는 함수
# w 쓰기모드
# r 읽기 모드
# a 추가 모드
# encoding="utf-8" (한글 깨지지 않게)
# open을 통해 열어줬다면 반드시 close를 해줘야 함
file = open("예시.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

# open과 동시에 close를 한방에 할 수 있는 방법 (as=별칭)
# => 들여쓰기가 되면서 내부에 코드블록이 생겨서 알아서 닫힘
with open("예시.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


#pow()
#첫 번째 인수를 두 번째 인수만큼 거듭제곱
print(pow(3, 10)) #3을 10번 거듭제곱한 값이 나옴
print(pow(2, 4))


#range()
#range(시작, 끝, 간격) for문과 함께 자주 사용
#반복 가능한 객체로 만들어서 리턴
print(list(range(5, 100, 5)))


#round()
#반올림
print(round(4.4))
print(round(8.9))
print(round(5.1284, 2)) #반올림해서 두 번째 인수까지 나타내라


#sum()
#합계를 구하는 함수
num_list = [123, 5820, 475, 863]
print(sum(num_list))


#실습문제
data = ["apple", "banana", "cherry", "grape", "mango", "blueberry", "lemon"]

for fruit, value in enumerate(data):
    print(f"{fruit + 1}. {value}")

# 1. apple
# 2. banana ~

#index가 짝수인 요소만 출력 (인덱스 : 요소)

data = ["apple", "banana", "cherry", "grape", "mango", "blueberry", "lemon"]

for fruit, value in enumerate(data):
    if fruit in range(0:6:2)
    print(f"({fruit} : {value})")

