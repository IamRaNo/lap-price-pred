import math
import pickle
import pandas as pd
import streamlit as st

# Load model and data
model = pickle.load(open('model.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))

# Title and description
st.title('💻 Laptop Price Predictor')
st.markdown("Predict laptop prices based on technical specifications.")

# Input layout
st.header("📝 Enter Specifications")

col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('Brand', data['company'].unique())
    typeName = st.selectbox('Laptop Type', data['typename'].unique())
    ram = st.selectbox('RAM (GB)', sorted(data['ram'].unique()))
    os = st.selectbox('Operating System', data['os'].unique())
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, step=0.1)
    cpu_type = st.selectbox('CPU Type', data['cpu_type'].unique())
    cpu_brand = st.selectbox('CPU Brand', data['cpu_brand'].unique())
    cpu_speed = st.number_input('CPU Speed (GHz)', min_value=0.5, max_value=5.0, step=0.1)

with col2:
    uhd_display = st.selectbox('4K Display', ['Yes', 'No'])
    prm_mem = st.selectbox('Primary Memory Type', data['primary_memory_type'].unique())
    prm_mem_size = st.selectbox('Primary Memory Size (GB)', sorted(data['primary_memory_capacity'].unique()))
    sec_mem = st.selectbox('Secondary Memory Type', data['secondary_memory_type'].unique())
    sec_mem_size = st.selectbox('Secondary Memory Size (GB)', sorted(data['secondary_memory_capacity'].unique()))
    gpu = st.selectbox('GPU Brand', data['gpu_brand'].unique())

st.subheader("📺 Display Details")
screen_size = st.number_input('Screen Size (inches)', min_value=10.0, max_value=20.0, step=0.1)
width_resolution = st.number_input('Screen Width (px)', min_value=800)
height_resolution = st.number_input('Screen Height (px)', min_value=600)

# Predict button
if st.button('🔮 Predict Price'):
    # Convert 4K display to binary
    uhd_display = int(uhd_display == 'Yes')

    # Validate screen size
    if screen_size == 0:
        st.error("Screen size must be greater than zero.")
    else:
        # Calculate PPI
        ppi = round(math.sqrt(width_resolution ** 2 + height_resolution ** 2) / screen_size, 2)

        # Input data
        input_df = pd.DataFrame([{
            'company': company,
            'typename': typeName,
            'ram': ram,
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

        # Predict price
        predicted_log_price = model.predict(input_df)[0]
        predicted_price = round(math.exp(predicted_log_price), 2)

        # Output
        st.success(f"🎯 **Estimated Laptop Price: ₹{predicted_price}**")

