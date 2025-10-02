# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 19:14:09 2025

@author: Dhanush Ramachandran
"""

# streamlit app for autocorrect/ spell checker
import streamlit as st
from textblob import TextBlob
import os
import sys
from src.spell_checker_ops import SpellSuggestion



st.set_page_config(page_title="WhatsApp Autocorrect,Spell checker", page_icon="💬")

st.title("💬 WhatsApp Autocorrect / Spell Checker")
st.write("Type your message below and get suggested corrections!")

# Input box for user text
user_input = st.text_area("Enter your message:", "")

if st.button("Check & Correct"):
    if user_input.strip() == "":
        st.warning("Please enter some text to check.")
    else:
        # Create TextBlob object
        blob = TextBlob(user_input)
        #corrected_text = str(blob.correct())
        
        
        
        # Optional: show suggestions for each word
        st.subheader("🔍 Suggestions for words:")
        suggestions = {} 
        
        for word in user_input.split():
            if len(word)>1:
                suggestions[word]=[] 
                spell_checker = SpellSuggestion(word, no_of_suggestions=3)
                sugg_words = spell_checker.aggregated_suggestion() 
                suggestions[word]=sugg_words
                
        st.subheader("✅ Suggested changes:")
        st.success(suggestions)
                
        if suggestions:
            st.json(suggestions)
        else:
            st.info("No corrections needed!")
