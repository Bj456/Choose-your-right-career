import streamlit as st
import pandas as pd

# CSV लोड करें
@st.cache_data
def load_data():
    df = pd.read_csv("career_dataset_hindi.csv", header=0)  # Ensure the first row is treated as header
    df.columns = df.columns.str.strip()   # 🟢 कॉलम हेडर से extra spaces हटाओ
    return df

df = load_data()

# Debugging के लिए कॉलम लिस्ट दिखाएँ
st.write("📂 CSV Columns:", df.columns.tolist())

# --- Streamlit App UI ---
st.set_page_config(page_title="Career Guide App", layout="wide")

st.title("🎓 करियर गाइड ऐप (भारत)")
st.write("👉 इस ऐप की मदद से आप 10वीं, 12वीं और ग्रेजुएशन के बाद उपलब्ध करियर विकल्प देख सकते हैं।")

# Level Filter
level_options = df["Level"].unique()
selected_level = st.selectbox("📌 कक्षा चुनें:", sorted(level_options))

# Interest Filter
interest_options = df[df["Level"] == selected_level]["Interest"].unique()
selected_interest = st.selectbox("🎯 रूचि का क्षेत्र चुनें:", sorted(interest_options))

# Filter Data
filtered_df = df[(df["Level"] == selected_level) & (df["Interest"] == selected_interest)]

# Display Results
if not filtered_df.empty:
    for idx, row in filtered_df.iterrows():
        with st.container():
            st.subheader(f"📘 {row['Course_Name']}")
            st.write(f"**करियर विकल्प:** {row['Career_Option']}")
            st.write(f"**विवरण:** {row['Description']}")
            st.write(f"**पात्रता (Eligibility):** {row['Eligibility']}")
            st.write(f"**प्रवेश परीक्षा (Entrance Exam):** {row['Entrance_Exam']}")
            st.write(f"**प्रवेश माह (Admission Month):** {row['Admission_Month']}")
            st.write(f"**संस्थान / विश्वविद्यालय:** {row['Universities']}")
            if pd.notna(row['Application_Link']) and row['Application_Link'] != "N/A":
                st.markdown(f"[🔗 आवेदन / वेबसाइट देखें]({row['Application_Link']})")
            st.progress(int(row['Match_Percentage']))
            st.divider()
else:
    st.warning("❌ इस श्रेणी में कोई डेटा उपलब्ध नहीं है।")
