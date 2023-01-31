import streamlit as st
from keybert import KeyBERT
import pandas as pd
import matplotlib.pyplot as plt

app = st.container()
def process(keywords_set):
    keywords = []
    for tuples in keywords_set:
        keywords.append(tuples[0])
    return keywords

def plot_keywords(keywords):
    keywords = pd.Series(keywords).value_counts(ascending = True)
    fig, ax = plt.subplots(figsize =(15, 15))
    ax.barh(keywords.keys(), keywords)
    plt.rcParams.update({'font.size': 25})
    return fig
with app:
    model_keyword = KeyBERT()
    if 'keywords' not in st.session_state:
        st.session_state['keywords'] = []
    with st.form("app_form"):
        text = st.text_input(label = 'Insert text',
                    value = 'It is the oldest mummy, complete and covered in gold, ever found in Egypt.')
        num_keywords = st.slider('number of keywords', 1, 3, 1)
        set_keywords = st.slider('set of keywords', 1, 3, 1)
        submitted = st.form_submit_button("Submit")
        if submitted:
            keywords = process(model_keyword.extract_keywords(text, keyphrase_ngram_range=(1, num_keywords),top_n = set_keywords))
            st.session_state.keywords.extend(keywords)
            st.pyplot(plot_keywords(st.session_state.keywords))
