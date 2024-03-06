# 중복된 숫자를 입력하면 'strkie' 숫자와 'ball'숫자가 중복 반영됨

import random
number = []

while len(number)<4 :
    number_list = str(random.randint(1,9))
    if number_list not in number :
        number.append(number_list)

strike = 0
ball = 0
count = 0

print('------------------')
print('베이스볼 게임 시작!')
print('------------------')

while True :
    answer = input('4자리 숫자를 적어주세요 ')
    answer = list(answer)

    if answer == number :
        count = count + 1
        print('%d번만에 정답입니다!' % count)
        break
    else :
        strike = 0
        ball = 0
        for i in range(4) :
            for j in range(4) :
                if number[i] == answer[j] :
                    if i == j :
                        strike += 1
                    else :
                        ball += 1
                
        count = count + 1
        print('%d스트라이크 %d볼 %d시도' % (strike, ball, count))