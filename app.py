import streamlit as st
import google.generativeai as genai

# Secrets থেকে API Key গ্রহণ
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key খুঁজে পাওয়া যায়নি। দয়া করে Secrets-এ গিয়ে কি (Key) সেট করুন।")

def generate_ecommerce_content(product_name, niche):
    # মডেলের নাম আপডেট করা হয়েছে যা 404 এরর দূর করবে
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Create catchy product title, description, and 3 Facebook ad copies for: {product_name} in {niche} niche."
    response = model.generate_content(prompt)
    return response.text

st.title("🚀 E-commerce AI Success Engine")
product_name = st.text_input("পণ্যের নাম লিখুন:")
niche = st.selectbox("নিশ:", ["Fashion", "Electronics", "Gadgets", "Home Decor"])

if st.button("Generate Strategy & Content"):
    if product_name:
        with st.spinner('তৈরি হচ্ছে...'):
            try:
                result = generate_ecommerce_content(product_name, niche)
                st.write(result)
            except Exception as e:
                st.error(f"সমস্যা: {str(e)}")
