import os
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="고등학생용 5등급제 ➔ 9등급제 성적 변환기",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        /* Streamlit 기본 여백 제거 및 뷰포트 맞춤 */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 100%;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 현재 파일(app.py) 위치를 기준으로 htmls/index.html 경로 설정
BASE_DIR = Path(__file__).resolve().parent
HTML_FILE_PATH = BASE_DIR / "htmls" / "index.html"

if HTML_FILE_PATH.exists():
    try:
        # UTF-8 인코딩으로 HTML 파일 읽기
        with open(HTML_FILE_PATH, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Streamlit HTML 컴포넌트로 화면에 전체 출력
        components.html(html_content, height=1000, scrolling=True)
    except Exception as e:
        st.error(f"⚠️ HTML 파일을 읽는 도중 오류가 발생했습니다: {e}")
else:
    # 파일이 존재하지 않을 때 출력할 사용자 친화적 메시지
    st.warning("⚠️ `htmls/index.html` 파일을 찾을 수 없습니다.")
    st.info("""
    **프로젝트 폴더 구조를 확인해 주세요:**
    ```
    내-웹앱/
    ├── app.py
    ├── requirements.txt
    └── htmls/
        └── index.html
    ```
    `app.py`가 위치한 디렉토리 안에 `htmls` 폴더를 생성하고, 그 안에 `index.html` 파일을 위치시켜 주세요.
    """)
