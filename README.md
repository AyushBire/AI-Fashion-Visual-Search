# AI Fashion Visual Search

## Overview

AI Fashion Visual Search is a Computer Vision and Deep Learning project that enables users to upload a clothing image and discover visually similar fashion products.

The system leverages:

* Convolutional Neural Networks (CNN)
* Deep Feature Embeddings
* FAISS Similarity Search

to provide fast and accurate fashion recommendations based on visual appearance rather than text descriptions.

---

## Features

* Upload clothing images for visual search
* Extract image features using ResNet50
* Find visually similar fashion products
* Fast image retrieval using FAISS
* Interactive web interface with Streamlit
* Real-time recommendation results
* Scalable architecture for larger fashion datasets

---

## Technologies Used

* Python
* TensorFlow / Keras
* ResNet50
* FAISS
* NumPy
* Pillow (PIL)
* Streamlit

---

## Project Structure

```text
AI-Fashion-Visual-Search/
│
├── dataset/
│   ├── shirt_1.jpg
│   ├── shirt_2.jpg
│   ├── tshirt_1.jpg
│   └── ...
│
├── feature_extractor.py
├── generate_embeddings.py
├── search.py
├── app.py
│
├── embeddings.pkl
├── image_paths.pkl
│
├── requirements.txt
└── README.md
```

---

## Dataset

The project uses a collection of fashion product images including:

* Shirts
* T-Shirts
* Jackets
* Jeans
* Shoes

Each image is converted into a high-dimensional feature vector using a pre-trained ResNet50 model.

---

## System Workflow

### 1. Feature Extraction

A pre-trained ResNet50 model is used to extract deep visual features from fashion images.

The extracted feature vector represents:

* Color
* Texture
* Shape
* Visual Patterns

---

### 2. Embedding Generation

All product images are processed and converted into feature embeddings.

Generated data is stored in:

```text
embeddings.pkl
image_paths.pkl
```

for efficient retrieval.

---

### 3. Similarity Search

FAISS (Facebook AI Similarity Search) is used to perform nearest-neighbor search on image embeddings.

The system identifies products that are visually similar to the uploaded image.

---

### 4. Recommendation Display

Users upload a clothing image through the Streamlit interface.

The system:

1. Extracts image features
2. Searches the FAISS index
3. Returns the Top-K visually similar products

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Fashion-Visual-Search.git
```

Move into the project directory:

```bash
cd AI-Fashion-Visual-Search
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Generate image embeddings:

```bash
python generate_embeddings.py
```

Run similarity search:

```bash
python search.py
```

Launch the web application:

```bash
streamlit run app.py
```

---

## Example Workflow

1. Upload a clothing image.
2. Extract image embeddings using ResNet50.
3. Search similar products using FAISS.
4. Display Top 5 visually similar fashion items.
5. Explore recommendations instantly.

---

## Future Improvements

* Fashion Category Classification
* Personalized User Recommendations
* FastAPI Backend Integration
* Advanced Vision Transformer Models (ViT)
* Cloud Deployment
* E-commerce Platform Integration

---

## Learning Outcomes

* Computer Vision
* Deep Learning
* Transfer Learning
* Feature Extraction
* Similarity Search
* Recommendation Systems
* Streamlit Application Development
* Machine Learning Deployment

---

## Author

**Ayush Bire**

Computer Science and Engineering (AI & ML)

G.H. Raisoni College of Engineering, Nagpur
