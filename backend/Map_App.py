import pandas as pd
from flask import Flask, render_template, request
from flask_caching import Cache
import os
from MapProject import clean_data, filter_conditions, create_combined_map
from flask_compress import Compress

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})
Compress(app)
# Load and clean data at app startup
csv_file_path = "Curb_Ramps_20241226.csv"
df = pd.read_csv(csv_file_path)
df_cleaned = clean_data(df)
missing_ramps, poor_condition_ramps = filter_conditions(df_cleaned)

# Pre-generate combined map
combined_map_path = "static/maps/combined_map.html"
os.makedirs(os.path.dirname(combined_map_path), exist_ok=True)

if not os.path.exists(combined_map_path):
    create_combined_map(
        missing_ramps=missing_ramps,
        poor_condition_ramps=poor_condition_ramps,
        filtered_data=df_cleaned,
        file_name=combined_map_path,
        use_clustering=True
    )

@app.route('/')
def home():
    """Render the homepage with the pre-generated combined map."""
    return render_template('index.html', combined_map_file=f"/{combined_map_path}")

@app.route('/search', methods=['GET'])
def search_location():
    """Search for ramps by street name and display the zoomed-in map."""
    street_query = request.args.get('street', '').strip().lower()

    # If no query, show the combined map with a search bar
    if not street_query:
        return render_template(
            'search.html',
            combined_map_file=f"/{combined_map_path}",
            error_message="Please enter a street name to search."
        )

    # Check if the map for the query is already cached
    cached_map = cache.get(street_query)
    if cached_map:
        return render_template('map.html', map_file=f"/{cached_map}")

    # Filter the data based on the search query
    df_filtered = df_cleaned[df_cleaned['LocationDescription'].str.lower().str.contains(street_query, na=False)]

    # If no results found
    if df_filtered.empty:
        return render_template(
            'search.html',
            combined_map_file=f"/{combined_map_path}",
            error_message=f"No results found for: {street_query}"
        )

    # Generate a zoomed-in map for the search quer
    zoomed_map_path = f"static/maps/{street_query}_map.html"
    create_combined_map(
        missing_ramps=missing_ramps,
        poor_condition_ramps=poor_condition_ramps,
        filtered_data=df_filtered,
        file_name=zoomed_map_path,
        use_clustering=True
    )

    # Cache the generated map
    cache.set(street_query, zoomed_map_path)
    return render_template('map.html', map_file=f"/{zoomed_map_path}")
@app.route('/about')
def about():
    """Render the About page."""
    return render_template('about.html')
@app.route('/legend')
def legend():
    """Render the legend page."""
    return render_template('legend.html')
if __name__ == "__main__":
    app.run(debug=True)

