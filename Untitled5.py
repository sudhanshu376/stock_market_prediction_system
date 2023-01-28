#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests
import json
from textblob import TextBlob

# Your API key
api_key = "2e2a00dcf30045ff8ec2608106a95653"

# The stock market related keywords you want to search for
stock_market_keywords = "NESTLE"

# The base URL for the NewsAPI
base_url = "https://newsapi.org/v2/everything"

# Build the final URL with the parameters
url = f"{base_url}?q={stock_market_keywords}&sortBy=relevancy&apiKey={api_key}"

# Make the GET request to the NewsAPI
response = requests.get(url)

# Get the JSON data from the response
data = json.loads(response.text)

# Get the list of articles from the data
articles = data["articles"]

# Iterate through the articles and print the title and description
for article in articles:
    print("Title: ", article["title"])
    print(article["description"])
    text=(article["description"])
    print()
    #text='Northwestern Mutual chief investment officer Brent Schutte explained how investors can best position themselves in a mild, brief recession.'\
    
    analysis=TextBlob(text)
    
    print(analysis.sentiment.polarity)


# In[ ]:




