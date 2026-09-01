import pandas as pd
from backend.constants import DATA_PATH

solar_df = pd.read_csv(DATA_PATH / "solar.csv")
lunar_df = pd.read_csv(DATA_PATH / "lunar.csv")

solar_df["Path Width (km)"] = solar_df["Path Width (km)"].fillna("missing")
solar_df["Central Duration"] = solar_df["Central Duration"].fillna("missing")
