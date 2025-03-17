from flask import Flask,request,render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import Normalizer
from sklearn.metrics import accuracy_score

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)