# lst = [1,2,3,4,5]
# print(lst)
# lst.reverse()
# print(lst)

# lst2 = [1,2,3,4,5]
# print("리스트 뒤집기 전 : ", lst2) # [5, 4, 3, 2, 1]

# lst3 = reversed(lst2)
# print("리스트 뒤집은 후 : ", lst3) # <list_reverseiterator object at 0x7f04854c2d90>

# kor = ["사과", "바나나", "오렌지"]
# eng = ["apple", "banana", "orange"]

# print(list(zip(kor, eng))) # [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # [('사과', '바나나', '오렌지'), ('apple', 'banana', 'orange')]

kor2, eng2 = zip(*mixed)
print(kor2) # ('사과', '바나나', '오렌지')
print(eng2) # ('apple', 'banana', 'orange')

import requests
import time
res = requests.get("http://naver.com")
print("응답코드 : ", res.status_code) # 200 이면 정상