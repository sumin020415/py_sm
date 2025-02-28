import sys

def find_words(sentence):
    if not sentence.strip():
        return []  # 빈 문자열일 경우 빈 리스트 반환
    words = sentence.split()
    max_len = max(len(word) for word in words)
    long = [word for word in words if len(word) == max_len]
    return long

sentence = input("문장을 입력하세요: ")
longest_words = find_words(sentence)

if longest_words:
    print("문장 중 가장 긴 단어는:", ", ".join(longest_words))
else:
    print("입력된 문장이 없습니다.")
