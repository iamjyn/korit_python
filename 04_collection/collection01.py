#List - 요소들을 [ ] 대괄호로 감싼 형태
fruits = ["apple", "banana", "cherry"] #문자열 리스트
numbers = [1, 2, 3, 4, 5] #숫자 리스트
bools = [True, True, False, False] #불리언 리스트
mixed_list = ["안녕하세요", 42, 3.14, "pyton", True] #여러 타입 혼합 사용가능

#요소 접근 (인덱스)
print(fruits[0])
print(fruits[0][0])
print(numbers[-1])

#요소 변경
fruits[1] = "blueberry"
print(fruits)

#요소 추가
fruits.append("grape") #마지막 요소 뒤에 추가됨
fruits.insert(1, "mango") #특정 인덱스 자리에 추가됨
print(fruits)

#리스트 더하기
list1 = ["A", "B", "C"]
list2 = ["D", "E"]
print(list1 + list2)

#리스트 곱하기
print(list1 * 3)

#리스트에 여러 요소 추가
list1.extend(list2)
print(list1)

#요소 삭제
fruits.remove("cherry") #특정 값을 삭제
fruits.pop() #특정 인덱스를 삭제 / 인덱스 생략시 마지막 요소 삭제
del fruits[2] #특정 인덱스를 삭제
print(fruits)

#리스트 길이
print(len(fruits))

#리스트 슬라이싱
print(numbers[1:4])
print(numbers[::-1])

#리스트 정렬 (원본에 영향감)
numbers.sort() #기본적으로 오름차순 정렬
print(numbers)
numbers.sort(reverse=True) #내림차순 정렬
print(numbers)
list1.sort(reverse=True)
print(list1)
kor = ["가", "나", "다"]
kor.sort(reverse=True) #한글도 가능함
print(kor)

numers2 = sorted(numbers) #원본 변수에는 영향X, 새롭게 변수에 값을 할당

#리스트 안에 요소 존재 체크
print("apple" in fruits)
print("apple" not in fruits)

#리스트 요소들 이어 붙이기
result = "-".join(list1)
print(result)