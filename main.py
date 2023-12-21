import re
import sys

def check_url(text):
    url_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(url_pattern, text)
    return urls

from urllib.parse import urlparse
from googlesearch import search

def having_ip_address(url):
    match = re.search(
        '(([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.'
        '([01]?\d\d?|2[0-4]\d|25[0-5])\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0

def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    if match:
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0

def google_index(url):
    site = search(url, 5)
    return 1 if site else 0

def count_dot(url):
    count_dot = url.count('.')
    return count_dot

def count_www(url):
    url.count('www')
    return url.count('www')

def count_atrate(url):
    return url.count('@')

def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')

def no_of_embed(url):
    urldir = urlparse(url).path
    return urldir.count('//')

def shortening_service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      url)
    if match:
        return 1
    else:
        return 0

def count_https(url):
    return url.count('https')

def count_http(url):
    return url.count('http')

def count_per(url):
    return url.count('%')

def count_ques(url):
    return url.count('?')

def count_hyphen(url):
    return url.count('-')

def count_equal(url):
    return url.count('=')

def url_length(url):
    return len(str(url))

def hostname_length(url):
    return len(urlparse(url).netloc)

def suspicious_words(url):
    match = re.search('PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',
                      url)
    if match:
        return 1
    else:
        return 0

def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits

def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters

from urllib.parse import urlparse
from tld import get_tld
import os.path

def fd_length(url):
    urlpath= urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

def get_tld_length(url):
    try:
        tld = get_tld(url, fail_silently=True)
        return len(tld)
    except:
        return -1

def feature_extractor(url):
    features = []

    # Feature 2: Abnormal URL
    abnormal_url_feature=abnormal_url(url)
    features.append(abnormal_url_feature)

    # Feature 3: Count Dot
    dot_count_feature = count_dot(url)
    features.append(dot_count_feature)

    # Feature 4: Count www
    www_count_feature = count_www(url)
    features.append(www_count_feature)

    # Feature 10: Count 'http'
    count_http_feature = count_http(url)
    features.append(count_http_feature)

    # Feature 14: Count '='
    count_equal_feature = count_equal(url)
    features.append(count_equal_feature)

    # Feature 16: Hostname Length
    hostname_length_feature = hostname_length(url)
    features.append(hostname_length_feature)

    # Feature 21: TLD Length
    tld_length_feature = get_tld_length(url)
    features.append(tld_length_feature)

    return features

import joblib

def get_prediction(url):
    
    model = joblib.load('best_pipeline_url.pkl')
    url_features = feature_extractor(url)
    prediction = model.predict([url_features])
    phishing=url+ ": PHISHING \n"
    benign=url+ ": BENIGN \n"
    if prediction[0]==1:
      return phishing
    else:
      return benign
    #print("There is", i, "% chance that this URL is malicious!")

def url_predict(url):
  prediction = get_prediction(url)
  return prediction

import joblib

best_pipeline = joblib.load('phishing_emails_models/best_pipeline_tfidf.pkl')

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
email_pipeline = joblib.load('phishing_emails_models/best_pipeline_tfidf.pkl')
def preprocess(text):
      words = word_tokenize(text)
      no_stop_words = [word for word in words if word.isalpha() and word.lower() not in stop_words]
      return ' '.join(no_stop_words)

def preprocess_email(email_text):

  # Preprocess the text
  preprocessed_email = preprocess(email_text)
  preprocessed_email=preprocessed_email.lower()
  return preprocessed_email
print(stop_words)

def email_predict(email_text):
  predicted_label = email_pipeline.predict([preprocess_email(email_text)])

  # Print the predicted label (1 for Safe Email, 0 for Phishing Email)
  safe="Predicted Label: SAFE EMAIL \n"
  phishy="Predicted Label: PHISHING EMAIL \n"
  if predicted_label[0] == '1':
    return safe
  elif predicted_label[0]=='0':
    return phishy
  else:
      return

def final(text):
  urls=check_url(text)
  ans=email_predict(text)
  if len(urls)!=0:
    x = "URL Predictions: \n\n"
    for i in urls:
      x=x+url_predict(i)+"\n"
    return x
  return ans+"\n"

