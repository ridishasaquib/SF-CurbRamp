SF Curb Ramp is an interactive web application that visualizes the accessibility of curb ramps in San Francisco. This tool highlights missing and poorly maintained ramps to raise awareness about accessibility issues. Users can search by location, view ramp conditions, and interact with an informative map. Designed for policymakers, advocates, and the community to encourage inclusive infrastructure development. Built using Flask, Folium, Pandas, and HTML/CSS.

project-folder/
├── app.py                # Backend: Flask application
├── utils.py              # Backend: Utility functions
├── templates/            # Frontend: HTML files
│   ├── index.html
│   ├── search.html
│   ├── about.html
│   ├── legend.html
├── static/               # Frontend: Static assets
│   ├── css/
│   ├── images/
├── Curb_Ramps.csv        # Backend: Dataset
├── requirements.txt      # Backend: Dependencies
├── README.md             # Documentation
