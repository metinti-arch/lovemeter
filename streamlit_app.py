import streamlit as st

# Title of the app
st.title('Love Meter')

# Define a list of categories with individual colors
categories = {
    'Happiness': '#FFDDC1',
    'Sadness': '#BFDBFE',
    'Anger': '#FCA5A1',
    'Fear': '#C4B5FD',
    'Surprise': '#A7F3D0',
}

# Sidebar configuration
st.sidebar.header('Select a Category')

# Create bordered category groups
for category, color in categories.items():
    st.markdown(f'<h3 style="border: 2px solid {color}; padding: 5px; background-color: {color}; color: black;">{category}</h3>', unsafe_allow_html=True)
    st.text_input(f'Enter your feelings about {category}:')

# Add a submit button
if st.button('Submit'):  
    st.success('Thank you for sharing your feelings!')