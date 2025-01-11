# SF Curb Ramp

SF Curb Ramp is an interactive web application that visualizes the accessibility of curb ramps in San Francisco. This tool highlights missing and poorly maintained ramps to raise awareness about accessibility issues. Users can search by location, view ramp conditions, and interact with an informative map.

Designed for policymakers, advocates, and the community to encourage inclusive infrastructure development.

Built using **Flask**, **Folium**, **Pandas**, and **HTML/CSS**.

---

## Features
- Search functionality to locate curb ramps by street or area.
- Interactive map displaying ramp conditions (missing, poorly maintained, and good condition).
- Informative "About" and "Legend" pages for additional context.
- Highlight areas in need of improvement to encourage inclusivity.

---

## Project Structure

```plaintext
project-folder/
├── Map_App.py                 # Backend: Flask application
├── MapProject.py               # Backend: Utility functions
├── templates/             # Frontend: HTML files
│   ├── index.html         # Homepage
│   ├── search.html        # Search functionality
│   ├── about.html         # About the project
│   ├── legend.html        # Map legend
│   ├── map.html           # Filtered map page
├── static/                # Frontend: Static assets
│   ├── css/
│   │   ├── style.css      # Main styles for the application
│   │   ├── search-style.css  # Styles for the search page
│   ├── images/
│       ├── logo.png       # Project logo
│       ├── streetsf.jpeg  # Image used in the "About" page
│       ├── bridge.jpeg    # Image used in the "About" page
│       ├── nighsf.jpg     # Night view of SF
├── Curb_Ramps.csv         # Backend: Dataset
├── requirements.txt       # Backend: Python dependencies
├── README.md              # Documentation
