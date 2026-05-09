import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="Art Gallery Dashboard",
    page_icon="🎨",
    layout="wide"
)

# 제목
st.title("🎨 Art Gallery Dashboard")
st.write("Explore famous artworks and their values.")

# 데이터 만들기
data = {
    "Artwork": [
        "Mona Lisa",
        "Starry Night",
        "The Scream",
        "The Kiss",
        "Girl with a Pearl Earring"
    ],
    "Artist": [
        "Leonardo da Vinci",
        "Vincent van Gogh",
        "Edvard Munch",
        "Gustav Klimt",
        "Johannes Vermeer"
    ],
    "Year": [1503, 1889, 1893, 1908, 1665],
    "Price": [860, 100, 120, 150, 80],
    "Category": [
        "Portrait",
        "Landscape",
        "Expressionism",
        "Symbolism",
        "Portrait"
    ]
}

df = pd.DataFrame(data)

# 사이드바 필터
st.sidebar.header("Filter")
selected_category = st.sidebar.selectbox(
    "Choose Category",
    ["All"] + list(df["Category"].unique())
)

if selected_category != "All":
    df = df[df["Category"] == selected_category]

# 요약 카드
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Artworks", len(df))

with col2:
    st.metric("Average Price", f"${df['Price'].mean():.1f}M")

with col3:
    st.metric("Oldest Artwork", df["Year"].min())

# 데이터 표
st.subheader("Artwork Table")
st.dataframe(df)

# 막대 그래프
st.subheader("Artwork Price Chart")
fig = px.bar(
    df,
    x="Artwork",
    y="Price",
    color="Category"
)

st.plotly_chart(fig, use_container_width=True)

# 연도별 그래프
st.subheader("Artwork Timeline")
fig2 = px.scatter(
    df,
    x="Year",
    y="Price",
    size="Price",
    color="Artist",
    hover_name="Artwork"
)

st.plotly_chart(fig2, use_container_width=True)
