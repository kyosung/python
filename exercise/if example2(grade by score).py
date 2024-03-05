score = int(input('시험성적을 입력하세요: '))
if score >= 80 :
    print(score,'점','A등급입니다')
elif score >=60 :
    print(score,'점','B등급입니다')
elif score >=40 :
    print(score,'점','C등급입니다')
else :
    print(score,'점','재시험입니다')