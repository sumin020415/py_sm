import requests as req
import sys

# 인자 받기
args = sys.argv  

def reverse(s):
    word = ""
    for i in s:
        word = i + word
    if word == s :
        return True
    else:
        return False

s = input("단어를 입력하세요: ")
s = s.upper()
new = ""        
i = 0
for i in range(len(s)):
    if s[i] != " " and s[i] != "," and s[i] != "?":
        new = new + s[i]
result = reverse(new)
print(result)