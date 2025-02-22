import streamlit as st
from scrape import scrape_website, split_dom_content,clean_body_content,extract_body
from parse import parse_with_ollama
st.title("AI Web Scrapper")
url = st.text_input("Enter the Website URL: ")

if st.button("Scrape Site"):
    st.write("Scrapping the website")

    result = scrape_website(url)
    body_content = extract_body(result)
    clean_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View DOM Content: "):
        st.text_area("DOM Content",clean_content,height = 300)

if 'dom_content' in st.session_state:
    parse_description : st.text_area("Describe what you want to parse? ")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing Content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            results = parse_with_ollama(dom_chunks,parse_description)
            st.write(results)
