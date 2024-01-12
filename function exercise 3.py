# Import the libraries
import nltk 
import spacy 
import pandas as pd 
import emoji 

def social_media_post_analysis(post):
  tokens = nltk.word_tokenize(post)
  nlp = spacy.load("en_core_web_sm")
  doc = nlp(tokens)
  sentiment = []
  keywords = []
  for token in doc:
    text = token.text
    if emoji.demojize(text) != text:
      sentiment.append("Emoji")
    else:
      if nlp(text).pos_ == "POSITIVE":
        sentiment.append("Positive")
      elif nlp(text).pos_ == "NEGATIVE":
        sentiment.append("Negative")
      else:
        sentiment.append("Neutral")
    keywords.extend(nlp(text).keywords)
  sentiment_df = pd.DataFrame(sentiment)
  keywords_df = pd.DataFrame(keywords)
post1 = """I just bought a new smartwatch and I'm loving it! It has so many features and functions that make my life easier. It tracks my heart rate, steps, calories, sleep quality, and more. It also has notifications for calls, messages, emails, and social media apps. It even has voice control so I can use it hands-free. It's like having a mini computer on my wrist! 😍"""
post2 = """I hate this airline! They lost my luggage and they won't compensate me for it. They also delayed my flight by two hours and they didn't offer me any food or drinks. They were rude and unprofessional. I will never fly with them again! 😡"""
post3 = """I'm feeling okay today. Nothing too exciting happened. Just watched some Netflix and ordered some pizza. Maybe tomorrow will be better. 🤷‍♂️"""
print(social_media_post_analysis(post1))
print(social_media_post_analysis(post2))
print(social_media_post_analysis(post3))
