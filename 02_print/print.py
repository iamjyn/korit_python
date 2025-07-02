#입력받기 => 사용자에게 입력받음
#input()
# a = input()
# print("내가 입력한 것 : " + a)

# user_name = input("이름을 입력하세요 : ")
# print("사용자 이름 : " + user_name)

# age = input("나이를 입력하세요 : ")
# print(type(age))
# print("사용자 나이 : " + age)
#input()으로 입력 받은 모든 값은 문자열 형태이다.

#출력하기 다양한 방식
# last_name = "정" #문자열 str
# first_name = "유나"
# name = last_name + first_name
# age = 29 #int
# phone_number = "01012345678" #숫자는 맨 앞에 0이 나올 수 없음 => 그러한 경우 쌍따옴표로 문자열 처리 해야함

# print("hi" + "hello" + "world")
# print("hi", "hello", "world")
# print("내 전화번호는 " + phone_number + " 입니다.")
# print("제 나이는 " + age + " 입니다.")
# print("제 나이는 {} 입니다.".format(age)) #옛날 방식임
# print("제 이름은 {}, 나이는 {} 입니다.".format(name, age))
# print("제 이름은 {nm}, 나이는 {ag} 입니다.".format(nm="홍길동", ag=18))

# print(f"제 나이는 {age} 입니다.") #f-string방식

# print("제 나이는 %s 입니다." % age) #모든 문자를 문자열로 포맷팅해서 출력
# print("제 나이는 %d 입니다." % age) #모든 문자를 정수형으로 포맷팅해서 출력
# print("제 이름은 %s 이고, 제 나이는 %d 입니다." %(name, age))
# print("Loading...%d%%" % 98) #문자 그대로 퍼센트를 사용하고 싶다면 '퍼센트 2번'(%%) 사용하면 됨
# print("%10s" % "hi") # 숫자: 문자열 포함 길이 (문자열 앞에 공백 포함)
# print("%-10s" % "hi") # -숫자 : 문자열 포함 길이 (문자열 뒤에 공백 포함)
# print("%0.4f" % 3.422134) #앞의 0은 자리수를 의미, .4는 소수점 4번째 자리까지 표현
# print("%10.4f" % 3.422134) #10은 자리수를 의미하므로 소수점 4번째 자리까지 표현 후 남는 자리만큼 앞에 공백이 생김

"""
%s => 문자열
%c => 문자 1개
%d => 정수
%f => 실수
%o => 8진수
%x => 16진수
%% => 리터럴 (문자 % 자체)
"""

#실습
#이름 :
#나이 :
#취미 :
#주소 :
#각각 변수에 넣고 f-string방식으로 출력
#ex) 제 이름은 ***이고 나이는 **살 입니다. 제 취미는 ***이고, 주소는 ***입니다.

name = input("이름 : ")
age = input("나이 : ")
hobby = input("취미 : ")
adress = input("주소 : ")
print(f"제 이름은 {name}이고, 나이는 {age}살 입니다.\n제 취미는 {hobby}이고, 주소는 {adress}입니다.")


