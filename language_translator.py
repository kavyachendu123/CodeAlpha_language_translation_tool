#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import required modules
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Map language names to codes
lang_codes = {v.lower(): k for k, v in LANGUAGES.items()}

# Runtime interaction
while True:
    user_text = input("Enter text to translate (or type 'exit' to quit): ").strip()
    if user_text.lower() == 'exit':
        print(" Exiting translator.")
        break

    src_lang = input("Enter source language: ").strip().lower()
    dest_lang = input("Enter target language: ").strip().lower()

    src_code = lang_codes.get(src_lang)
    dest_code = lang_codes.get(dest_lang)

    if not src_code or not dest_code:
        print(" Invalid language. Please check your input.\n")
        continue

    try:
        translated = translator.translate(user_text, src=src_code, dest=dest_code)
        print(f"\n Translated ({src_lang} → {dest_lang}):\n{translated.text}\n")
    except Exception as e:
        print(f" Error: {e}\n")

