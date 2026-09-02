
import streamlit as st 
import httpx 
import pandas as pd


BASE_URL = "http://127.0.0.1:8000" 

def main(): 
    st.markdown("## EclipseBord")
    st.write("Explore solar and lunar eclipse data.")

    solar_data = httpx.get(f"{BASE_URL}/solar", timeout=30).json() 
    lunar_data = httpx.get(f"{BASE_URL}/lunar", timeout=30).json() 

    
    solar_df = pd.DataFrame(solar_data) # Convert eclipse data to DataFrames
    lunar_df = pd.DataFrame(lunar_data) 


    # Add eclipse record metrics
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Number of solar eclipse records", len(solar_data))

    with col2:
        st.metric("Number of lunar eclipse records", len(lunar_data))


    # Add tabs for solar and lunar eclipse data
    solar_tab, lunar_tab = st.tabs(
    ["☀️ Solar Eclipses", "🌙 Lunar Eclipses"]
    )
    
    with solar_tab:
        st.dataframe(solar_data)

    with lunar_tab:
        st.dataframe(lunar_data)

    

    # Add solar eclipse types chart:
    solar_types = solar_df["Eclipse Type"].value_counts()
    st.subheader("Solar Eclipse Types")
    st.bar_chart(solar_types)

    # Add lunar eclipse types chart:
    lunar_types = lunar_df["Eclipse Type"].value_counts()
    st.subheader("Lunar Eclipse Types")
    st.bar_chart(lunar_types)

if __name__ == "__main__": 
    main()