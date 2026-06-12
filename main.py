import streamlit as st
import main_helper as mh
import textwrap

st.title("Youtube Video Summarizer")

with st.sidebar:
    with st.form(key="my_form"):
        video_url = st.sidebar.text_area(
            label = "Enter the Youtube video URL",
            max_chars= 50,
        )
        
        query=st.sidebar.text_area(
            label = "Enter your question about the video",
            max_chars= 100
        )

        submit_button = st.form_submit_button(label="Submit")

if query and video_url:

    vector_store = mh.create_vectors(video_url)
    response, docs = mh.get_response(vector_store, query)
    st.subheader("Answer:")
    wrapped_response = textwrap.fill(response, width=80)
    st.text(wrapped_response)