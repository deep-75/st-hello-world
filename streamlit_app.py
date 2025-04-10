import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("delivery_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load any encoders or transformers if necessary
with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Streamlit UI
st.title("Timelytics: Delivery Time Predictor")

st.markdown("Fill in the order details below to get a predicted delivery time:")

# User Inputs
product_category = st.selectbox("Product Category", ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty'])
customer_location = st.selectbox("Customer Location", ['New York', 'California', 'Texas', 'Florida', 'Illinois'])
shipping_method = st.selectbox("Shipping Method", ['Standard', 'Express', 'Same Day'])

if st.button("Predict Delivery Time"):
    # Create DataFrame from input
    input_df = pd.DataFrame({
        'Product_Category': [product_category],
        'Customer_Location': [customer_location],
        'Shipping_Method': [shipping_method]
    })

    # Encode inputs if needed
    input_encoded = encoder.transform(input_df)

    # Make prediction
    prediction = model.predict(input_encoded)[0]

    # Display result
    st.success(f"📦 Estimated Delivery Time: **{prediction:.2f} days**")
