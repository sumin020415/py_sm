# 모듈 만들기
def add(a,b):
    return a + b
def sub(a,b):
    return a-b

print(add(1,4))
print(sub(4,2))
print(__name__)
if __name__ == "__main__":
    print("전 실행이 되었어요.")
else:
    print("전 모듈로 임포트 되었어요.")