import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster, Geocoder
from streamlit_folium import folium_static

# Set up the page configuration
st.set_page_config(page_title="Postcode Data", page_icon="📈", layout="wide")


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

# Set the title and sidebar header
st.markdown("# Postcode Data")
st.write("This page shows a table of UK postcodes and their corresponding Atterberg Limits")

# Read and preprocess the CSV data
filename = 'Points.csv'  # replace with your actual CSV file path
df = pd.read_csv(filename)

# Determine the range for Plasticity Index slider
plasticity_rng = (df['PlasticityIndex'].min(), df['PlasticityIndex'].max())


def get_color(plasticity_index):
    if plasticity_index >= 40:
        return 'red'
    elif 20 <= plasticity_index < 40:
        return 'orange'
    elif 10 <= plasticity_index < 20:
        return 'yellow'
    else:
        return 'green'


def create_map(filter_df):
    m = folium.Map(location=[filter_df['Latitude'].mean(), filter_df['Longitude'].mean()], zoom_start=6)
    marker_cluster = MarkerCluster().add_to(m)

    # Iterate over the filtered DataFrame rows and add markers to the cluster
    for _, row in filter_df.iterrows():
        location = [row['Latitude'], row['Longitude']]
        popup_content = (
            f"Postcode: {row['Postcode']}<br>"
            f"Project ID: {row['ProjectID']}<br>"
            f"Geology: {row['GeologyCode']}<br>"
            f"Plastic Limit: {row['PlasticLimit']}<br>"
            f"Liquid Limit: {row['LiquidLimit']}<br>"
            f"Plasticity Index: {row['PlasticityIndex']}<br>"
            f"Moisture Content: {row['MoistureContent']}"
        )
        popup = folium.Popup(popup_content, max_width=300)
        folium.Marker(location=location, popup=popup, icon=folium.Icon(color=get_color(row['PlasticityIndex']))).add_to(
            marker_cluster)

    # Add Geocoder plugin
    Geocoder().add_to(m)
    return m


def show_map(filter_df):
    m = create_map(filter_df)  # Create the map with the filtered data
    folium_static(m)  # Display the map


# Create a two-column layout
col1, col2 = st.columns([2, 2])

with col1:
    st.header("Map")

    # Add Plasticity Index slider
    plasticity_min, plasticity_max = plasticity_rng
    plasticity_filter = st.slider("Plasticity Index", min_value=int(plasticity_min), max_value=int(plasticity_max),
                                  value=(int(plasticity_min), int(plasticity_max)))

    # Apply Plasticity Index filter
    filtered_df = df[(df['PlasticityIndex'] >= plasticity_filter[0]) &
                     (df['PlasticityIndex'] <= plasticity_filter[1])]

    # Initialize session state
    if 'project_options' not in st.session_state:
        st.session_state.project_options = sorted(df['ProjectID'].astype(str).unique())
    if 'geology_options' not in st.session_state:
        st.session_state.geology_options = sorted(df['GeologyCode'].astype(str).unique())

    # Dropdown for Project ID
    filtered_project_ids = sorted(filtered_df['ProjectID'].astype(str).unique())
    selected_project_id = st.selectbox("Select Project ID", options=[""] + filtered_project_ids)

    # Dropdown for Geology Code
    if selected_project_id:
        filtered_df = filtered_df[filtered_df['ProjectID'].astype(str) == selected_project_id]
    filtered_geology_codes = sorted(filtered_df['GeologyCode'].astype(str).unique())
    selected_geology_code = st.selectbox("Select Geology Code", options=[""] + filtered_geology_codes)

    # Apply Geology Code filter
    if selected_geology_code:
        filtered_df = filtered_df[filtered_df['GeologyCode'].astype(str) == selected_geology_code]

    # Update project options based on selected geology code
    if selected_geology_code:
        filtered_projects_for_geology = sorted(filtered_df['ProjectID'].astype(str).unique())
        st.session_state.project_options = filtered_projects_for_geology
    else:
        st.session_state.project_options = sorted(df['ProjectID'].astype(str).unique())

    # Update geology options based on selected project ID
    if selected_project_id:
        filtered_geologies_for_project = sorted(filtered_df['GeologyCode'].astype(str).unique())
        st.session_state.geology_options = filtered_geologies_for_project
    else:
        st.session_state.geology_options = sorted(df['GeologyCode'].astype(str).unique())

    # Show the map with the filtered data
    show_map(filtered_df)

with col2:
    st.header("Data")

    # Group checkboxes
    show_utm = st.checkbox('Show UTM Coordinates', value=True)
    show_latlong = st.checkbox('Show LATLONG Coordinates', value=True)

    # Define column groups
    utm_columns = ['Easting', 'Northing']
    latlong_columns = ['Latitude', 'Longitude']

    # Determine which columns to display
    columns_to_display = []
    if show_utm:
        columns_to_display.extend(utm_columns)
    if show_latlong:
        columns_to_display.extend(latlong_columns)

    # Always show these columns and reorder them
    always_display_columns = ['ProjectID', 'LocationID', 'Postcode', 'GeologyCode', 'PlasticLimit', 'LiquidLimit',
                              'PlasticityIndex', 'MoistureContent']

    # Combine always displayed columns with selected columns
    columns_to_display = always_display_columns + columns_to_display

    # Ensure only existing columns are included
    columns_to_display = [col for col in columns_to_display if col in df.columns]

    # Filter DataFrame for display
    filtered_df_display = filtered_df[columns_to_display]
    st.dataframe(filtered_df_display, hide_index=True)
