# home.py
import streamlit as st

def home_page():
    st.title("Market Basket Analysis App")

    st.markdown("""
    ## Welcome to the Market Basket Analysis App!

    This application is designed to help you perform market basket analysis on transaction data. Here's a brief overview of what you can do:

    ### Features

    1. **Data Overview**:
       - View a preview of the dataset.
       - Understand the basic structure and content of the data.

    2. **Plots**:
       - **Total Number of Items Sold by Date**: See how the number of items sold varies over time.
       - **Total Number of Items Sold by Month**: View monthly trends in item sales.

    3. **Item Frequency Analysis**:
       - Analyze how frequently each item is sold.

    4. **Item Word Cloud**:
       - Generate a word cloud to visualize the most frequently sold items.

    5. **Market Basket Analysis**:
       - **Run Market Basket Analysis**: Discover patterns and relationships in the purchase data.
       - **Frequent Itemsets**: Find itemsets that frequently appear together in transactions.
       - **Association Rules**: Extract rules indicating relationships between items.

    6. **Interactive Plots for Market Basket Analysis**:
       - **Support vs Confidence**: Explore the relationship between support and confidence of association rules.
       - **Support vs Lift**: See how support correlates with lift.
       - **Lift vs Confidence**: Understand the correlation between lift and confidence.

    ### How to Use the Application

    1. **Navigate to the 'Analysis' page** using the sidebar to access various data analysis features.
    2. **Check the boxes in the sidebar** to generate and view plots and analyses.
    3. **Interact with the plots** to explore trends and patterns in the data.

    Feel free to explore the features and gain valuable insights from your transaction data!
    """)
