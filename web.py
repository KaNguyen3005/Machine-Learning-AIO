import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from service import calculate_average, percentage_distribution

if __name__ == "__main__":
    st.title("Phân tích dữ liệu điểm số học sinh")
    uploaded_file = st.file_uploader("Chọn file Excel (có cột ‘Điểm số’)", type=["xlsx"])
    df = pd.read_excel(uploaded_file)
    scores = df["Điểm số"].dropna().astype(float).tolist()
    st.write("Tổng số học sinh:", len(scores))
    st.write("Điểm trung bình:", round(calculate_average(scores), 2))
    print(scores)
    dist = percentage_distribution(scores)
    print(percentage_distribution(scores))
    labels = list(dist.keys())
    values = list(dist.values())
    fig, ax = plt.subplots(figsize = (3,3))
    ax.pie(values, labels = labels, autopct = "%1.1f%%", startangle = 90)
    ax.axis("equal")
    st.pyplot(fig)

    st.pyplot(fig, use_container_width=False)
    st.markdown("Biểu đồ phân bố điểm số.")