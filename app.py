import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 제목
st.title("📦 배송 데이터 시각화")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("Delivery.csv")
    return df

df = load_data()
st.subheader("데이터 미리보기")
st.dataframe(df)

# 컬럼 목록 보여주기
numeric_columns = df.select_dtypes(include='number').columns.tolist()
categorical_columns = df.select_dtypes(include='object').columns.tolist()

# 사용자 선택: 시각화 타입
st.sidebar.header("시각화 옵션")
plot_type = st.sidebar.selectbox("시각화 종류", ["히스토그램", "산점도", "박스플롯"])

if plot_type == "히스토그램":
    column = st.sidebar.selectbox("히스토그램 대상 열", numeric_columns)
    fig = px.histogram(df, x=column, nbins=30, title=f"{column} 분포")
    st.plotly_chart(fig)

elif plot_type == "산점도":
    x_col = st.sidebar.selectbox("X축", numeric_columns)
    y_col = st.sidebar.selectbox("Y축", numeric_columns, index=1)
    fig = px.scatter(df, x=x_col, y=y_col, color=df[categorical_columns[0]], title=f"{x_col} vs {y_col}")
    st.plotly_chart(fig)

elif plot_type == "박스플롯":
    y_col = st.sidebar.selectbox("Y축", numeric_columns)
    x_col = st.sidebar.selectbox("카테고리 기준 열", categorical_columns)
    fig = px.box(df, x=x_col, y=y_col, title=f"{x_col} 별 {y_col} 분포")
    st.plotly_chart(fig)
