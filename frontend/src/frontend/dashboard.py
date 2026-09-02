
import streamlit as st 
import httpx 



BASE_URL = "http://127.0.0.1:8000" 

def main(): 
    st.markdown("# EclipseBord") 

    solar_data = httpx.get(f"{BASE_URL}/solar", timeout=30).json() 
    lunar_data = httpx.get(f"{BASE_URL}/lunar", timeout=30).json() 

    st.dataframe(solar_data) 
    st.dataframe(lunar_data) 


if __name__ == "__main__": 
    main()