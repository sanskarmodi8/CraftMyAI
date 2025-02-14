import streamlit as st

# Set page config
st.set_page_config(page_title="CraftMyAI - AI Solutions", page_icon="🛠️", layout="wide")

# Center align the app
st.markdown(
    """
    <style>
        .main {
            text-align: center;
        }
        .block-container {
            max-width: 800px;
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("CraftMyAI")
page = st.sidebar.radio("", ["🏠 Home", "📩 Request AI Solution", "ℹ️ About Us"])

# Home Page
if page == "🏠 Home":
    st.title("🛠️ Welcome to CraftMyAI ")
    st.write("")
    st.subheader("Get your custom AI solutions, tailored to your needs.")
    st.markdown(
        """
        - 🤖 **Personalized AI solutions** for your business and individual needs
        - 🛠️ **1-month free support** after delivery
        - 💰 **Transparent and flexible pricing based on complexity**
        - 🚀 **Affordable MVPs to kickstart your idea**
        - 🎨 **Customization at every step to match your exact needs**
        
        🔥 **Let's bring your AI vision to life!**
        """
    )
    st.write("")
    st.image(
        "https://images.pexels.com/photos/6153068/pexels-photo-6153068.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        width=800,
    )

# Request AI Solution Form
elif page == "📩 Request AI Solution":
    st.title("📩 Request Your AI Solution")
    st.write("Fill out the form below, and we will get back to you.")

    with st.form("ai_request_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        project_details = st.text_area("Project Description")
        budget = st.number_input("Estimated Budget (in INR)", min_value=0, step=100)
        submit_button = st.form_submit_button("Submit Request")

    if submit_button:
        st.success(f"✅ Thank you {name}! We will contact you at {email} soon.")

# About Us Page
elif page == "ℹ️ About Us":
    st.title("ℹ️ About CraftMyAI")
    st.write(
        "We specialize in developing AI solutions tailored for businesses and individuals."
    )
    st.markdown(
        """
        - 🎯 **Mission:** Deliver high-quality AI solutions with seamless support.
        - 🌍 **Vision:** Making AI accessible to businesses of all sizes.
        """
    )
