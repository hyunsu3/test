# 논리형(Bool, Boolean)
print(3<2)
print(3==3)
print(3==3.0)
print(3 is 3)
print(3 is 3.0) #===


# 형 변환
a=100
b="103"
print(str(a)+b)
print(a+int(b))
print(a+float(b))


# 큰 수 (언더스코어로 표현해도 없는 것과 같게 읽음)
price = 12_345_000_000_000
price2 = 12345000000000
print(price)
print(price2)

#숫자
a=2
b=3
print(a+b)
print(a-b)
print(a*b)

#몫, 나머지
print(a/b)
print(a//b)
print(a%b)

#제곱
print(a**b)


# #문자열에서 삭제 
score = "점수:90"
print(score.removeprefix("점수:"))

city="서울 중구"
print(city.replace("서울", "서울시"))

# #공백 제거
occupation = 'developer  '
print(occupation)

occupation.strip()
print(occupation)

# #대소문자 변환
city_name = "seoul"
print(f"저는 {city_name}에 살아요")

city_name = city_name.upper()
print(f"저는 {city_name}에 살아요")

city_name = city_name.lower()
print(f"저는 {city_name}에 살아요")