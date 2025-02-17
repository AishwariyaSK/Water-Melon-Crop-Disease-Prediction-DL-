import streamlit as st
import numpy as np
import json
from PIL import Image
import tensorflow as tf

# Load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model/cnn_model.h5")  # Fixed path

model = load_model()

# Define class labels
class_labels = ["Anthracnose", "Downy Mildew", "Healthy", "Mosaic Virus"]  # Your labels

# Load JSON data
def load_json_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Load additional tips for all diseases
additional_tips = load_json_data("assets/data/additional_tips_data.json")

# Map diseases to their respective JSON data files
disease_data_files = {
    "Anthracnose": "assets/data/anthracnose_data.json",
    "Downy Mildew": "assets/data/downy_mildew_data.json",
    "Mosaic Virus": "assets/data/mosaic_virus_data.json",
    "Healthy": "assets/data/healthy_data.json"
}

def preprocess_image(image):
    image = image.convert("RGB")  # Convert to RGB (3 channels)
    image = image.resize((128, 128))  # Resize to match model input size
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit UI
st.title("🍉 Watermelon Leaf Disease Prediction")
st.write("Upload an image of a watermelon leaf to predict its disease.")

uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = class_labels[np.argmax(prediction)]

        st.success(f"🧑‍🌾 Predicted Disease: **{predicted_class}**")

        # Load disease-specific JSON data
        disease_data = load_json_data(disease_data_files[predicted_class])

        # Display symptoms & treatment for diseased plants
        if predicted_class != "Healthy":
            st.subheader("🦠 Symptoms:")
            for symptom in disease_data["symptoms"]:
                st.write(f"- {symptom}")

            st.subheader("🛠 Treatment:")
            for treatment in disease_data["treatment"]:
                st.write(f"- {treatment}")

        # Display growing tips for healthy plants
        if predicted_class == "Healthy":
            st.subheader("🌱 Tips for Growing Healthy Watermelons:")
            for tip in disease_data["tips_for_growing_healthy_watermelon"]:
                st.write(f"- {tip}")

        # Display additional tips for all cases
        st.subheader("📢 Additional Tips:")
        st.write("### Prevention Tips:")
        for tip in additional_tips["prevention_tips"]:
            st.write(f"- {tip}")

        st.write("### Environmental Conditions:")
        for condition in additional_tips["environmental_conditions"]:
            st.write(f"- {condition}")

        st.write("### Cultural Practices:")
        for practice in additional_tips["cultural_practices"]:
            st.write(f"- {practice}")

        st.write("### Impact of Diseases:")
        for impact in additional_tips["impact"]:
            st.write(f"- {impact}")
