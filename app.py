import streamlit as st

# Set page config
st.set_page_config(page_title="CraftMyAI - AI Solutions", page_icon="🛠️", layout="wide")

# Center align the app
st.markdown(
    """
    <style>
        .main {
            text-align: left;
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
page = st.sidebar.radio("", ["🏠 Home", "📩 Request AI Solution", "📝 Feedback", "ℹ️ About Us"])

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


# Feedback Page
elif page == "📝 Feedback":
    st.title("📝 CraftMyAi Feedback Form")
    st.write("We value your feedback! Help us improve by sharing your thoughts.")
    
    # Feedback Form
    name = st.text_input("Your Name", "")
    email = st.text_input("Your Email", "")
    rating = st.slider("Rate your experience (1-5)", 1, 5, 3)
    feedback = st.text_area("Your Feedback", "")
    
    if st.button("Submit Feedback"):
        if name and email and feedback:
            # Simulate saving feedback (Can be connected to a database later)
            feedback_data = {
                "Name": name,
                "Email": email,
                "Rating": rating,
                "Feedback": feedback
            }
            df = pd.DataFrame([feedback_data])
            df.to_csv("feedback.csv", mode='a', header=False, index=False)
            
            st.success("✅ Thank you for your feedback! We appreciate your input.")
        else:
            st.error("⚠️ Please fill out all fields before submitting.")
    
    st.write("---")
    st.write("📧 Contact us at support@craftmyai.com")