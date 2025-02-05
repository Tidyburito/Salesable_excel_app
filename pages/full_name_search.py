import streamlit as st
import pandas as pd

@st.cache_data 
def load_data():
    df = pd.read_excel("data/All IN Contacts Suppression (Feb).xlsx")
    return df

df = load_data()

search_variable = st.text_input("Enter a name")

# Initialize matched_column as an empty list
matched_column = []
for column in df.columns:
    if df[column].dtype == object:  # Ensures we're only searching in text columns
        if df[column].str.contains(search_variable, na=False).any():
            matched_column.append(column)

if not matched_column:  # Check if the list is empty
    st.write("No matches found")
else:
    for i in matched_column:
        st.write(f'Matches in {i} column')
        filtered_df = df[df[i].str.contains(search_variable, na=False)]
        st.dataframe(filtered_df, use_container_width=True)
