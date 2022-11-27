import streamlit as st
from textblob import TextBlob
import emoji
st.title("Hello User")
st.header("Welcome to emoji suggester")
st.subheader("First confirm that you are not a robot")
if st.checkbox("You are not a robot", value=False):
    st.write("Thank You :smile:")    
    raw_text = st.text_area("Enter Your Text below")
    if st.button("Analyze"):
        blob = TextBlob(raw_text)
        result = blob.sentiment.polarity
        if result > 0.0:
            custom_emoji = ':smile:'
            st.write(emoji.emojize(custom_emoji, ))
        elif result < 0.0:
            custom_emoji = ':disappointed:'
            st.write(emoji.emojize(custom_emoji, ))
        else:
            st.write(emoji.emojize(':expressionless:', ))
