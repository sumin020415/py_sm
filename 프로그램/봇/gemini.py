# 구글 제미나이 AI
from google import genai
def aiai(text):
    client = genai.Client(api_key="")
    response = client.models.generate_content(model="gemini-2.0-flash",contents= text + "단, 500자 이내로 알려줘. 서술형으로 친절하게 알려줘.",)
    answer = response.text
    print(answer)
    return answer

if__name__=="__main__":
    aiai("gpt에 대해 설명해줘")