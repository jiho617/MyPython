import random
wins = 0
lotto = str(input("복권번호를 입력하세요(0에서 99사이):"))
solution = random.randrange(0,99)
digit1 = solution // 10
digit2 = solution % 10
print("당첨번호는",solution, "입니다")
if str(digit1) in lotto:
    wins = 50
if str(digit2) in lotto:
    wins = 50
print("상금은", wins, "만원입니다") 


