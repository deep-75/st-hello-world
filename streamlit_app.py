import streamlit as st
import pandas as pd

st.title("Timelytics: Delivery Time Predictor")

st.markdown("Provide order details below to get an estimated delivery time:")

# User Inputs
product_category = st.selectbox("Product Category", ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty'])
customer_location = st.selectbox("Customer Location", ['New York', 'California', 'Texas', 'Florida', 'Illinois'])
shipping_method = st.selectbox("Shipping Method", ['Standard', 'Express', 'Same Day'])

def predict_delivery_time(category, location, shipping):
    # Dummy rule-based prediction logic
    base_time = {
        'Standard': 5,
        'Express': 3,
        'Same Day': 1
    }.get(shipping, 5)
    
    # Adjust based on category
    if category in ['Electronics', 'Home & Kitchen']:
        base_time += 1
    elif category == 'Books':
        base_time -= 1

    # Adjust based on location (mock logic)
    if location in ['California', 'Texas']:
        base_time += 0.5
    elif location == 'New York':
        base_time -= 0.5

    return max(1, round(base_time, 1))

if st.button("Predict Delivery Time"):
    prediction = predict_delivery_time(product_category, customer_location, shipping_method)
    st.success(f"📦 Estimated Delivery Time: **{prediction} days**")
