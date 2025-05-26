import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 로드
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
data = pd.read_csv(url)

# 앱 타이틀
st.title('당뇨병 진단 데이터 시각화')

# 데이터 프레임 표시
st.write("데이터 샘플:", data.head())

# 나이, BMI, 당뇨병 여부를 시각화
fig = px.scatter(data_frame=data, 
                 x="Age", 
                 y="BMI", 
                 color="Outcome", 
                 title="Age vs BMI by Diabetes Outcome",
                 labels={"Age": "나이", "BMI": "체질량지수(BMI)", "Outcome": "당뇨병 여부"})

# 시각화 출력
st.plotly_chart(fig)

# 예시: 데이터 통계 정보
st.subheader("데이터 통계 정보")
st.write(data.describe())
