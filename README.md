# Email Spam Classifier

A Machine Learning based Email Spam Classifier built using Flask, Scikit-learn, and NLP techniques.  
This project detects whether an email/message is **Spam** or **Not Spam** using a trained ML model.

---

# Features

- Spam Detection using Machine Learning
- NLP Text Preprocessing
- TF-IDF Vectorization
- Flask Web Application
- Modern Black & White UI
- Real-time Prediction
- Lightweight and Fast

---

# Tech Stack

- Python
- Flask
- Scikit-learn
- NLTK
- HTML
- CSS

---

# Project Structure

```bash
EMAIL_SPAM_CLASSIFIER/
│
├── templates/
│   └── index.html
│
├── static/
│   └── logo.png
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
└── spam.csv
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/adityadav002/Email_Spam-Classifier.git
```

## 2. Move Into Project Folder

```bash
cd Email_Spam-Classifier
```

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\Activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python app.py
```

---

# Open In Browser

```bash
http://127.0.0.1:5000
```

---

# How It Works

1. User enters an email/message.
2. Text preprocessing is applied:
   - Lowercasing
   - Tokenization
   - Stopword removal
   - Stemming
3. TF-IDF converts text into vectors.
4. Machine Learning model predicts:
   - Spam
   - Not Spam

---

# Example Spam Message

```text
Congratulations! You have won a free iPhone. Click here to claim your reward.
```

# Example Not Spam Message

```text
Hey Aditya, are we meeting tomorrow for the project discussion?
```

---

# Deployment

This project can be deployed on:

- Render
- Railway
- PythonAnywhere
- Heroku

---

# Quick Start

```bash
git clone https://github.com/adityadav002/Email_Spam-Classifier.git

cd Email_Spam-Classifier

python -m venv .venv

.venv\Scripts\Activate

pip install -r requirements.txt

python app.py
```

---

# Author

Aditya Yadav

---

# License

This project is open source and available under the MIT License.
