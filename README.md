# SF Curb Ramp

SF Curb Ramp is an interactive web application that visualizes the accessibility of curb ramps in San Francisco. This tool highlights missing and poorly maintained ramps to raise awareness about accessibility issues. Users can search by location, view ramp conditions, and interact with an informative map.

Designed for policymakers, advocates, and the community to encourage inclusive infrastructure development.

Built using **Flask**, **Folium**, **Pandas**, and **HTML/CSS**.

---

## Features
- **Search for curb ramps** by location using an interactive search tool.
- View ramp conditions (e.g., missing ramps, poorly maintained ramps) on a **map with visual markers**.
- Access an **About page** and **Legend page** for additional project context.

---

## Project Structure

```plaintext
project-folder/
├── app.py                 # Backend: Flask application
├── utils.py               # Backend: Utility functions
├── templates/             # Frontend: HTML files
│   ├── index.html         # Homepage
│   ├── search.html        # Search functionality
│   ├── about.html         # About the project
│   ├── legend.html        # Map legend
├── static/                # Frontend: Static assets
│   ├── css/
│   │   ├── style.css      # Main styles for the application
│   ├── images/
│       ├── logo.png       # Project logo
│       ├── streetsf.jpeg  # Image used in the "About" page
├── Curb_Ramps.csv         # Backend: Dataset
├── requirements.txt       # Backend: Dependencies
├── README.md              # Documentation

