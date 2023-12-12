from matplotlib.ticker import MaxNLocator
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

uploadedCSVFile = st.file_uploader("Choose a CSV file with columns Name and age", type="csv")


if uploadedCSVFile is not None:
    
    df = pd.read_csv(uploadedCSVFile)

    if 'Age' in df.columns and 'Name' in df.columns:
        st.write("Ages Histogram:")
        fig, ax = plt.subplots()

        ax.hist(df['Age'], bins=100, edgecolor='blue')
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        ax.set_title('Ages Histogram')

        st.pyplot(fig)
        
    else:
        st.error("File does not have name and age columns")
