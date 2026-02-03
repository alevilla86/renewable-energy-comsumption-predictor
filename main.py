import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from ml_model_data_cleanup import load_data, get_locations, get_location_data
from ml_model_config import train_model, predict

DATA_PATH = "raw_data/renewable_energy.csv"

st.title("Renewable Energy Consumption Predictor")
st.write("Predict future renewable energy consumption by country using linear regression.")

# Load data
@st.cache_data
def get_data():
    return load_data(DATA_PATH)

df = get_data()
locations = get_locations(df)

# UI Controls
col1, col2 = st.columns(2)
with col1:
    selected_location = st.selectbox("Select Location", locations)
with col2:
    years_to_predict = st.number_input("Years to Predict", min_value=1, max_value=20, value=5)

# Get location data
location_data = get_location_data(df, selected_location)

if len(location_data) < 2:
    st.warning("Not enough data for this location to make predictions.")
else:
    # Train model
    X = location_data["TIME"].values
    y = location_data["Value"].values
    model = train_model(X, y)

    # Generate predictions
    last_year = int(X.max())
    future_years = np.arange(last_year + 1, last_year + years_to_predict + 1)
    predictions = predict(model, future_years)

    # Create prediction dataframe
    prediction_df = pd.DataFrame({
        "Year": future_years,
        "Predicted Value (KTOE)": predictions.round(2)
    })

    # Create combined data for chart
    historical_df = pd.DataFrame({
        "Year": X,
        "Value": y,
        "Type": "Historical"
    })
    future_df = pd.DataFrame({
        "Year": future_years,
        "Value": predictions,
        "Type": "Predicted"
    })
    chart_data = pd.concat([historical_df, future_df], ignore_index=True)

    # Display chart
    st.subheader(f"Renewable Energy Consumption: {selected_location}")
    chart = alt.Chart(chart_data).mark_line(point=True).encode(
        x=alt.X("Year:O", title="Year"),
        y=alt.Y("Value:Q", title="Value (KTOE)"),
        color=alt.Color("Type:N", legend=alt.Legend(title="Data Type"))
    ).properties(height=400)
    st.altair_chart(chart, use_container_width=True)

    # Display predictions table
    st.subheader("Predictions")
    st.dataframe(prediction_df, hide_index=True)

    # Model info
    with st.expander("Model Details"):
        st.write(f"**Training data points:** {len(X)}")
        st.write(f"**Year range:** {int(X.min())} - {int(X.max())}")
        st.write(f"**Model coefficient (slope):** {model.coef_[0]:.2f} KTOE/year")
        st.write(f"**Model intercept:** {model.intercept_:.2f}")
