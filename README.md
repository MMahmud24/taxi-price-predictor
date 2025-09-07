#NYC Taxi Fare & Demand Prediction (In Progress)

<p>
This project is a work-in-progress web application that predicts NYC taxi fares and identifies ride demand hotspots using a combination of data engineering pipelines, machine learning models, and full-stack integration.
</p>

<h2>Current Features</h2>
<ul>
  <li><b>Data Engineering Pipelines</b>: Python scripts for cleaning and preprocessing 5M+ NYC TLC taxi trip records.</li>
  <li><b>Feature Enrichment</b>: Integration of the OpenRouteService API for trip distance, as well as weather and event data for contextual insights.</li>
  <li><b>Machine Learning</b>: Gradient Boosting model trained on engineered features, currently achieving an R² of ~0.80 on validation data.</li>
  <li><b>Modular Script Design</b>: Individual scripts for distance calculation, feature building, model training, and live predictions (<code>calculate_distance.py</code>, <code>build_live_features.py</code>, <code>train_model.py</code>, <code>predict.py</code>).</li>
  <li><b>Backend API (Express + Python Bridge)</b>: Node.js/Express server that routes requests to Python scripts for real-time predictions.</li>
  <li><b>Frontend (React + Tailwind)</b>: Early-stage UI where users input pickup and dropoff locations to view predicted fares.</li>
</ul>

<h2>Tech Stack</h2>
<ul>
  <li><b>Frontend</b>: React, TailwindCSS</li>
  <li><b>Backend</b>: Express (Node.js) with Python child processes</li>
  <li><b>Machine Learning</b>: Python (pandas, scikit-learn, joblib)</li>
  <li><b>Data Sources</b>: NYC TLC trip data, weather APIs, event feeds, OpenRouteService</li>
</ul>

<h2>Roadmap (In Progress)</h2>
<ul>
  <li>Improve feature engineering with richer weather and event integration</li>
  <li>Expand ML pipeline to include demand hotspot clustering (K-means)</li>
  <li>Add interactive maps (Leaflet/Google Maps) for visualizing routes and hotspots</li>
  <li>Deploy backend and frontend to cloud platforms (Render + Vercel/Netlify)</li>
</ul>