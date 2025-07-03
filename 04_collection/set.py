#세트 - 중복 삭제 되고, 순서가 실행할 때 마다 바뀜
fruits = {"사과", "바나나", "오렌지", "바나나"}
print(fruits)
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

empty_set = {} #비어 있는 딕셔너리 (세트가 아님 세트는 set() 적어줘야함
empty_dict = {}

empty_set = set() #비어 있는 세트

#세트 - 요소 추가
s = {1, 2, 3}
s.add(4) #한 개만 추가할 때
print(s)

s.update([5, 6, 7]) #여러 개를 한번에 추가할 떄
print(s)

#세트 - 요소 삭제
s.remove(3) #존재 하지 않는 값 제거 시 오류 발생
s.discard(10) #존재 하지 않는 값 제거 시 오류 없음
print(s)

s.clear() #전체 삭제
print(s)

#세트 - 합집합 / (중복제거됨)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A.union(B))

#세트 - 교집합
print(A & B)
print(A.intersection(B))

#세트 - 차집합
print(A - B)
print(A.difference(B))
print(B.difference(A))

#실습
python_class = {"철수", "영희", "민수", "지수"}
java_class = {"영희", "민수", "지훈", "길동"}

#파이썬과 자바 수업을 둘 다 듣는 사람
print("파이썬, 자바 :", python_class & java_class)
print("파이썬, 자바 :", python_class.intersection(java_class))

#파이썬만 듣는 사람
print("파이썬 :", python_class - java_class)
print("파이썬 :", python_class.difference(java_class))

#자바만 듣는 사람
print("자바 :", java_class - python_class)
print("자바 :", java_class.difference(python_class))