import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# CONFIG
st.set_page_config(
    page_title="Spotify Music Analysis Dashboard",
    layout="wide"
)

# LOAD DATA

@st.cache_data
def load_data():
    return pd.read_csv("SpotifyFeatures.csv")

df = load_data()

# SIDEBAR

st.sidebar.title("Spotify Data Analysis")
section = st.sidebar.radio(
    "Chọn nội dung phân tích",
    [
        "Tổng quan dữ liệu",
        "Phân tích đặc trưng âm thanh",
        "Bức tranh thể loại âm nhạc",
        "Phân cụm âm nhạc",
        "Dự đoán mức độ phổ biến"
    ]
)

# 1. OVERVIEW

if section == "Tổng quan dữ liệu":
    st.title("Tổng quan bộ dữ liệu Spotify")

    st.markdown("""
    Dashboard này minh họa quá trình **phân tích dữ liệu âm nhạc Spotify**
    từ khám phá dữ liệu đến mô hình phân tích nâng cao.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Số bài hát", f"{df.shape[0]:,}")
    col2.metric("Số thuộc tính", df.shape[1])
    col3.metric("Số thể loại", df['genre'].nunique())

    st.subheader("Xem mẫu dữ liệu")
    st.dataframe(df.head())

# 2. AUDIO FEATURES

elif section == "Phân tích đặc trưng âm thanh":
    st.title("🎚 Phân tích đặc trưng âm thanh")

    features = [
        "danceability", "energy", "valence",
        "acousticness", "instrumentalness",
        "loudness", "tempo"
    ]

    feature = st.selectbox("Chọn thuộc tính", features)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df[feature], bins=40)
    ax.set_title(f"Phân phối {feature}")
    ax.set_xlabel(feature)
    ax.set_ylabel("Số lượng bài hát")

    st.pyplot(fig)

    st.markdown("""
    Biểu đồ cho thấy cách các bài hát phân bố theo từng đặc trưng âm thanh,
    từ đó phản ánh **xu hướng âm nhạc phổ biến hiện nay**.
    """)

# 3. GENRE ANALYSIS

elif section == "Bức tranh thể loại âm nhạc":
    st.title("🎼 Bức tranh thể loại âm nhạc trên Spotify")

    top_genres = df['genre'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(8, 4))
    top_genres.plot(kind="bar", ax=ax)
    ax.set_title("Top 10 thể loại phổ biến nhất")
    ax.set_ylabel("Số lượng bài hát")

    st.pyplot(fig)

    st.markdown("""
    Các thể loại như **Pop, Rock, Hip-Hop** chiếm ưu thế rõ rệt,
    phản ánh cấu trúc thị trường âm nhạc trên nền tảng Spotify.
    """)

# 4. CLUSTERING

elif section == "Phân cụm âm nhạc":
    st.title("Phân cụm các nhóm âm nhạc tự nhiên")

    features_cluster = [
        "danceability", "energy", "valence",
        "acousticness", "instrumentalness", "loudness"
    ]

    X = df[features_cluster]
    X_scaled = StandardScaler().fit_transform(X)

    k = st.slider("Chọn số cụm (K)", 2, 8, 5)

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)

    df["cluster"] = clusters

    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(
        df["energy"],
        df["danceability"],
        c=clusters,
        s=5
    )
    ax.set_xlabel("Energy")
    ax.set_ylabel("Danceability")
    ax.set_title("Phân cụm bài hát (Energy vs Danceability)")

    st.pyplot(fig)

    st.markdown("""
    Các cụm phản ánh **những kiểu âm thanh phổ biến**
    (sôi động – thư giãn – không lời),
    dù ranh giới giữa các nhóm không hoàn toàn tách biệt.
    """)

# 5. CLASSIFICATION

elif section == "Dự đoán mức độ phổ biến":
    st.title("📈 Dự đoán mức độ phổ biến của bài hát")

    threshold = 60
    df["is_popular"] = (df["popularity"] >= threshold).astype(int)

    features_cls = [
        "danceability", "energy", "valence",
        "loudness", "acousticness", "instrumentalness"
    ]

    X = df[features_cls]
    y = df["is_popular"]

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    coef = pd.Series(model.coef_[0], index=features_cls)

    fig, ax = plt.subplots(figsize=(8, 4))
    coef.sort_values().plot(kind="barh", ax=ax)
    ax.set_title("Ảnh hưởng của các thuộc tính đến độ phổ biến")

    st.pyplot(fig)

    st.markdown("""
    Các thuộc tính như **Loudness, Energy, Danceability**
    có ảnh hưởng tích cực đến khả năng trở nên phổ biến,
    trong khi **Instrumentalness** làm giảm xác suất trở thành hit.
    """)
