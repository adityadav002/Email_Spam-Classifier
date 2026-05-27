import pickle
import string
import nltk

from flask import Flask, request, render_template
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

def transform_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalnum()]
    words = [
        word for word in words
        if word not in stop_words
        and word not in string.punctuation
    ]
    words = [ps.stem(word) for word in words]
    return " ".join(words)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]
    transformed_message = transform_text(message)
    vector_input = tfidf.transform([transformed_message])
    prediction = model.predict(vector_input)[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return render_template(
        "index.html",
        prediction=result,
        message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)