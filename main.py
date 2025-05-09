import math
import pickle
import pandas as pd
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))
st.title('Laptop Price Predictor')

company = st.selectbox('Company', data['company'].unique())
typeName = st.selectbox('Type', data['typename'].unique())
ram = int(st.selectbox('Ram(In GB)', (data['ram'].unique())))
os = st.selectbox('OS', data['os'].unique())
weight = st.number_input('weight')
fhd_display = st.selectbox('Full HD', ['Yes', 'No'])
ips_display = st.selectbox('IPS Panel', ['Yes', 'No'])
touchscreen_display = st.selectbox('Touch Screen', ['Yes', 'No'])
uhd_display = st.selectbox('4k Display', ['Yes', 'No'])
cpu_type = st.selectbox('CPU Type', data['cpu_type'].unique())
cpu_brand = st.selectbox('CPU Brand', data['cpu_brand'].unique())
cpu_speed = st.number_input('CPU Speed')
prm_mem = st.selectbox('Primary Memory Type', data['primary_memory_type'].unique())
prm_mem_size = st.selectbox('Primary Memory Size', data['primary_memory_capacity'].unique())
sec_mem = st.selectbox('Secondary Memory Type', data['secondary_memory_type'].unique())
sec_mem_size = st.selectbox('Secondary Memory Size', data['secondary_memory_capacity'].unique())
screen_size = st.number_input('Screen Size In Inches')
width_resolution = st.number_input('Width Resolution')
height_resolution = st.number_input('Height Resolution')
gpu = st.selectbox('GPU', data['gpu_brand'].unique())
if st.button('Predict Price'):
    # Convert display options to binary
    fhd_display = 1 if fhd_display == 'Yes' else 0
    ips_display = 1 if ips_display == 'Yes' else 0
    uhd_display = 1 if uhd_display == 'Yes' else 0
    touchscreen_display = 1 if touchscreen_display == 'Yes' else 0

    # Calculate PPI
    try:
        ppi = round(math.sqrt(width_resolution ** 2 + height_resolution ** 2) / screen_size, 2)
    except ZeroDivisionError:
        st.error("Screen size must be greater than zero.")
        ppi = 0

    # Build DataFrame with correct column names
    input_df = pd.DataFrame([{
        'company': company,
        'typename': typeName,
        'ram': ram,
        'full_hd': fhd_display,
        'ips_panel': ips_display,
        'touchscreen': touchscreen_display,
        '4k_display': uhd_display,
        'cpu_type': cpu_type,
        'cpu_speed': cpu_speed,
        'cpu_brand': cpu_brand,
        'primary_memory_type': prm_mem,
        'primary_memory_capacity': prm_mem_size,
        'secondary_memory_type': sec_mem,
        'secondary_memory_capacity': sec_mem_size,
        'gpu_brand': gpu,
        'os': os,
        'weight': weight,
        'ppi': ppi
    }])

    # Predict and display result
    predicted_log_price = model.predict(input_df)[0]
    predicted_price = round(math.exp(predicted_log_price), 2)
    st.title(f"Predicted Laptop Price: ₹{predicted_price}")
