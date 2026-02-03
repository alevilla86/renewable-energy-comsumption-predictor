import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV data into a DataFrame."""
    return pd.read_csv(filepath)


def get_locations(df: pd.DataFrame) -> list:
    """Return sorted list of unique location codes."""
    return sorted(df["LOCATION"].unique().tolist())


def get_location_data(df: pd.DataFrame, location: str) -> pd.DataFrame:
    """Return TIME and Value columns for a specific location, excluding NaN values."""
    location_df = df[(df["LOCATION"] == location) & (df["MEASURE"] == "KTOE")][["TIME", "Value"]].copy()
    location_df = location_df.dropna(subset=["Value"])
    location_df = location_df.sort_values("TIME").reset_index(drop=True)
    return location_df
