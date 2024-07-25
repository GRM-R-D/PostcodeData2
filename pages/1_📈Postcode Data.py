import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster, Geocoder
from streamlit_folium import folium_static
from branca.element import Template, MacroElement

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

    # Add a custom legend to the map
    template = """
        {% macro html(this, kwargs) %}
        <html>
        <head>
          <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
          <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
          <style>
            .maplegend {
              position: absolute;
              z-index: 9999;
              border: 2px solid grey;
              background-color: rgba(255, 255, 255, 0.8);
              border-radius: 6px;
              padding: 10px;
              font-size: 14px;
            }
            .maplegend .legend-title {
              text-align: left;
              margin-bottom: 5px;
              font-weight: bold;
            }
            .maplegend .legend-scale ul {
              margin: 0;
              padding: 0;
              list-style: none;
            }
            .maplegend .legend-scale ul li {
              font-size: 80%;
              margin-bottom: 2px;
            }
            .maplegend ul.legend-labels li span {
              display: block;
              float: left;
              height: 16px;
              width: 30px;
              margin-right: 5px;
              border: 1px solid #999;
            }
          </style>
          <script>
            $( function() {
              $( "#maplegend" ).draggable();
            });
          </script>
        </head>
        <body>
          <div id='maplegend' class='maplegend' 
              style='right: 20px; bottom: 20px;'>
            <div class='legend-title'>Plasticity Index</div>
            <div class='legend-scale'>
              <ul class='legend-labels'>
                <li><span style='background: green;'></span>Plasticity Index < 10</li>
                <li><span style='background: yellow;'></span>10 ≤ Plasticity Index < 20</li>
                <li><span style='background: orange;'></span>20 ≤ Plasticity Index < 40</li>
                <li><span style='background: red;'></span>Plasticity Index ≥ 40</li>
              </ul>
            </div>
          </div>
        </body>
        </html>
        {% endmacro %}
        """
    macro = MacroElement()
    macro._template = Template(template)
    m.get_root().add_child(macro)

    return m


def show_map(filter_df):
    m = create_map(filter_df)  # Create the map with the filtered data
    folium_static(m)  # Display the map with the legend


# Call the show_map function with your filtered DataFrame
# show_map(filtered_df)


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

    # Dropdown for Project ID
    project_ids = sorted(filtered_df['ProjectID'].astype(str).unique())
    selected_project_id = st.selectbox("Select Project ID", options=[""] + project_ids)

    # Filter DataFrame based on selected Project ID
    if selected_project_id:
        filtered_df = filtered_df[filtered_df['ProjectID'].astype(str) == selected_project_id]

    # Update Geology Code options based on the filtered DataFrame
    geology_codes = sorted(filtered_df['GeologyCode'].astype(str).unique())
    selected_geology_code = st.selectbox("Select Geology Code", options=[""] + geology_codes)

    # Apply Geology Code filter
    if selected_geology_code:
        filtered_df = filtered_df[filtered_df['GeologyCode'].astype(str) == selected_geology_code]

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
