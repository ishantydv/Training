from flask import Flask,render_template,url_for,request
import joblib

model = joblib.load('logistic_regression.lb')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

# @app.route("/prediction",methods=['GET','POST'])
# def prediction():
#     if request.method == "POST":

        


if __name__ == "__main__":
    app.run(debug=True)