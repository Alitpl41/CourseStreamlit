import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from misc import to_float

#title and subtitle
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlits")


# upload
upload = st.file_uploader("Upload Your Dataset (In Csv Format)" )

if upload is not None:
    data = pd.read_csv(upload)
    
    
#show dataset

if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

# Analyze Of Data 

if upload is not None:
    if st.checkbox("Intermediate Level Head Of Data"):
        #Filter For Price
        filter_data = st.number_input("Price Filter")
        if filter_data is not None:
            data["price"] = data["price"].apply(to_float)
            filter_price_data = data[(data["level"]=="Intermediate Level") & (data["price"] >filter_data)].head()
            st.write(filter_price_data)
        else:
            st.write(data[data["level"]=="Intermediate Level"].head())
        
        if st.button("Chart NumLecture"):
            fig, ax = plt.subplots()
            sns.scatterplot(data,  x="num_lectures", y="price", ax=ax)
            st.pyplot(fig)
            

# Check data types of Each Column            
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)

# Check data types of Each Rows or Column
if upload is not None:
    data_shape = st.radio("What Dimension Do You Want To Check ?", ("Rows","Columns"))
    if data_shape=='Rows':
        st.text("Number of Rows ")
        st.write(data.shape[0])
    elif data_shape =='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])
        

#Find Null Values in The Dataset
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null Values in the dataset"):
            fig, ax = plt.subplots()
            sns.heatmap(data.isnull(), cmap="viridis", cbar=False, ax=ax)
            st.pyplot(fig)
    else:
        st.success("Congratulation!!! , No Missing Values")
        

#Find Duplicate Values in The Dataset
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This Dataset Contains Same Duplicate Values ")
        dup = st.selectbox("Do you want to Remove Duplicate Values", ("Select One", "Yes", "No"))
        
        if dup == "Yes":
            st.text("Duplicated Values Are Removed")
        if dup == "No":
            st.text("Nothing changed")

#Get overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include="all"))
        

#About Section
if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks To Streamlit")


#Finish
st.success("App finished")