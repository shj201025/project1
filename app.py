import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="첫 웹페이지",
    page_icon="👋",
    layout="centered"
)

# 배경색과 글자색 설정
st.markdown("""
<style>
.stApp {
    background-color: #0B1F4D;
    color: white;
}

h1, h2, h3, p, div {
    color: white;
}

div.stButton > button {
    background-color: #3B82F6;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    font-size: 18px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #2563EB;
}
</style>
""", unsafe_allow_html=True)

# 메인 화면
st.markdown(
    "<h1 style='text-align:center;'>👋 안녕하세요</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='text-align:center;'>😊</h2>",
    unsafe_allow_html=True
)

st.write("")

# 버튼
if st.button("나도 인사하기", use_container_width=True):
    st.balloons()          # 풍선 효과
    st.snow()              # 반짝이는 효과(추가)

    # 폭죽 효과
    st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
    <script>
    confetti({
        particleCount: 250,
        spread: 180,
        origin: { y: 0.6 }
    });
    </script>
    """, unsafe_allow_html=True)

    st.success("🎉 첫 웹페이지 제작을 축하해요! 🎉")
  
