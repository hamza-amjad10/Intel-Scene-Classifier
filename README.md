# 🏔️ Intel Scene Classifier

A deep learning web app that classifies natural and urban scene images into **6 categories** using a fine-tuned **ResNet50** model, served via **FastAPI** and visualized through a **Streamlit** frontend.

---

## 🎯 Categories

| Label | Scene |
|-------|-------|
| 0 | Buildings |
| 1 | Forest |
| 2 | Glacier |
| 3 | Mountain |
| 4 | Sea |
| 5 | Street |

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Test Accuracy | **77.97%** |
| Macro F1-Score | **0.78** |
| Training Epochs | 25 (early stopping at best: Epoch 20) |

### Per-Class F1 Scores
```
buildings  → 0.79
forest     → 0.93  ✅ Best
glacier    → 0.71
mountain   → 0.71
sea        → 0.73
street     → 0.83
```

---

## 🏗️ Architecture

```
ResNet50 (pretrained, ImageNet)
    ↓
GlobalAveragePooling2D
    ↓
Dense(128, relu)
    ↓
Dropout
    ↓
Dense(6, softmax)
```

- **Total params:** ~23.8M  
- **Trainable params:** ~4.7M (top layers only — transfer learning)
- **Input size:** 224×224 RGB

---

## 🗂️ Project Structure

```
CNN_Inet/
├── Intel_model_code.ipynb   # Training notebook (Colab)
├── requirements.txt         # Dependencies
└── web_app/
    ├── backend.py           # FastAPI app
    └── frontend.py          # Streamlit app
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/hamza-amjad10/Intel-Scene-Classifier.git

```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
```bash
kaggle datasets download -d puneet6060/intel-image-classification
```

---

## ⚙️ Running the App

### Backend (FastAPI + ngrok)
Run the last cell of `Intel_model_code.ipynb` in **Google Colab**.  
It will print a public ngrok URL like:
```
Public URL: https://xxxx-xx-xxx-xxx-xxx.ngrok-free.app
```

Copy that URL and paste it into `frontend.py` as `api_url`.

### Frontend (Streamlit)
```bash
streamlit run web_app/frontend.py
```

Then open your browser at `http://localhost:8501`.

---

## 🖼️ How It Works

1. User uploads a `.jpg` / `.jpeg` / `.png` image via Streamlit UI
2. Streamlit sends the image to the FastAPI `/predict` endpoint
3. FastAPI preprocesses the image (resize → normalize → batch dimension)
4. ResNet50 model runs inference and returns the top class + confidence
5. Result is displayed back in the Streamlit UI

---

## 📦 Requirements

```
tensorflow
fastapi
uvicorn
pyngrok
nest_asyncio
opencv-python
streamlit
requests
numpy
```

---

## 📁 Dataset

[Intel Image Classification — Kaggle](https://www.kaggle.com/datasets/puneet6060/intel-image-classification)

- ~14,000 training images  
- ~3,000 test images  
- 6 scene categories  
- Image size: 150×150 (resized to 224×224 for ResNet50)

---

## 🧠 Training Details

- **Base model:** ResNet50 (ImageNet weights, frozen base)
- **Optimizer:** Adam
- **Loss:** Categorical Crossentropy
- **Callbacks:** EarlyStopping (restoring best weights)
- **Platform:** Google Colab (T4 GPU)

---

## 🙌 Acknowledgements

- Dataset by [puneet6060](https://www.kaggle.com/puneet6060) on Kaggle
- ResNet50 via [Keras Applications](https://keras.io/api/applications/resnet/)


## 👨‍💻 Author

Made with ❤️ by **Hamza Amjad**
