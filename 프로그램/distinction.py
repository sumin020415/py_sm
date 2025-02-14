import requests as req
import sys

# 인자 받기
args = sys.argv[1:]

def distinction(*args):
    even = []
    odd = []
    for l in args:
        num = int(l)  # 문자열을 정수로 변환
        if num % 2 == 0:
            even.append(num)
        else: 
            odd.append(num)
    result = even, odd # *들여쓰기 주의*
    return result

print(distinction(*args))