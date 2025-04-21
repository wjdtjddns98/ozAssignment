#True = 양수(+), False = 음수(-)
#1 = +, 2 = -
정수 = [10, 5, 8] #list
부호 = ["Plus", "Minus", "Plus"]

합 = 0 #0 이라는 시작점을 만들어줌 ( 변수 초기화 )


#zip이라는 기능이 있음(내장함수)
#zip은 두 개의 리스트를 묶어줌
#정수의 리스트 [10, 5, 8], 부호의 리스트[True, False, True] 묶어줌
#10 = True, 5 = False, 8 = True
for k, v in zip(부호, 정수):
    if k == "Plus": #True일때
        합 += v
    else: #False
        합 -= v

print(합)


