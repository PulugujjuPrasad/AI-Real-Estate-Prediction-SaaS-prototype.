import os
from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import plotly.express as px

st.set_page_config(
    page_title="Real Estate Prediction SaaS",
    page_icon="🏡",
    layout="wide",
)

BANNER_IMAGE = "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80"
SAMPLE_DATA_PATH = Path("data/sample_properties.csv")

@st.cache_data(show_spinner=False)
def read_data(source_file=None, custom_path=None):
    if source_file is not None:
        return _load_dataframe(source_file)

    if custom_path:
        try:
            return _load_dataframe(custom_path)
        except Exception:
            pass

    if SAMPLE_DATA_PATH.exists():
        return pd.read_csv(SAMPLE_DATA_PATH)

    return pd.DataFrame()


def _load_dataframe(source):
    if isinstance(source, (str, Path)):
        path = Path(source)
        if path.suffix.lower() == ".csv":
            return pd.read_csv(path)
        return pd.read_excel(path, engine="openpyxl")

    filename = getattr(source, "name", "upload")
    if str(filename).lower().endswith(".csv"):
        return pd.read_csv(source)
    return pd.read_excel(source, engine="openpyxl")


def find_target_column(df):
    candidates = [c for c in df.columns if any(k in c.lower() for k in ["price", "sale", "value", "amount"])]
    return candidates[0] if candidates else None


def find_column(df, candidates):
    for name in candidates:
        if name in df.columns:
            return name
    return None


def format_currency(value):
    return f"${value:,.0f}"


def get_property_image(property_type: str):
    key = str(property_type).lower()
    if "condo" in key or "apartment" in key:
        return "https://images.unsplash.com/photo-1560185127-6fd5a25959ef?auto=format&fit=crop&w=900&q=80"
    if "town" in key:
        return "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=900&q=80"
    return "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=900&q=80"


def render_property_cards(df):
    if df.empty:
        st.write("No properties found for the selected filters.")
        return

    cols = st.columns(3)
    for index, row in df.iterrows():
        col = cols[index % 3]
        image_url = get_property_image(row.get("Property Type", row.get("PropertyType", "house")))
        with col:
            st.image(image_url, use_column_width=True)
            st.markdown(f"### {row.get('Neighborhood', row.get('City', 'Property'))}")
            st.markdown(f"**Type:** {row.get('Property Type', row.get('PropertyType', 'Residential'))}")
            st.markdown(f"**Bedrooms:** {row.get('Bedrooms', row.get('Beds', 'N/A'))} | **Bathrooms:** {row.get('Bathrooms', row.get('Baths', 'N/A'))}")
            sqft = row.get('Area', row.get('SquareFeet', row.get('Sqft', 'N/A')))
            st.markdown(f"**Area:** {sqft} sqft")
            price = row.get('SalePrice') or row.get('Price') or row.get('Value')
            if pd.notna(price):
                st.markdown(f"**Price:** {format_currency(price)}")
            st.markdown("---")


@st.cache_data(show_spinner=False)
def build_model(df, target):
    df = df.copy()
    df = df.dropna(subset=[target])
    y = df[target]

    features = df.drop(columns=[target])
    numeric_cols = features.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = features.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    if not numeric_cols:
        return None, None, None, None, None

    X = features[numeric_cols + categorical_cols].fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", StandardScaler(), numeric_cols),
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ],
        remainder="drop",
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
        ]
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    metrics = {
        "MAE": mean_absolute_error(y_test, y_pred),
        "R2": r2_score(y_test, y_pred),
    }

    return model, numeric_cols, categorical_cols, metrics, df


