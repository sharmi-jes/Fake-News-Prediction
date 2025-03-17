from flask import Flask,request,render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import Normalizer
from sklearn.metrics import accuracy_score

app=Flask(__name__)


# load the all modesl
import joblib

tfidf = joblib.load('tfidf_vectorizer.pkl')


pca = joblib.load('pca_transformer.pkl')


normalizer = joblib.load('normalizer.pkl')


model = joblib.load('news_classifier_model.pkl')

print("All components loaded successfully!")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def predictdata():
    if request.method=='GET':
        return render_template('home.html')
    
    else:
        


if __name__=="__main__":
    app.run(debug=True)