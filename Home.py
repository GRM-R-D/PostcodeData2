import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)


@st.cache_resource
def add_logo(logo_url: str, width: int = 250, height: int = 300):
    """Add a logo (from logo_url) on the top of the navigation page of a multipage app."""
    logo_css = f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url({logo_url});
                background-repeat: no-repeat;
                background-size: {width}px {height}px; /* Set the size of the logo */
                padding-top: {height + 20}px;
                background-position: 20px 0px;
            }}
        </style>
    """
    st.markdown(logo_css, unsafe_allow_html=True)


# URL of the logo image
logo_url = "https://grmdevelopment.wpengine.com/wp-content/uploads/2020/07/GRM-master-logo-02.png"

# Add the logo with a specified height and resize using CSS
add_logo(logo_url, height=100)

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
