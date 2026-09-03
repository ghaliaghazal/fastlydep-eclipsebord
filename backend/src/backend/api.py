from fastapi import FastAPI
from backend.data_processing import solar_df, lunar_df


app = FastAPI()

@app.get("/solar")
async def show_solar_data():
    return solar_df.head(30).to_dict(orient="records")

@app.get("/lunar")
async def show_lunar_data():
    return lunar_df.head(30).to_dict(orient="records")
