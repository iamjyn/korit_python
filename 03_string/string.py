#문자열의 인덱싱
a = "Life is too short, You need Python"
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
print(a[0:4]) #Life
print(a[5:7]) #is / 끝 번호는 자기 자신을 포함하지 않는다
print(a[19:]) #끝번호 생략의 경우 끝까지
print(a[:17]) #시작번호 생략의 경우 처음부터
print(a[19:-7])
print(a[::2])
print(a[::-1]) #문자열 뒤집기