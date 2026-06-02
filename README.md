# AI Real Estate Prediction SaaS Prototype

## Overview
This repository is a Python-based Streamlit prototype for a real estate market analytics and prediction app. It enables users to upload property datasets, explore listings visually, filter results, and generate automated price predictions using a local machine learning model.

## What’s Included
- `app.py` — main Streamlit application and UI logic
- `requirements.txt` — Python dependencies
- `.streamlit/config.toml` — Streamlit server and theme settings
- `data/sample_properties.csv` — sample dataset for demo and testing
- `docs/PRD.md` — detailed product requirements document
- `docs/BRD.md` — business requirements document
- `docs/100-q-and-a.md` — 100 Q&A reference for stakeholders and product engineering

## Key Features
- Upload `.csv`, `.xlsx`, or `.xls` datasets
- Use a built-in sample dataset for quick demo
- Preview and filter property listings
- View property cards with remote imagery
- Train a local `RandomForestRegressor` when price labels are detected
- Display model metrics (R² and MAE)
- Support for GitHub Codespaces deployment

## Screenshots
Images are not yet included in this repository. To add them, place screenshot files in `/assets/` and reference them below.

Example:
```md
![App landing page](assets/landing-page.png)
```

1. App landing page with banner and sidebar data controls
2. Property cards and filter section
3. Prediction engine panel with model metrics
4. Dataset preview and filtered results

## Setup Instructions
1. Open the repository in a Python environment.
2. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```
4. Open the browser URL shown in the terminal, typically `http://localhost:8501`.

## Running in GitHub Codespaces
- Use the Codespaces terminal to install dependencies.
- Start the app with:
```bash
python -m streamlit run app.py --server.headless true --server.port 8501
```
- Forward port `8501` in GitHub Codespaces and open the preview URL.

## Data Loading Options
### Upload via browser
- Choose `Upload file` in the sidebar.
- Upload a `.csv`, `.xlsx`, or `.xls` dataset.

### Load local dataset
- Place your dataset under the `data/` folder.
- Choose `Enter local path` and provide the file path.

## Recommended Dataset Columns
The app works best with datasets that include price and property metadata columns such as:
- `SalePrice`, `Price`, or `Value`
- `City`
- `Neighborhood`
- `Property Type`
- `Bedrooms`, `Beds`
- `Bathrooms`, `Baths`
- `Area`, `SquareFeet`, `Sqft`

## Project Organization
- `app.py` — UI, data loading, filtering, model training, and prediction flows
- `.streamlit/` — Streamlit configuration and appearance settings
- `data/` — sample dataset and any local datasets you add
- `docs/` — PRD, BRD, and project Q&A documentation

## PRD / BRD Alignment
- `docs/PRD.md` defines the product vision, user personas, key goals, and target features.
- `docs/BRD.md` captures business objectives, success metrics, and stakeholder requirements.
- The README now references both docs and provides a complete developer and user guide.

## Notes
- The current prototype does not require API keys.
- For production, add dataset validation, secure config management, and improved model explainability.

## Next Steps
- Add screenshot assets under `/assets/` and link them here
- Align dataset examples to the case-study data structure
- Expand the model training flow with cross-validation and feature selection
- Add a polished UI with custom visuals and charts
