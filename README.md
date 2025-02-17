# 🍉 Watermelon Leaf Disease Prediction

## 📌 Overview
This project is a deep learning-based **Watermelon Leaf Disease Prediction** system built using **Streamlit** for the web interface. The application allows users to upload images of watermelon leaves, and it predicts whether the leaf is **Healthy** or affected by one of the diseases (**Anthracnose, Downy Mildew, Mosaic Virus**). The model also provides detailed symptoms, treatment recommendations, and additional agricultural tips.

## 🚀 Features
- **Upload an image** of a watermelon leaf for disease prediction.
- **Deep learning model (CNN + Transfer Learning)** predicts the disease.
- **Displays symptoms & treatments** for diseased leaves.
- **Provides healthy growth tips** for watermelon plants.
- **Shows additional agricultural tips** for prevention, environment, and cultural practices.

## 🧠 Model Training Details
The model was trained using a **Convolutional Neural Network (CNN)** with additional **Transfer Learning** techniques, including:
- **ResNet**
- **VGG**
- **EfficientNet**
- **MobileNet**

After experimentation, the **CNN model with BatchNormalization and Dropout layers** performed the best and was chosen for deployment in the Streamlit web application.

### 🔄 Data Preprocessing & Balancing
- Used **data augmentation** to increase dataset diversity.
- Applied **data balancing** with `sklearn.utils.resample` to address class imbalance.

### ⚡ Training Optimizations
- **BatchNormalization** to stabilize training.
- **Dropout** for reducing overfitting.
- **Callbacks Used:**
  - **ReduceLROnPlateau**: Automatically reduces learning rate when validation loss stagnates.
  - **EarlyStopping**: Stops training early if validation loss does not improve.

## 📁 Project Structure
```
📦 Watermelon-Crop-Disease-Prediction
├── model/
│   ├── cnn_model.h5  # Trained CNN model
├── assets/
│   ├── data/
│   │   ├── anthracnose_data.json
│   │   ├── downy_mildew_data.json
│   │   ├── mosaic_virus_data.json
│   │   ├── healthy_data.json
│   │   ├── additional_tips_data.json
├── app.py  # Streamlit application
├── requirements.txt  # Required dependencies
├── README.md  # Documentation
```

## 📥 Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/AishwariyaSK/Water-Melon-Crop-Disease-Prediction-DL-.git
   cd Water-Melon-Crop-Disease-Prediction-DL-
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```sh
   streamlit run app.py
   ```

## 📜 Dependencies (requirements.txt)
```
streamlit
numpy
p
Pillow
tensorflow
```

## 🎯 Usage
- Upload a watermelon leaf image.
- Click **Predict** to get disease classification.
- View symptoms, treatments, and additional tips.

## 💡 Future Improvements
- Adding more diseases for classification.
- Improving accuracy with advanced architectures.
- Deploying as a cloud-based API.

---
📌 Developed with ❤️ by **AishwariyaSK** 🚀

