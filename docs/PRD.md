# Product Requirements Document (PRD)

## Project Name
AI Real Estate Prediction SaaS Prototype

## Vision
Create a lightweight web prototype that turns real estate market data into visual property intelligence and automated price estimates. The prototype should make it easy for property professionals and analysts to test datasets, view filtered listings, and validate model outputs.

## Target Users
- Real estate agents
- Property investors
- Market analysts
- Product managers validating data-driven property tools

## Business Goals
- Demonstrate a working data-driven real estate MVP
- Enable rapid dataset testing without engineering overhead
- Provide immediate visual feedback for property listings
- Show how price labels can power predictive analytics

## Scope
### Must-have Features
- Upload `.csv`, `.xlsx`, and `.xls` datasets via a browser UI
- Load a built-in sample dataset for demo mode
- Display properties in a card-based list with remote imagery
- Provide simple filters for city, neighborhood, property type, bedrooms, area, and price
- Detect a price-related target column automatically
- Train a local regression model and show MAE / R² metrics
- Expose prediction inputs and display predicted property values
- Include product documentation in `docs/`

### Nice-to-have Features
- Visualize dataset summary charts and key metrics
- Support more intelligent column mapping for custom datasets
- Add geolocation or map-based views
- Improve image selection with user-provided photos

## Functional Requirements
- Streamlit front-end with sidebar controls
- Data loader that accepts uploaded files and local paths
- Dataset preview and filter controls for key property fields
- Price prediction engine with a regression model
- Model evaluation output visible to users

## Non-functional Requirements
- Run reliably in GitHub Codespaces
- Start quickly and display a useful fallback dataset
- Keep code simple and modular for future extension
- Provide clear README, PRD, BRD, and Q&A documentation

## Acceptance Criteria
- A user can open the app and load the sample data successfully
- The app displays property cards and filters based on available columns
- The model trains when a price column exists and shows metrics
- The README and docs accurately describe how to run the project
