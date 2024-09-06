import streamlit as st
from openai import OpenAI

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # OpenAI 클라이언트 초기화
    client = OpenAI(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("인공지능 상장 생성기")

    # 사용자 입력 받기
    user_input = st.text_area("상장을 생성할 내용을 입력하세요", 
                              "예: 민수는 체육대회에서 친구들과 함께 열심히 뛰면서 서로 응원하고 도와주었어요.")

    if st.button("상장 생성"):
        # OpenAI 클라이언트를 사용하여 상장 생성
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "초등학생에게 평소 생활을 반영하는 상장을 수여하고자 합니다. 입력의 내용을 참고하여 재치있는 상장명과 문구를 생성해주세요."},
                {"role": "user", "content": f"input: {user_input}"}
            ]
        )
        
        # 결과 출력
        st.subheader("생성된 상장")
        st.write(response.choices[0].message.content)
else:
    st.warning("API 키를 사이드바에 입력하세요.")
