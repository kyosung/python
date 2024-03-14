import datetime

'''
datetime.strftime 쓰임세
%y : 두 자리 수의 연도 ex) 19, 20, 21
%Y : 네 자리 수의 연도 ex) 2019, 2020, 2021
%m : 0을 채운 두 자리 수의 월 ex) 01, 02 ...  11 ,12
%d : 0을 채운 두 자리 수의 일 ex) 01, 02 ...  30, 31
%I : 0을 채운 12시간제의 시간 ex) 01, 02 … 12
%H : 0을 채운 24시간제의 시간 ex) 00, 01 … 23
%M : 0을 채운 두 자리 수의 분 ex) 00, 01 ... 58, 59
%S : 0을 채운 두 자리 수의 초 ex) 00, 01 ... 58, 59
'''

now_time = datetime.datetime.now()
now_time_string = now_time.strftime('%Y-%m-%d\n%H:%M:%S')

print(now_time)
print(now_time_string)