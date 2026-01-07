#!/usr/bin/env python
# coding: utf-8

# In[8]:


from google import genai
from google.genai import types
print("Imports successful!")


# In[19]:


# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key="AIzaSyB8Bax2L5pZH3xOCOIdlw9lkoWkR1h1ZQc"
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HER"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")


# In[20]:


import streamlit as st
from google import genai
from google.genai import types
client=genai.Client(api_key="AIzaSyB8Bax2L5pZH3xOCOIdlw9lkoWkR1h1ZQc")
st.title("spacebot")
query=st.text_input("Ask a question:")

if st.button("Ask"):
    contents=[
        types.Content(role="user",parts=[types.Part.from_text(text=query)]
                     )
    ]
    response=client.models.generate_content(model="gemini-3-flash-preview",contents=contents)
    st.write(response.text)


# In[ ]:





# In[ ]:





# In[ ]:




