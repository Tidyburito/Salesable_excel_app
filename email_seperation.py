import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Email Search Page'
)




@st.cache_data #pickling the data frame such that every time its called it gets a different instance of the dataset
def load_data():
    df = pd.read_excel("data/All IN Emails Suppression (Feb).xlsx")
    return df


df = load_data()

search_variable  = st.text_input("Enter gmail to search")

filtered_df = df[df['Email'].str.contains(search_variable, na=False)]

st.dataframe(filtered_df, use_container_width=True)