#반복문 (for)
"""
for 변수 in 반복할 대상:
    반복할 코드
"""
#리스트 순회
fruits = ["사과", "바나나", "딸기", "포도"] #fruits = 전역변수 (for문 바깥에서 선언)

for fruit in fruits: #fruit = 지역변수 (for문 안에서 선언) > 이 변수는 이 코드 블록 내에서만 사용 가능
    print(fruit)

#딕셔너리 순회
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
for key in scores: #키를 빼와서 변수에 할당
    print(key,"의 점수는", scores[key]) #대괄호에 [key]를 넣으면 값을 반환함

#튜플 순회
a_tuple = ("안녕", "하세요", "반갑습니다")
for b in a_tuple:
    print(b)

#세트 순회
a_set = {"사과", "바나나", "체리", "딸기", "오렌지"}
for c in a_set:
    print(c)

#세트 정렬 추가 설명
numbers = {3, 1, 4, 1, 5, 9, 2}
sorted_numbers = sorted(numbers) #솔티드 함수를 적용하게 되면 리스트 타입으로 바뀜
print(sorted_numbers)
print(type(sorted_numbers))