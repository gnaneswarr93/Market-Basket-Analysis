import streamlit as st
from analysis import analysis_page
from home import home_page

def main():
    """
    Main function to render the Streamlit app with navigation between Home and Analysis pages.
    """
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a Page", ["Home", "Analysis"])

    # Conditional rendering based on selected page
    if page == "Home":
        st.title("Welcome to the Market Basket Analysis App")
        home_page()  # Function to render the Home page
    elif page == "Analysis":
        analysis_page()  # Function to render the Analysis page

if __name__ == "__main__":
    main()
