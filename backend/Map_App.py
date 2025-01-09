import pandas as pd
from flask import Flask, render_template, request
from flask_caching import Cache
import os
from MapProject import clean_data, filter_conditions, create_combined_map
from flask_compress import Compress

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})
Compress(app)
csv_file_path = "Curb_Ramps_20241226.csv"
df = pd.read_csv(csv_file_path)
df_cleaned = clean_data(df)
missing_ramps, poor_condition_ramps = filter_conditions(df_cleaned)
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
    return render_template('index.html', combined_map_file=f"/{combined_map_path}")

@app.route('/search', methods=['GET'])
def search_location():
    street_query = request.args.get('street', '').strip().lower()
    if not street_query:
        return render_template(
            'search.html',
            combined_map_file=f"/{combined_map_path}",
            error_message="Please enter a street name to search."
        )

    cached_map = cache.get(street_query)
    if cached_map:
        return render_template('map.html', map_file=f"/{cached_map}")

    df_filtered = df_cleaned[df_cleaned['LocationDescription'].str.lower().str.contains(street_query, na=False)]

    if df_filtered.empty:
        return render_template(
            'search.html',
            combined_map_file=f"/{combined_map_path}",
            error_message=f"No results found for: {street_query}"
        )

    zoomed_map_path = f"static/maps/{street_query}_map.html"
    create_combined_map(
        missing_ramps=missing_ramps,
        poor_condition_ramps=poor_condition_ramps,
        filtered_data=df_filtered,
        file_name=zoomed_map_path,
        use_clustering=True
    )

    cache.set(street_query, zoomed_map_path)
    return render_template('map.html', map_file=f"/{zoomed_map_path}")
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/legend')
def legend():
    return render_template('legend.html')
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

