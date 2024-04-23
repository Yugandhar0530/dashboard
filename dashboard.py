# Importing the necessary packages
import streamlit as st
import pandas as pd
import pygwalker as pyg

# Setting up web app page
st.set_page_config(page_title='PyGWalker Visualization App')

# Creating section in sidebar
st.sidebar.write("****File Upload****")

# Dynamic file upload option in sidebar
uploaded_file = st.sidebar.file_uploader("Upload file here", type=["csv", "xlsx"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]

    # Load data
    if file_extension == 'csv':
        data = pd.read_csv(uploaded_file)
    elif file_extension == 'xlsx':
        data = pd.read_excel(uploaded_file)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        st.stop()

    # Visualizations
    st.write("### Visualizations")

    # Check if visualizations are required
    vis_select = st.sidebar.checkbox("Show visualizations")

    if vis_select:
        st.write("#### PyGWalker Visualization")

        try:
            # Create PyGWalker dashboard
            walker = pyg.walk(data)
            html_string = str(walker)

            # Display PyGWalker dashboard in Streamlit app
            st.components.v1.html(html_string, width=1100, height=800)
        except Exception as e:
            st.error(f"An error occurred: {e}")
