import folium
from folium.plugins import MarkerCluster
import pandas as pd
import json

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            print(f"File found: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit()
    return pd.read_csv(file_path)

def clean_data(df):
    df_cleaned = df.dropna(subset=['Latitude', 'Longitude']).copy()
    df_cleaned.loc[:, 'LocationDescription'] = df_cleaned['LocationDescription'].fillna('Unknown Location')
    df_cleaned.loc[:, 'conditionScore'] = pd.to_numeric(df_cleaned['conditionScore'], errors='coerce').fillna(-1)
    return df_cleaned

def filter_conditions(df_cleaned):
    missing_ramps = df_cleaned[df_cleaned['conditionScore'] == 0]
    poor_condition_ramps = df_cleaned[
        (df_cleaned['conditionScore'] > 0) & 
        (df_cleaned['conditionScore'] <= 50) & 
        (~df_cleaned[['Latitude', 'Longitude']].apply(tuple, axis=1).isin(
            missing_ramps[['Latitude', 'Longitude']].apply(tuple, axis=1))
        )
    ]
    return missing_ramps, poor_condition_ramps

def create_combined_map(missing_ramps, poor_condition_ramps, filtered_data, file_name, use_clustering=True):
    filtered_data = filtered_data.head(1000)
    missing_ramps = missing_ramps.head(1000)
    poor_condition_ramps = poor_condition_ramps.head(1000)
    if not filtered_data.empty:
        center_lat = filtered_data['Latitude'].mean()
        center_lon = filtered_data['Longitude'].mean()
    else:
        center_lat, center_lon = 37.7749, -122.4194

    zoom_level = 15 if len(filtered_data) < 500 else 12
    sf_map = folium.Map(location=[center_lat, center_lon], zoom_start=zoom_level)

    marker_cluster = MarkerCluster().add_to(sf_map) if use_clustering else sf_map

    for _, row in missing_ramps.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"<strong>{row.get('LocationDescription', 'Unknown')}</strong><br>Condition: Missing",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(marker_cluster)

    for _, row in poor_condition_ramps.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"<strong>{row.get('LocationDescription', 'Unknown')}</strong><br>Condition: Poor",
            icon=folium.Icon(color="orange", icon="info-sign")
        ).add_to(marker_cluster)

    for _, row in filtered_data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"<strong>{row.get('LocationDescription', 'Unknown')}</strong>",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(marker_cluster)

    sf_map.save(file_name)
    print(f"Map saved to {file_name}")
