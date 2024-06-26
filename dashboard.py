# # #Importing the necessary packages
# # import sys
# # import streamlit as st
# # import openpyxl
# # import pygwalker as pyg
# # import pandas as pd

# # #Setting up web app page
# # st.set_page_config(page_title='Exploratory Data Analysis App', page_icon=None, layout="wide")

# # #Creating section in sidebar
# # st.sidebar.write("****A) File upload****")

# # #User prompt to select file type
# # ft = st.sidebar.selectbox("*What is the file type?*",["Excel", "csv"])

# # #Creating dynamic file upload option in sidebar
# # uploaded_file = st.sidebar.file_uploader("*Upload file here*")

# # if uploaded_file is not None:
# #     file_path = uploaded_file

# #     if ft == 'Excel':
# #         try:
# #             #User prompt to select sheet name in uploaded Excel
# #             sh = st.sidebar.selectbox("*Which sheet name in the file should be read?*",pd.ExcelFile(file_path).sheet_names)
# #             #User prompt to define row with column names if they aren't in the header row in the uploaded Excel
# #             h = st.sidebar.number_input("*Which row contains the column names?*",0,100)
# #         except:
# #             st.info("File is not recognised as an Excel file")
# #             sys.exit()
    
# #     elif ft == 'csv':
# #         try:
# #             #No need for sh and h for csv, set them to None
# #             sh = None
# #             h = None
# #         except:
# #             st.info("File is not recognised as a csv file.")
# #             sys.exit()

# #     #Caching function to load data
# #     @st.cache_data(experimental_allow_widgets=True)
# #     def load_data(file_path,ft,sh,h):
        
# #         if ft == 'Excel':
# #             try:
# #                 #Reading the excel file
# #                 data = pd.read_excel(file_path,header=h,sheet_name=sh,engine='openpyxl')
# #             except:
# #                 st.info("File is not recognised as an Excel file.")
# #                 sys.exit()
    
# #         elif ft == 'csv':
# #             try:
# #                 #Reading the csv file
# #                 data = pd.read_csv(file_path)
# #             except:
# #                 st.info("File is not recognised as a csv file.")
# #                 sys.exit()
        
# #         return data

# #     data = load_data(file_path,ft,sh,h)

# # #=====================================================================================================
# # ## 1. Overview of the data
# #     st.write( '### 1. Dataset Preview ')

# #     try:
# #       #View the dataframe in streamlit
# #       st.dataframe(data, use_container_width=True)

# #     except:
# #       st.info("The file wasn't read properly. Please ensure that the input parameters are correctly defined.")
# #       sys.exit()


# # ## 2. Understanding the data
# #     st.write( '### 2. High-Level Overview ')

# #     #Creating radio button and sidebar simulataneously
# #     selected = st.sidebar.radio( "**B) What would you like to know about the data?**", 
# #                                 ["Data Dimensions",
# #                                  "Field Descriptions",
# #                                 "Summary Statistics", 
# #                                 "Value Counts of Fields"])

# #     #Showing field types
# #     if selected == 'Field Descriptions':
# #         fd = data.dtypes.reset_index().rename(columns={'index':'Field Name',0:'Field Type'}).sort_values(by='Field Type',ascending=False).reset_index(drop=True)
# #         st.dataframe(fd, use_container_width=True)

# #     #Showing summary statistics
# #     elif selected == 'Summary Statistics':
# #         ss = pd.DataFrame(data.describe(include='all').round(2).fillna(''))
# #         st.dataframe(ss, use_container_width=True)

# #     #Showing value counts of object fields
# #     elif selected == 'Value Counts of Fields':
# #         # creating radio button and sidebar simulataneously if this main selection is made
# #         sub_selected = st.sidebar.radio( "*Which field should be investigated?*",data.select_dtypes('object').columns)
# #         vc = data[sub_selected].value_counts().reset_index().rename(columns={'count':'Count'}).reset_index(drop=True)
# #         st.dataframe(vc, use_container_width=True)

# #     #Showing the shape of the dataframe
# #     else:
# #         st.write('###### The data has the dimensions :',data.shape)


# # #=====================================================================================================
# # ## 3. Visualisation

# #     #Selecting whether visualisation is required
# #     vis_select = st.sidebar.checkbox("**C) Is visualisation required for this dataset?**")

# #     if vis_select:

# #         st.write( '### 3. Visual Insights ')

# #         #Creating a PyGWalker Dashboard
# #         walker = pyg.walk(data, return_html=True)
# #         st.components.v1.html(walker, width=1100, height=800)  #Adjust width and height as needed


# # Importing the necessary packages
# import streamlit as st
# import pandas as pd
# import pygwalker as pyg

# # Setting up web app page
# st.set_page_config(page_title='PyGWalker Visualization App')

# # Creating section in sidebar
# st.sidebar.write("****File Upload****")

# # Dynamic file upload option in sidebar
# uploaded_file = st.sidebar.file_uploader("Upload file here", type=["csv", "xlsx"])

# if uploaded_file is not None:
#     file_extension = uploaded_file.name.split(".")[-1]

#     # Load data
#     if file_extension == 'csv':
#         data = pd.read_csv(uploaded_file)
#     elif file_extension == 'xlsx':
#         data = pd.read_excel(uploaded_file)
#     else:
#         st.error("Unsupported file format. Please upload a CSV or Excel file.")
#         st.stop()

#     # Visualizations
#     st.write("### Visualizations")

#     # Check if visualizations are required
#     vis_select = st.sidebar.checkbox("Show visualizations")

#     if vis_select:
#         st.write("#### PyGWalker Visualization")

#         try:
#             # Create PyGWalker dashboard
#             walker = pyg.walk(data)
#             html_string = str(walker)

#             # Display PyGWalker dashboard in Streamlit app
#             st.components.v1.html(html_string, width=1100, height=800)
#         except Exception as e:
#             st.error(f"An error occurred: {e}")

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to generate visualizations based on file path
def generate_visualizations(file_path):
    # Check file extension
    file_extension = file_path.split(".")[-1]
    
    if file_extension == 'csv':
        data = pd.read_csv(file_path)
    elif file_extension == 'xlsx':
        data = pd.read_excel(file_path)
    else:
        st.error("Unsupported file format. Please provide a CSV or Excel file.")
        st.stop()

    st.write("### Visualizations")

    # Example visualization 1: Histogram
    st.write("#### Histogram")
    numeric_columns = data.select_dtypes(include=['int', 'float']).columns
    selected_column = st.selectbox("Select a column for histogram", numeric_columns)
    plt.figure(figsize=(8, 6))
    sns.histplot(data[selected_column], kde=True)
    st.pyplot()

    # Example visualization 2: Pairplot
    st.write("#### Pairplot")
    sns.pairplot(data)
    st.pyplot()

    # Add more visualizations as needed


def main():
    st.title("Visualization App")

    # Sidebar for file upload
    st.sidebar.write("### File Upload")
    file_path = st.sidebar.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

    if file_path is not None:
        generate_visualizations(file_path)


if __name__ == "__main__":
    main()
