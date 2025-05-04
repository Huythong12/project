import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import streamlit_lottie as st_lottie
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain

# ✅ Chỉ GỌI MỘT LẦN duy nhất ngay sau import
st.set_page_config(page_title="Gộp 2 WebApp", page_icon="🧡", layout="wide")

st.title("🎉 WebApp Hợp Nhất")
st.markdown("Hiển thị nội dung từ cả `codename.py` và `app.py`.")

st.subheader("📌 Phần 1: Codename")
# --- CODE TỪ codename.py ---
with st.expander("Xem chi tiết Codename", expanded=True):
    st.title("PYTHON 2 - BUSINESS IT 2 :orange_heart:")

    st.write("We are a group of business students who are interested in the economical situation in the world. Therefore, we decided to analyze a set of data about the employment fluctuation in the USA from 1978 to 2022. Through this visualization, we hope to bring a clear vision to people about how the labor market in the USA has changed over the past decades.")

    stoggle(
        "Group information",
        """
        \n 1. Dinh Ha Tu Van - 10622045
        \n 2. Bui Cam Ha Quyen - 10622023
        \n 3. Mai Hong Hanh - 10622014
        \n 4. Tran Quang Hieu - 10622088
        \n 5. Le Thi Minh Chau - 10622073
        """,
    )

    st.write("[Accessing our dataset >](https://docs.google.com/spreadsheets/d/1HbBDpeXYXhl3MQU2bZ-YZiHb1Fe2COrT/edit?usp=drive_link)")

    rain(
        emoji="🔍",
        font_size=54,
        falling_speed=5,
        animation_length="3",
    )

    colored_header(
        label="Group members introduction",
        description="Get to know about our group",
        color_name="light-blue-70",
    )

    # === Members ===
    members = [
        ("1.jpg", "Dinh Ha Tu Van (Group leader)", "10622045", "10622045@student.vgu.edu.vn", "Business Administration (BBA)", "077 6209215"),
        ("2.jpg", "Bui Cam Ha Quyen", "10622023", "10622023@student.vgu.edu.vn", "Finance & Accounting (BFA)", "090 8784370"),
        ("3.jpg", "Mai Hong Hanh", "10622014", "10622014@student.vgu.edu.vn", "Business Administration (BBA)", "039 2230636"),
        ("4.jpg", "Tran Quang Hieu", "10622088", "10622088@student.vgu.edu.vn", "Business Administration (BBA)", "096 1234567"),
        ("5.jpg", "Le Thi Minh Chau", "10622073", "10622073@student.vgu.edu.vn", "Finance & Accounting (BFA)", "093 7654321"),
    ]

    for i in range(0, len(members), 2):
        col1, col2 = st.columns(2)
        for col, (img, name, sid, email, major, phone) in zip([col1, col2], members[i:i+2]):
            with col:
                st.image(Image.open(img))
                st.subheader(f"**Full name: {name}**")
                st.write(f"Student ID: {sid}")
                st.write(f"Email: {email}")
                st.write(f"Major: {major}")
                st.write(f"Phone number: {phone}")

    # --- Contact form ---
    st.markdown("---")
    st.subheader("💬 Leave us your message!")
    st.caption("Let us know if you have any recommendations")

    contactform = """<form action="https://formsubmit.co/10622045@student.vgu.edu.vn" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email address" required>
         <textarea name="message" placeholder="What do you think?"></textarea>
         <button type="submit">Send</button>
    </form>"""

    st.markdown(contactform, unsafe_allow_html=True)

st.subheader("📌 Phần 2: App Phân Tích")
# --- CODE TỪ app.py ---
with st.expander("Xem chi tiết App", expanded=True):

    @st.cache_data
    def load_data():
        df = pd.read_excel("shopping_trends.xlsx", sheet_name="shopping_trends")
        return df

    df = load_data()

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox(
        "Choose the section:",
        [
            "🧭 Introduction - Shopping Trends",
            "📅 Purchase Frequency Analysis",
            "🛒 Item Purchased Analysis"
        ]
    )

    if app_mode == "🧭 Introduction - Shopping Trends":
        st.title("🛍️ Customer Shopping Trends")
        st.markdown("""
        ### Welcome to the Customer Shopping Trends!

        In this dashboard, we explore insights from shopping behavior data, helping businesses and analysts uncover patterns in customer purchases.

        **What you'll learn:**
        - Who buys what?
        - How frequently customers shop?
        - What are the top trending products?

        Let's dive into the world of shopping trends and consumer analytics! 🛍️📊
        """)

        st.image(
            "https://images.unsplash.com/photo-1542831371-d531d36971e6?auto=format&fit=crop&w=1600&q=80",
            caption="Shopping behavior insights",
            use_column_width=True
        )

    elif app_mode == "📅 Purchase Frequency Analysis":
        st.title("🛍️ Shopping Trends Dashboard - Frequency Analysis")
        frequency_filter = st.sidebar.selectbox("Select purchase frequency:", df["Frequency of Purchases"].unique(), index=0)
        filtered_df = df[df["Frequency of Purchases"] == frequency_filter]

        st.markdown(f"### 📌 Data for **'{frequency_filter}'** group")
        col1, col2, col3 = st.columns(3)
        col1.metric("👥 Total Customers", filtered_df.shape[0])
        col2.metric("💵 Total Revenue", f"${filtered_df['Purchase Amount (USD)'].sum():,.2f}")
        col3.metric("📈 Avg. Previous Purchases", f"{filtered_df['Previous Purchases'].mean():.2f}")

        st.markdown("### 🎨 Age Distribution Chart")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(filtered_df["Age"], bins=10, kde=True, color=sns.color_palette("plasma", 10)[4], edgecolor='black')
        ax.set_xlabel("Age")
        ax.set_ylabel("Number of Customers")
        ax.set_title("Customer Age Distribution", fontsize=14)
        st.pyplot(fig)

    elif app_mode == "🛒 Item Purchased Analysis":
        st.title("🛒 Shopping Trends Dashboard - Item Purchased Analysis")
        st.sidebar.header("Filters")

        gender_filter = st.sidebar.multiselect(
            "Select Gender:",
            options=df["Gender"].unique(),
            default=df["Gender"].unique()
        )

        age_filter = st.sidebar.slider(
            "Select Age Range:",
            min_value=int(df["Age"].min()),
            max_value=int(df["Age"].max()),
            value=(int(df["Age"].min()), int(df["Age"].max()))
        )

        df_filtered = df[
            (df["Gender"].isin(gender_filter)) &
            (df["Age"] >= age_filter[0]) &
            (df["Age"] <= age_filter[1])
        ]

        st.subheader("Top 10 Most Purchased Items")
        item_counts = df_filtered["Item Purchased"].value_counts().reset_index()
        item_counts.columns = ["Item Purchased", "Count"]

        fig = px.bar(
            item_counts.head(10),
            x="Count",
            y="Item Purchased",
            orientation='h',
            color="Count",
            color_continuous_scale="Teal",
            title="Top 10 Most Purchased Items"
        )
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Distribution of Purchased Items")
        fig2 = px.pie(
            item_counts,
            names="Item Purchased",
            values="Count",
            title="Item Purchased Distribution",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        st.plotly_chart(fig2, use_container_width=True)
