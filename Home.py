import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.write("# Welcome! 👋")

st.sidebar.success("Select a visual above")

st.markdown(
    """
    Welcome to this data demo!
    **👈 Select a demo from the sidebar** to see some examples
    of what we can do with our data!
    
    ### Any suggestions for new visualisations?
"""
)