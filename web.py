import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import io
from PIL import Image
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
    plt.tight_layout(pad=0.1)
    st.pyplot(fig, use_container_width=False)
    st.markdown("Biểu đồ phân bố điểm số.")

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300) # Lưu với dpi cao để ảnh sắc nét
    buf.seek(0)

    st.markdown("Biểu đồ phân bố điểm số.")
    img = Image.open(buf)
    st.image(img, width=250) # Hiển thị ảnh với kích thước cố định
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, width=300) # Hiển thị biểu đồ ở cột giữa
        st.markdown("Biểu đồ phân bố điểm số.")