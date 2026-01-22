import streamlit as st
import datetime

# 앱 설정
st.set_page_config(page_title="인생 일기예보", page_icon="☔")

# 메인 타이틀
st.title("☔ 모두를 위한 인생 일기예보")
st.write("당신이 어떤 계절에 태어났는지, 지금 어떤 우산이 필요한지 알려드릴게요.")

# 1. 사용자 입력 받기
with st.sidebar:
    st.header("정보를 알려주세요")
    user_name = st.text_input("성함이나 닉네임", "이웃님")
    birth_date = st.date_input("생년월일", datetime.date(1990, 1, 1))
    birth_time = st.time_input("태어난 시간", datetime.time(12, 0))
    gender = st.radio("성별", ["여성", "남성"])

# 2. 결과 출력하기
st.divider()
st.subheader(f"✨ {user_name} 님을 위한 오늘의 예보")

# 똥님이 선택한 핵심 문구
st.info("### \"오늘의 날씨는 당신의 잘못이 아닙니다.\n### 그저 우산을 챙길 시간일 뿐입니다.\"")

# 3. 간단한 기질 분석 메시지 (예시 로직)
# 실제 상용화 때는 여기서 십신/운성 계산 로직이 들어갑니다.
st.success(f"#### 🌈 {user_name} 님의 기질 분석")
st.write(f"{user_name} 님은 따뜻한 포용력을 가진 분이시군요.")
st.write("지금 당신의 운 흐름은 새로운 시작을 준비하는 '봄의 길목'에 서 있습니다.")
st.write("조금 서툴러도 괜찮습니다. 당신이라는 씨앗은 이미 싹을 틔울 준비를 마쳤으니까요.")

st.divider()
st.caption("제작: 동양철학전공자 똥강")
