import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="나의 첫 스트림릿 앱",
    page_icon="🚀",
    layout="centered"
)

# 2. 메인 타이틀 및 설명
st.title("🚀 나의 첫 Streamlit 웹 앱")
st.write("파이썬 코드 몇 줄로 손쉽게 반응형 웹 화면을 만들 수 있습니다.")

st.divider()  # 구분선

# 3. 사이드바 구성
st.sidebar.header("⚙️ 사용자 프로필")
user_name = st.sidebar.text_input("이름을 입력하세요", value="홍길동")
job = st.sidebar.selectbox("직업을 선택하세요", ["학생", "개발자", "기획자", "기타"])

# 4. 메인 화면 - 사용자 입력 요소
st.header("1. 입력 테스트")

# 슬라이더
age = st.slider("나이를 선택하세요", min_value=1, max_value=100, value=20)

# 버튼 클릭 이벤트
if st.button("반갑게 인사하기"):
    st.success(f"안녕하세요, **{user_name}**님! ({job}, {age}세)")

st.divider()

# 5. 메인 화면 - 텍스트 입력 및 출력
st.header("2. 간단한 메모장")
user_memo = st.text_area("오늘의 메모를 작성해보세요:")

if user_memo:
    st.info(f"**작성한 내용:** {user_memo}")