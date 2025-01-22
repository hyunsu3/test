# value=int(input("숫자를 넣어보세요!"))

# if (value>3):
#     print('3보다 크다')
# else :
#     print("3과 같거나 작다")



input_txt=input("input your MBTI!").upper()

if (input_txt=="INFJ"):
    print('저랑 같군요')
elif (input_txt=="ISTJ"):
    print('저희 남편과 같군요')
else :
    print(f"{input_txt}이시군요!")