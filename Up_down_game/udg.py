import random
number = random.randint(1,100)
count = 0

while True:
    answer = int(input('내가 선택한 숫자는 '))
    if answer == number:
        count = count + 1
        print(str(count)+'번 만에 정답이야')
        break
    elif answer > number:
        count = count + 1
        print('다운!')
    else :
        count = count + 1
        print('업!')
