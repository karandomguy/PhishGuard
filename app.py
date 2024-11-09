import streamlit as st
from PIL import Image
from main import final
from streamlit.components.v1 import html

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://removal.ai/wp-content/uploads/2021/09/black-background-01-pexels.png");
             background-size: cover;
             color: white;
         }}
         h1 {{
             color: #00acee;  /* Light blue for visibility */
         }}
         h2, h3 {{
             color: #f2f2f2;  /* Light gray for subheadings */
         }}
         .steps {{
             font-size: 18px;
             padding-left: 25px;
             color: white;  /* Ensures visibility of the steps text */
         }}
         </style>
         """,
         unsafe_allow_html=True
    )

def main():
    set_bg_hack_url()
    
    # Page Logo
    #st.sidebar.image("logo.png", width=150)
    
    # Title with Icon
    st.markdown("<h1 style='text-align: center;'>PhishGuard 🛡️</h1>", unsafe_allow_html=True)

    # Description
    st.write(
        """
        <div style='text-align: center; font-size: 18px;'>
            PhishGuard is a comprehensive phishing email detection solution designed to enhance email security by employing two distinct models. The first model detects phishing URLs, and the second model analyzes the email body content. By combining these approaches, PhishGuard provides a robust defense against phishing attacks in a single, unified solution.
        </div>
        """, unsafe_allow_html=True
    )

    # Steps Section with Icons
    st.subheader("Steps to Use PhishGuard")
    st.markdown("""
    <ul class="steps">
        <li>📋 <b>Step 1:</b> Add the chrome extension [Copy as Markdown](https://chromewebstore.google.com/detail/copy-as-markdown/nlaionblcaejecbkcillglodmmfhjhfi?pli=1)</li>
        <li>✂️ <b>Step 2:</b> Select the content of your email and right-click</li>
        <li>📋 <b>Step 3:</b> Select <i>Copy selection as Markdown</i></li>
        <li>✏️ <b>Step 4:</b> Paste the content below and hit the <i>Submit</i> button.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Text Input
    st.subheader("Enter Email Content")
    user_input = st.text_area("Paste email content here")
    
    # Clean the input
    text = ''.join(user_input).replace('\n', ' ')
    
    # Call the function from the other file
    if st.button('🔍 Submit', key="submit_button"):
        result = final(user_input)
        st.markdown(f"<div style='padding: 10px; border-radius: 10px; background-color: #d4edda; color: #155724;'>"
                    f"<strong>Result: </strong> {result}</div>", unsafe_allow_html=True)
    else:
        st.info("Please paste the email content and click Submit to analyze.")

if __name__ == "__main__":
    main()
