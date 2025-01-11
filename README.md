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
├── MapProject.py              # Backend: Utility functions
├── templates/                 # Frontend: HTML templates for different pages
│   ├── Contains all HTML files (e.g., index.html, search.html, about.html, legend.html, map.html)
├── static/                    # Frontend: Static assets (CSS, images, etc.)
│   ├── css/                   # Stylesheets for the application
│   ├── images/                # Image assets (e.g., logo, map images)
├── Curb_Ramps.csv             # Dataset for ramp data
├── requirements.txt           # Python dependencies for the project
├── README.md                  # Project documentation

