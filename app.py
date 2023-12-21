import streamlit as st
from PIL import Image
from main import final
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
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
    )
def main():
    set_bg_hack_url()
    #my_logo = add_logo(logo_path="", width=50, height=60)
    #st.image(my_logo)
    st.title("PhishGuard")

    # Get user input (if needed)
    st.write("PhishGuard is a comprehensive phishing email detection solution designed to enhance email security by employing two distinct models. The first model focuses on detecting phishing URLs, while the second model checks for phishing content within the email body. By combining these approaches, PhishGuard provides a robust defense against phishing attacks in a single, unified solution.")
    st.subheader("Steps")
    st.caption("Select the content of your email and right-click")
    st.caption("1. First, add this chrome extension [Copy as Markdown](https://chromewebstore.google.com/detail/copy-as-markdown/nlaionblcaejecbkcillglodmmfhjhfi?pli=1)")
    st.caption("2. Select the content of your email and right-click")
    st.caption("3. Select **Copy selection as Markdown**")
    st.caption("4. Paste the content and hit the *Submit* button.")
    
    #st.image('')
    user_input = st.text_area("Enter Email Content")
    text = ''.join(user_input)
    text = text.replace('\n', ' ')
    # Call your function from the other file
    result = final(user_input)

    # Display the result
    if st.button('Submit'):
        st.write("Result:", result)

if __name__ == "__main__":
    main()

