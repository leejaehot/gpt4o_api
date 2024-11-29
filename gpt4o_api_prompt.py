from openai import OpenAI
import os
import base64

# tjkim 키
# openai_api_key = ''

# jclee 키
openai_api_key = ''


client = OpenAI(
  api_key=openai_api_key,  # this is also the default, it can be omitted
)


""" 글로벌 변수 설정 """
ENGINE = 'gpt-4o'
CORRECT_ANSWER = '52' # 정답설정
ANSWER_TOKEN = 'Answer: ' # 답을 나타내는 토큰
CODE_START_TOKEN = "# CODE START" # 코드 시작을 알리는 토큰
CODE_END_TOKEN = "# CODE END" # 코드 종료를 알리는 토큰
MAX_TOKENS = 4096 # 최대 토큰 수 설정
# ENCODER = tiktoken.encoding_for_model(ENGINE) # 모델에 맞는 토큰 인코딩 설정


# 로컬 이미지 파일을 Base64로 인코딩
with open("/home/jclee/workspace/src/gpt4o_api/medicine_image.jpeg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# Helper function to interact with GPT-4
def ask_gpt(prompt):
    
    response = client.chat.completions.create(
        model=ENGINE,
        messages=[
            {
                "role": "system", "content": "넌 지금부터 한국어로 대답해야 해. 넌 약사야. Let's think step by step."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64, {base64_image}",
                        }
                    },
                ],
            },
        ],
        max_tokens=MAX_TOKENS,
        temperature=0.6,
    )
    
    # breakpoint()
    return response.choices[0].message.content

# Initial conversation
# prompt_list = [
#     "이미지의 좌상단부터, 보이는 약마다 약 위에 순서대로 번호를 매겨서 우하단의 약까지 번호가 다 매겨지게 해봐.",
#     # "스트렙실 놓쳤어. 다시.",
#     "나 팔이 찢겨서 피가 철철 나. 이 상황에 필요한 약을 번호로 불러줘. \
#         다음과 같은 예시로 설명해. \
#         1. **물체1**: 행동 1. (사진의 중앙 상단) \
#         2. **물체2**: 행동 2. (사진의 우측 하단) \
#         3. **물체3**: 행동 3. (사진의 좌측 중앙) \
#         (여기엔 적절한 행동 순서로 설명해줘).",
#     "이미지에서 좌상단부터 우상단까지 번호를 매겼던 것을 떠올려. 이젠 너가 제시한 물체에 해당하는 번호들을 ex) {1,2,5 ..}, 이런 형식으로 내뱉어줘.",
# ]

prompt_list = [
    "이미지의 좌상단부터, 보이는 약마다 약 위에 순서대로 번호를 매겨서 우하단의 약까지 번호가 다 매겨지게 해봐.",
    # "스트렙실 놓쳤어. 다시.",
    "나 팔이 찢겨서 피가 철철 나. 이 상황에 필요한 약을 번호로 불러줘. \
        다음과 같은 예시로 설명해. \
        <예시 설명> \
        1. **물체1**: 행동 1. (사진 내의 위치 bbox좌표값) \
        2. **물체2**: 행동 2. (사진 내의 위치 bbox좌표값) \
        3. **물체3**: 행동 3. (사진 내의 위치 bbox좌표값) \
        4. **물체4**: 행동 4. (사진 내의 위치 bbox좌표값) \
        ...\
        (사진 내의 위치는 ex: [0.15, 0.25, 0.45, 0.35]의 [x_min_norm, y_min_norm, x_max_norm, y_max_norm] 형태로 표현.) \
        물체에 따른 논리적인 행동 순서 설명.",
    # "이미지의 좌상단부터 우하단까지, 보이는 약마다 약 위에 순서대로 번호를 매겼었잖아?\
    "상황에 필요했던 물체를 이미지에서 할당되었던 번호와 결부지어서 object = {1,2,5,...}의 dict 형식으로 output을 줘. 즉 grouding 해줘.",
    
    # "이미지에서 상황별로 필요할 수 있는 물품들을 번호와 결부지어 리스트로 나타내면 다음과 같습니다:\
    #     ```python\
    #     objects = {\
    #         '물집 보호': [10, 11],  # 메디터치, 밴드\
    #         '진통제': [2],  # 타이레놀\
    #         '소독': [5, 9],  # 과산화수소수, 알코올 패드\
    #         '근육통': [13],  # 아렉스\
    #         '감기': [1, 3],  # 투즐콜드, 타이레놀\
    #         '가려움 완화': [6],  # 세이프론\
    #         '입안염증 완화': [4],  # 스트렙실\
    #         '상처 치료': [11, 12],  # 밴드, 연고\
    #     }\
    #     ```\
    # 각 번호는 이미지를 바탕으로 한 물품을 가리킵니다."\
    
    
]



# Simulating the conversation
for i, prompt in enumerate(prompt_list):
    print(f"User Prompt {i+1}: {prompt}")
    response = ask_gpt(prompt)
    print(f"GPT Response {i+1}:\n{response}\n")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    
# output  
# {
#   "id": "chatcmpl-123",
#   "object": "chat.completion",
#   "created": 1677652288,
#   "model": "gpt-4o-mini",
#   "system_fingerprint": "fp_44709d6fcb",
#   "choices": [{
#     "index": 0,
#     "message": {
#       "role": "assistant",
#       "content": "\n\nThis image shows a wooden boardwalk extending through a lush green marshland.",
#     },
#     "logprobs": null,
#     "finish_reason": "stop"
#   }],
#   "usage": {
#     "prompt_tokens": 9,
#     "completion_tokens": 12,
#     "total_tokens": 21,
#     "completion_tokens_details": {
#       "reasoning_tokens": 0,
#       "accepted_prediction_tokens": 0,
#       "rejected_prediction_tokens": 0
#     }
#   }
# }
