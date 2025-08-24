import streamlit as st
import pandas as pd

# CSV लोड करें
@st.cache_data
def load_data():
    return pd.read_csv("career_dataset_hindi.csv")

df = load_data()

st.set_page_config(page_title="कैरियर गाइड चैटबॉट", page_icon="🎓")

st.title("🤖 कैरियर गाइड चैटबॉट")
st.write("यह चैटबॉट आपकी कक्षा और रुचि के अनुसार करियर विकल्प बताता है।")

# Step 1: कक्षा चुनें
kaksha = st.selectbox("आप किस कक्षा में हैं?", ["10", "12", "UG"])

# Step 2: रुचि चुनें
interest_options = df[df['kaksha_level'] == kaksha]['interest'].unique()
interest = st.selectbox("आपकी रुचि क्या है?", interest_options)

# Step 3: सुझाव दिखाएँ
if st.button("🔍 करियर विकल्प देखें"):
    filtered = df[(df['kaksha_level'] == kaksha) & (df['interest'] == interest)]
    
    if not filtered.empty:
        for _, row in filtered.iterrows():
            st.subheader(f"🎯 {row['career_title']} ({row['match_weight']}%)")
            st.write(f"**विवरण:** {row['career_description']}")
            st.write(f"**सुझाया गया स्ट्रीम:** {row['suggested_stream']}")
            st.write(f"**जरूरी विषय:** {row['required_subjects']}")
            st.write(f"**प्रवेश परीक्षा:** {row['entrance_exams']}")
            st.write(f"**सामान्य डिग्री:** {row['typical_degrees']}")
            st.write(f"**वैकल्पिक रास्ता:** {row['alternative_paths']}")
            st.markdown("---")
    else:
        st.warning("क्षमा करें, आपके लिए कोई विकल्प नहीं मिला।")
