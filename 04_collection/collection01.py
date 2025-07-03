#List - 요소(element)들을 [ ] 대괄호로 감싼 형태
# fruits = ["apple", "banana", "cherry"] #문자열 리스트
# numbers = [1, 2, 3, 4, 5] #숫자 리스트
# bools = [True, True, False, False] #불리언 리스트
# mixed_list = ["안녕하세요", 42, 3.14, "pyton", True] #여러 타입 혼합 사용가능

#리스트 - 요소 접근 (인덱스)
# print(fruits[0])
# print(fruits[0][0]) #fruits 리스트에서 0번째 요소의 0번째 인덱스
# print(numbers[-1])

#리스트 - 요소 변경
# fruits[1] = "blueberry"
# print(fruits)

#리스트 - 요소 추가
# fruits.append("grape") #마지막 요소 뒤에 추가됨
# fruits.insert(1, "mango") #특정 인덱스 자리에 추가됨
# print(fruits)

#리스트 더하기
# list1 = ["A", "B", "C"]
# list2 = ["D", "E"]
# print(list1 + list2)

#리스트 곱하기 / =반복
# print(list1 * 3)

#리스트에 여러 요소 추가
# list1.extend(list2)
# print(list1)

#리스트 - 요소 삭제
# fruits.remove("cherry") #특정 값을 삭제
# fruits.pop() #특정 인덱스를 삭제 / 인덱스 생략시 마지막 요소 삭제
# del fruits[2] #특정 인덱스를 삭제
# print(fruits)

#리스트 길이
# print(len(fruits))

#리스트 슬라이싱
# print(numbers[1:4])
# print(numbers[::-1])

#리스트 정렬 (원본에 영향감)
# numbers.sort() #기본적으로 오름차순 정렬
# print(numbers)
# numbers.sort(reverse=True) #내림차순 정렬
# print(numbers)
# list1.sort(reverse=True)
# print(list1)
# kor = ["가", "나", "다"]
# kor.sort(reverse=True) #한글도 정렬 가능함
# print(kor)

# numbers2 = sorted(numbers) #원본 변수에는 영향X, 새롭게 변수에 값을 할당

#리스트 안에 요소 존재 체크
# print("apple" in fruits)
# print("apple" not in fruits)

#리스트 요소들 이어 붙이기
# result = "-".join(list1)
# print(result)

#리스트 실습
#3개의 상품명을 입력 받아서 cart에 추가
#최종적으로 cart를 출력

cart = []

# product1 = input("상품명 입력 : ")
# cart.append(product1)
#
# product2 = input("상품명 입력 : ")
# cart.append(product2)
#
# product3 = input("상품명 입력 : ")
# cart.append(product3)
# print(cart)

# cart.append(input("추가할 상품 : "))
# cart.append(input("추가할 상품 : "))
# cart.append(input("추가할 상품 : "))
# print(cart)

#튜플
colors = ("red", "blue", "green")
numbers = (1, 2, 3, 5, 9)
mixed = ("pink", 1, True)
single_tuple = ("hello",) #요소가 1개일 때는 꼭 ,(콤마)를 붙여야 함
alphabet = ("a", "a", "a", "b", "c", "c")

#튜플 - 요소 접근
print(colors[1])

#튜플 - 요소 변경 불가
# colors[1] = "yellow"

#튜플 - 슬라이싱
print(colors[:2])
print(colors[::-1])

#튜플 - count
print(alphabet.count("a"))

#튜플 - index
print(alphabet.index("b"))

#튜플 - 언패킹
a, b, c = colors #각각의 변수에 그대로 넣는 것 (변수와 튜플 갯수가 같아야함)
print(a, b, c)