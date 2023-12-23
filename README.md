# PhishGuard: One-Stop Phishing Email Detection Solution

## Overview

PhishGuard is a comprehensive phishing email detection solution designed to enhance email security by employing two distinct models. The first model focuses on detecting phishing URLs, while the second model checks for phishing content within the email body. By combining these approaches, PhishGuard provides a robust defense against phishing attacks in a single, unified solution.

## Features

- **URL-based Phishing Detection:** PhishGuard scans emails for existing URLs, extracts features from them, and leverages a Random Forest model to predict whether the URLs are phishing or benign.

- **Content-based Phishing Detection:** In cases where no URLs are found, PhishGuard directly analyzes the email content using a TF-IDF and SVM pipeline to identify phishing attempts.

- **Unified Solution:** PhishGuard streamlines the phishing detection process by seamlessly integrating both URL and content-based models, ensuring a comprehensive defense against phishing threats.
- **Web Platform:** You can use the application through our website [phish-guard.streamlit.app](https://phish-guard.streamlit.app/)

## Installation

1. Clone the PhishGuard repository:

   ```bash
   git clone https://github.com/karandomguy/PhishGuard.git
   cd PhishGuard
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. First, add this chrome extension [Copy as Markdown](https://chromewebstore.google.com/detail/copy-as-markdown/nlaionblcaejecbkcillglodmmfhjhfi?pli=1)
<img width="1440" alt="Screenshot 2023-11-16 at 12 06 05 AM" src="https://github.com/karandomguy/PhishGuard/assets/92136711/c4a03841-26f9-4c16-b18f-aba1a624bc5d">

2. Select the content of your email and right-click

3. Select "Copy selection as Markdown" 
  <img width="1188" alt="Screenshot 2023-11-16 at 12 04 21 AM" src="https://github.com/karandomguy/PhishGuard/assets/92136711/078435b0-988a-439b-8979-964eaf8b6aa1">

4. Run the [PhishGuard application](https://phish-guard.streamlit.app/), paste the content and hit the "Submit" button.
   <img width="1440" alt="Screenshot 2023-12-24 at 2 51 24 AM" src="https://github.com/karandomguy/PhishGuard/assets/92136711/b2203f39-f513-4ce8-971d-69d4ca0b99fa">



## Models

- **URL-based Phishing Detection Model:**
  - **Algorithm:** Random Forest
  - **Features:** Extracted from URLs found in the email

- **Content-based Phishing Detection Model:**
  - **Algorithm:** TF-IDF and SVM pipeline

  - **Features:** Analyzes the content of the email

## Contribution

We welcome contributions to enhance the capabilities and efficiency of PhishGuard. To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

PhishGuard is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Reasearch papers implemented
  - [Detecting Phishing Websites Using Machine Learning](https://github.com/karandomguy/PhishGuard/blob/main/research_papers/Detecting_Phishing_Websites_Using_Machine_Learning.pdf)
  - [Phishing Email Detection Using Robust NLP Techniques](https://github.com/karandomguy/PhishGuard/blob/main/research_papers/Phishing_Email_Detection_Using_Robust_NLP_Techniques.pdf)
  - [Phishing Website Detection Using Machine Learning](https://github.com/karandomguy/PhishGuard/blob/main/research_papers/Phishing_Website_Detection_Using_Machine_Learning.pdf)

Feel free to reach out for any questions or concerns. Happy phishing detection!

**Note:** This readme assumes you have Python and Git installed on your system. Adjust installation commands based on your environment.
