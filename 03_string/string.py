#문자열의 인덱싱
# a = "Life is too short, You need Python"
# print(a[3])
# print(a[-1])
#
# b = a[0] + a[1] + a[2] + a[3]
# print(b)

#실습
#단어를 입력 받고 변수에 선언한 다음 첫번째 글자와 마지막 글자를 출력하시오

# name = input("이름 : ")
# print("사용자 이름 : " + name)
# print(name[0] + name[-1])

# word = input("단어를 입력하세요 : ")
# print("첫번째 글자 -", word[0])
# print("마지막 글자 -", word[-1])

#슬라이싱
# print(a[0:4]) #Life
# print(a[5:7]) #is / 끝 번호는 자기 자신을 포함하지 않는다
# print(a[19:]) #끝번호 생략의 경우 끝까지
# print(a[:17]) #시작번호 생략의 경우 처음부터
# print(a[19:-7])
# print(a[::2])
# print(a[::-1]) #문자열 뒤집기

#실습
# date = "20250702Sunny"
#년도 출력
#월일 출력
#날씨 출력

# print("년도 :", date[:4])
# print("월일 :", date[4:8])
# print("날씨 :", date[-5:])

#각종 문자열 함수
a = "Life is too short, You need Python"
print(len(a)) #문자열의 길이
print(a.count("t")) #특정 문자가 몇 개 있는지
print(a.index("t")) #특정 문자의 인덱스 찾기
print(a.index("t", 10, 18)) #특정 문자, 시작 인덱스, 끝 인덱스로 구간을 설정
print(a.find("z")) #인덱스와 마찬가지로 구간 설정 가능

"""
index, find의 차이점
index는 해당 문자가 없으면 오류를 발생
find는 해당 문자가 없으면 -1을 반환
"""

print(",".join(a)) #문자 합치기 / 문자 사이에 특정 문자를 곁들여서
print(a.upper()) #모두 대문자로 변경
print(a.lower()) #모두 소문자로 변경
print(a[0].isupper()) #대문자 여부 / boolean(is~) => True / False 로 답이 나옴
print(a[2].islower()) #소문자 여부

b = "      hi        "
print(b.lstrip()) #왼쪽 공백 제거
print(b.rstrip()) #오른쪽 공백 제거
print(b.strip()) #양쪽 공백 제거
print(a.replace("short", "long")) #대체 함수 / old => new (모두 바꾸기 느낌쓰)
print(a.replace(" ", "")) #(공백없애기)
print(a.split()) #값을 아무것도 넣지 않으면 공백, 탭, 엔터 기준으로 나눔
c = "a:b:c:d"
print(c.split(":"))

#실습
#이메일을 입력받아서 변수에 담기
#해당 이메일에서 아이디만 추출해서 출력

email = input("이메일 : ")
# print("아이디 :", email.replace("@naver.com", ""))
print("아이디 :", email[:email.index("@")]) #처음부터 email 인덱스 @ 앞까지
print("아이디 :", email.split("@")[0]) #@를 기준으로 나누는데 그중에 [0]번째 인덱스 값만