def create_prediction_form(model, numeric_cols, categorical_cols, df_sample):
    if model is None:
        st.warning("The dataset does not contain enough data for an automated regression model.")
        return

    st.subheader("Predict a Property Value")
    input_values = {}

    with st.form(key="prediction_form"):
        for feature in numeric_cols:
            min_val = int(df_sample[feature].min()) if pd.api.types.is_numeric_dtype(df_sample[feature]) else 0
            max_val = int(df_sample[feature].max()) if pd.api.types.is_numeric_dtype(df_sample[feature]) else 100
            step = max(1, (max_val - min_val) // 10)
            input_values[feature] = st.slider(feature, min_val, max_val, int((min_val + max_val) / 2), step=step)

        for feature in categorical_cols:
            values = df_sample[feature].dropna().unique().tolist()[:10]
            if values:
                input_values[feature] = st.selectbox(feature, values)

        submit = st.form_submit_button("Run Prediction")

    if submit:
        row = pd.DataFrame([input_values])
        prediction = model.predict(row)[0]
        st.success(f"Predicted property value: {format_currency(prediction)}")


def main():
    st.image(BANNER_IMAGE, use_column_width=True)
    st.title("Real Estate Price Prediction Studio")
    st.markdown(
        "### Build a beautiful property insights dashboard with uploadable market data, interactive filtering, and fast value predictions."
    )

    with st.sidebar:
        st.header("Data and filters")
        data_source = st.radio("Load dataset", ["Upload file", "Use sample data", "Enter local path"])

        uploaded_file = None
        custom_path = None
        if data_source == "Upload file":
            uploaded_file = st.file_uploader("Upload Excel or CSV", type=["xlsx", "xls", "csv"])
        elif data_source == "Enter local path":
            custom_path = st.text_input("Local path to dataset", value=str(Path.cwd() / "data/Case Study 1 Data (1) (1).xlsx"))

        if st.checkbox("Show help text", value=False):
            st.markdown(
                "Upload an Excel or CSV data file from the case study. If you are running in Codespaces, upload via the file uploader or place the file in the `data/` folder."
            )

    df = read_data(source_file=uploaded_file, custom_path=custom_path)

    if df.empty:
        st.warning(
            "No dataset loaded. Use the sidebar to upload a file, enter a local path, or use the sample dataset."
        )
        return

    target_column = find_target_column(df)
    if target_column:
        st.success(f"Detected target column: **{target_column}**")
    else:
        st.info("No obvious target column detected. Prediction features will be limited until you upload labeled price data.")

    property_type_col = find_column(df, ["Property Type", "PropertyType", "Type"])
    city_col = find_column(df, ["City"])
    neighborhood_col = find_column(df, ["Neighborhood", "Neighbourhood"])
    bedrooms_col = find_column(df, ["Bedrooms", "Beds"])
    area_col = find_column(df, ["Area", "SquareFeet", "Sqft"])
    year_built_col = find_column(df, ["Year Built", "YearBuilt", "Built Year", "Year"])
    lot_size_col = find_column(df, ["Lot Size", "LotSize"])
    sale_price_col = target_column or find_column(df, ["SalePrice", "Price", "Value"])

    st.markdown("## Filter properties")
    st.write(f"Loaded dataset with **{df.shape[0]} rows** and **{df.shape[1]} columns**.")

    filters = {}
    if city_col:
        filters[city_col] = st.multiselect(city_col, sorted(df[city_col].dropna().unique()), default=sorted(df[city_col].dropna().unique()))
    if neighborhood_col:
        filters[neighborhood_col] = st.multiselect(neighborhood_col, sorted(df[neighborhood_col].dropna().unique()), default=sorted(df[neighborhood_col].dropna().unique()))
    if property_type_col:
        filters[property_type_col] = st.multiselect(property_type_col, sorted(df[property_type_col].dropna().unique()), default=sorted(df[property_type_col].dropna().unique()))

    if bedrooms_col and pd.api.types.is_numeric_dtype(df[bedrooms_col]):
        min_bed, max_bed = int(df[bedrooms_col].min()), int(df[bedrooms_col].max())
        filters[bedrooms_col] = st.slider(bedrooms_col, min_bed, max_bed, (min_bed, max_bed))
    if area_col and pd.api.types.is_numeric_dtype(df[area_col]):
        min_area, max_area = int(df[area_col].min()), int(df[area_col].max())
        filters[area_col] = st.slider(area_col, min_area, max_area, (min_area, max_area))
    if year_built_col and pd.api.types.is_numeric_dtype(df[year_built_col]):
        min_year, max_year = int(df[year_built_col].min()), int(df[year_built_col].max())
        filters[year_built_col] = st.slider(year_built_col, min_year, max_year, (min_year, max_year))
    if lot_size_col and pd.api.types.is_numeric_dtype(df[lot_size_col]):
        min_lot, max_lot = float(df[lot_size_col].min()), float(df[lot_size_col].max())
        filters[lot_size_col] = st.slider(lot_size_col, float(min_lot), float(max_lot), (float(min_lot), float(max_lot)))
    if sale_price_col and pd.api.types.is_numeric_dtype(df[sale_price_col]):
        min_price, max_price = int(df[sale_price_col].min()), int(df[sale_price_col].max())
        filters[sale_price_col] = st.slider(sale_price_col, min_price, max_price, (min_price, max_price), step=max(1, (max_price - min_price) // 20))

    filtered_df = df.copy()
    for key, value in filters.items():
        if isinstance(value, tuple):
            filtered_df = filtered_df[filtered_df[key].between(value[0], value[1])]
        elif isinstance(value, list) and value:
            filtered_df = filtered_df[filtered_df[key].isin(value)]

    st.markdown("---")
    st.header("Filtered results")
    st.write(f"Showing **{filtered_df.shape[0]}** rows after filter selection.")
    if filtered_df.empty:
        st.warning("No matching properties found with the selected filters.")
    else:
        render_property_cards(filtered_df.head(12))
        st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

    st.markdown("---")

    if target_column:
        model, numeric_cols, categorical_cols, metrics, train_df = build_model(df, target_column)
        if model is not None:
            st.header("Prediction engine")
            st.markdown(
                "Train a local regression model and test property value predictions with the dataset features."
            )
            st.metric("Model R²", round(metrics["R2"], 3))
            st.metric("Mean absolute error", format_currency(metrics["MAE"]))
            create_prediction_form(model, numeric_cols, categorical_cols, train_df)
        else:
            st.warning("Unable to build a model because the dataset does not contain enough numeric features.")

    st.sidebar.markdown("---")
    st.sidebar.markdown("## About this prototype")
    st.sidebar.markdown(
        "This demo is a Streamlit-based prototype designed for property market analysis, filterable property cards, and simple price predictions."
    )

    if st.button("Show app instructions"):
        st.info(
            "Use the sidebar to upload or load data, preview the dataset, filter properties, and run prediction tests." 
        )

if __name__ == "__main__":
    main()
