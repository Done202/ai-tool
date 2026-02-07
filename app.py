import streamlit as st
import google.generativeai as genai

# আপনার স্ট্রীমলিট Secrets থেকে API Key সংগ্রহ
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key খুঁজে পাওয়া যায়নি। দয়া করে Manage app > Settings > Secrets-এ গিয়ে কি (Key) সেট করুন।")

def generate_ecommerce_content(product_name, niche):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    You are an expert E-commerce Growth Hacker. 
    Task: Create high-converting content for the product: {product_name} in the {niche} niche.
    Provide:
    1. A catchy product title.
    2. A psychological product description (focus on benefits, not features).
    3. 3 Facebook Ad copies with different hooks (Emotional, Rational, Urgent).
    4. 5 SEO Keywords.
    Make the tone persuasive and professional.
    """
    response = model.generate_content(prompt)
    return response.text

# ওয়েব ইন্টারফেস ডিজাইন (আগের মতোই সুন্দর)
st.set_page_config(page_title="AI E-com Pro", layout="wide")
st.title("🚀 E-commerce AI Success Engine")
st.subheader("আপনার পণ্যের তথ্য দিন এবং ম্যাজিক দেখুন")

col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input("পণ্যের নাম (যেমন: Ergonomic Office Chair)")
    niche = st.selectbox("নিশ সিলেক্ট করুন", ["Fashion", "Electronics", "Health & Beauty", "Home Decor", "Gadgets"])
    generate_btn = st.button("Generate Strategy & Content")

with col2:
    if generate_btn:
        if product_name:
            with st.spinner('এআই আপনার জন্য সেরা কন্টেন্ট তৈরি করছে...'):
                try:
                    result = generate_ecommerce_content(product_name, niche)
                    st.markdown("### 🎯 আপনার কন্টেন্ট রেডি:")
                    st.write(result)
                except Exception as e:
                    st.error(f"একটি সমস্যা হয়েছে: {e}")
        else:
            st.error("দয়া করে পণ্যের নাম লিখুন।")
