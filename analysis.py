import streamlit as st
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud  # Ensure this import is included

def analysis_page():
    st.title("Market Basket Analysis")

    # Load data
    @st.cache_data
    def load_data():
        return pd.read_csv("Groceries_dataset.csv")

    data = load_data()

    st.write("Data Overview")
    st.markdown(
        """
        ##### The data used here shows the transactions made by the customers with their member number and the date of transaction and the list of items they bought.
    """
    )
    # Display data preview
    st.write(data.head())

    # Data Preprocessing
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.set_index('Date')
    data["Hour"] = data.index.hour
    data["Weekday"] = data.index.weekday + 1

    # Plot total number of items sold by date
    st.sidebar.header("Plots")
    if st.sidebar.checkbox("Total Number of Items Sold by Date", False):
        daily_sales = data.resample("D")['itemDescription'].count()
        fig, ax = plt.subplots(figsize=(12, 5))
        daily_sales.plot(ax=ax, grid=True)
        ax.set_title("Total Number of Items Sold by Date")
        ax.set_xlabel("Date")
        ax.set_ylabel("Total Number of Items Sold")
        st.pyplot(fig)

    # Plot total number of items sold by month
    if st.sidebar.checkbox("Total Number of Items Sold by Month", False):
        monthly_sales = data.resample("M")['itemDescription'].count()
        fig, ax = plt.subplots(figsize=(12, 5))
        monthly_sales.plot(ax=ax, grid=True)
        ax.set_title("Total Number of Items Sold by Month")
        ax.set_xlabel("Date")
        ax.set_ylabel("Total Number of Items Sold")
        st.pyplot(fig)

    # Item Frequency Analysis
    if st.sidebar.checkbox("Item Frequency Analysis", False):
        st.write("Item Frequency Analysis")
        item_counts = data['itemDescription'].value_counts()
        st.bar_chart(item_counts)

    # Word Cloud
    if st.sidebar.checkbox("Item Word Cloud", False):
        st.write("Item Word Cloud")
        st.markdown("**A Word Cloud (or Tag Cloud) is a graphical representation of word frequency. In the context of item data, an Item Word Cloud displays the most common items or terms, with their size in the cloud proportional to their frequency or importance.**")
        text = ' '.join(data['itemDescription'].tolist())
        wordcloud = WordCloud(background_color='white', width=1200, height=1200, max_words=100).generate(text)
        fig, ax = plt.subplots(figsize=(15, 15))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

    # Market Basket Analysis
    st.sidebar.header("Market Basket Analysis")
    if st.sidebar.checkbox("Run Market Basket Analysis", False):
        
        transactions = [x[1]['itemDescription'].tolist() for x in data.groupby(['Member_number', 'Date'])]
        
        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        transactions_df = pd.DataFrame(te_ary, columns=te.columns_)
        
        # Frequent itemsets
        freq_items = apriori(transactions_df, min_support=0.001, use_colnames=True)
        freq_items['length'] = freq_items['itemsets'].apply(lambda x: len(x))
        st.write("Frequent Itemsets")
        st.write(freq_items.head())
        
        # Association rules
        rules = association_rules(freq_items, metric="confidence", min_threshold=0.001)
        
        # Convert frozensets to lists for compatibility
        rules['antecedents'] = rules['antecedents'].apply(lambda x: list(x))
        rules['consequents'] = rules['consequents'].apply(lambda x: list(x))
        
        st.write("Association Rules")
        st.write(rules.head())
        
        # Plot Support vs Confidence
        if st.sidebar.checkbox("Support vs Confidence", False):
            fig = px.scatter(rules, x='support', y='confidence', color='lift', size='confidence', hover_name='antecedents', size_max=60)
            fig.update_layout(title="Support vs Confidence", xaxis_title="Support", yaxis_title="Confidence")
            st.plotly_chart(fig)
        
        # Plot Support vs Lift
        if st.sidebar.checkbox("Support vs Lift", False):
            fig = px.scatter(rules, x='support', y='lift', color='confidence', size='lift', hover_name='antecedents', size_max=60)
            fig.update_layout(title="Support vs Lift", xaxis_title="Support", yaxis_title="Lift")
            st.plotly_chart(fig)

        if st.sidebar.checkbox("Lift vs Confidence", False):
            fig = px.scatter(rules, x='lift', y='confidence', color='support', size='confidence', hover_name='antecedents', size_max=60)
            fig.update_layout(title="Lift vs Confidence", xaxis_title="Lift", yaxis_title="Confidence")
            st.plotly_chart(fig)
