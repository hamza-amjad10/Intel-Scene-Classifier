import streamlit as st
import requests


st.title("Intel Image Classification Web App")
st.write("Upload an image to classify it!")

api_url="https://8cf8-35-194-180-146.ngrok-free.app/predict"




uploaded_image=st.file_uploader("Choose an image",type=["jpg","jpeg","png"])

if uploaded_image:
    st.image(uploaded_image,caption="Uploaded Image",width=300)
    
    if st.button("predict"):
      with st.spinner("Predicting...."):
        response=requests.post(url=api_url,files={"image":uploaded_image})
        result = response.json()
        st.success(f"Predicted: **{result['prediction']}**")
        st.info(f"Confidence: **{result['confidence']}%**") 


    
    























