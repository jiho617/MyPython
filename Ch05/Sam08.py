year = int(input("연도를 입력하세요"))

if (year % 4 ==0 and year % 100 !=00) or year % 400 == 0 :
           print("입력한", year, "는 윤년입니다.")

else:
           print("윤년이 아닙니다.")
