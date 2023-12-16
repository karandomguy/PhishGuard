import streamlit as st
from main import final

def main():
    st.title("PhishGuard")

    # Get user input (if needed)
    st.write("PhishGuard is a comprehensive phishing email detection solution designed to enhance email security by employing two distinct models. The first model focuses on detecting phishing URLs, while the second model checks for phishing content within the email body. By combining these approaches, PhishGuard provides a robust defense against phishing attacks in a single, unified solution.")
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

